########################################################################
#
# Copyright (c) 2022, STEREOLABS.
#
# All rights reserved.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
########################################################################
import winsound
import pyzed.sl as sl
import time
import numpy as np
import pandas as pd
import os
from sklearn.decomposition import PCA

def predict_risk_probability(steps_count, wrong_steps, trial_time):
    # Coefficients of the model
    intercept = -23.3132
    coef_steps = 0.4935
    coef_wrong = 0.2591
    coef_time = 0.1959
    # Calculate the linear predictor (logit)
    logit = intercept + coef_steps * steps_count + coef_wrong * wrong_steps + coef_time * trial_time
    # Apply the logistic (sigmoid) function to get probability
    probability = 1 / (1 + np.exp(-logit))
    return probability

def wrong_steps_count_pca(df,width,param=8):
    avg_width = (df['right_x'] - df['left_x']).mean()
    pca = PCA(n_components=2)
    pca_right = pca.fit_transform(df[['right_z', 'right_x']].values)
    pca_left = pca.fit_transform(df[['left_z', 'left_x']].values)
    # right = pca_right.T[1]
    # left = pca_left.T[1]
    right = pca_right.T[1]+avg_width/2
    left = pca_left.T[1]- avg_width/2
    right_border = float(width/2)
    left_border = float(-1*width/2)
    wrong_counter =0
    thresh_param =0     #number of frames to consider wrong step
    for i in range(min(len(right),len(left))):
        if right[i]>right_border or left[i]<left_border or right[i]<left_border or left[i]>right_border:
            thresh_param+=1
        else:
            thresh_param=0
        if thresh_param==param:
            wrong_counter+=1
    return wrong_counter

def steps_Count(right_z, left_z,param=9):   #gets two lists of z coordinates of two joints
    count = 0
    plus_minus =[]
    plus_minus_counter =1
    steps_count=0           #used to be 2
    max_len = max(len(right_z.values),len(left_z.values))
    for i in range(max_len):
    # for right,left in right_z.values,left_z.values:
        right = right_z.values[i]
        left = left_z.values[i]
        if right == None:   #if there is no value take the last one
            right = last_right
        if left == None:
            left = last_left
        if right < left:
            plus_minus.append('+')
        else:
            plus_minus.append('-')
        last_right = right          #save the last value for none cells
        last_left = left
    last_symbol = plus_minus[0]
    for v in plus_minus[1:]:
        if last_symbol==v:
            plus_minus_counter+=1
        else:
            last_symbol = v
            plus_minus_counter=1
        if plus_minus_counter==param:
            steps_count+=1
    return steps_count

#temporary function for steps calculation using PCA
def steps_Count2(df,param=9):   #gets two lists of z coordinates of two joints
    pca = PCA(n_components=2)
    pca_right = pca.fit_transform(df[['right_z', 'right_x']].values)
    pca_left = pca.fit_transform(df[['left_z', 'left_x']].values)
    right_pca = pca_right.T[0]
    left_pca = pca_left.T[0]
    plus_minus =[]
    plus_minus_counter =0
    steps_count=0
    max_len = max(len(right_pca),len(left_pca))
    for i in range(max_len):
    # for right,left in right_z.values,left_z.values:
        right = right_pca[i]
        left = left_pca[i]
        if right < left:
            plus_minus.append('+')
        else:
            plus_minus.append('-')
    last_symbol = plus_minus[0]
    for i in range(1,len(plus_minus)-1):
        if last_symbol==plus_minus[i]:
            plus_minus_counter+=1
        elif last_symbol==plus_minus[i+1]:
            continue
        else:
            last_symbol = plus_minus[i]
            plus_minus_counter=0
        if plus_minus_counter==param:
            steps_count+=1
    return steps_count


def main(name,width):
    # Create a Camera object
    zed = sl.Camera()
    # Create a InitParameters object and set configuration parameters
    init_params = sl.InitParameters()
    init_params.camera_resolution = sl.RESOLUTION.HD720  # Use HD720 video mode
    init_params.depth_mode = sl.DEPTH_MODE.PERFORMANCE
    init_params.coordinate_units = sl.UNIT.METER
    init_params.sdk_verbose = True

    # Open the camera
    err = zed.open(init_params)
    if err != sl.ERROR_CODE.SUCCESS:
        exit(1)

    obj_param = sl.ObjectDetectionParameters()
    # Different model can be chosen, optimizing the runtime or the accuracy
    obj_param.detection_model = sl.DETECTION_MODEL.HUMAN_BODY_FAST
    obj_param.enable_tracking = True
    obj_param.image_sync = True
    obj_param.enable_mask_output = False
    # Optimize the person joints position, requires more computations
    obj_param.enable_body_fitting = True
    obj_param.body_format = sl.BODY_FORMAT.POSE_34

    camera_infos = zed.get_camera_information()
    if obj_param.enable_tracking:
        positional_tracking_param = sl.PositionalTrackingParameters()
        # positional_tracking_param.set_as_static = True
        positional_tracking_param.set_floor_as_origin = True
        zed.enable_positional_tracking(positional_tracking_param)

    print("Object Detection: Loading Module...")

    err = zed.enable_object_detection(obj_param)
    if err != sl.ERROR_CODE.SUCCESS:
        print(repr(err))
        zed.close()
        exit(1)
    objects = sl.Objects()
    obj_runtime_param = sl.ObjectDetectionRuntimeParameters()
    # For outdoor scene or long range, the confidence should be lowered to avoid missing detections (~20-30)
    # For indoor scene or closer range, a higher confidence limits the risk of false positives and increase the precision (~50+)
    obj_runtime_param.detection_confidence_threshold = 15
    ls_frames =[]
    frame_num=0
    flag = True
    winsound.Beep(2000,2000)
    starting_time = time.time()
    backup = []
    while flag and zed.grab() == sl.ERROR_CODE.SUCCESS:
        err = zed.retrieve_objects(objects, obj_runtime_param)
        if objects.is_new:
            obj_array = objects.object_list
            print(str(len(obj_array)) + " Person(s) detected\n")
            if abs(starting_time-time.time())>30:
                flag = False
                end_time = time.time()
            if len(obj_array) > 1:
                for i in range(len(obj_array)):
                    keypoint = obj_array[i].keypoint
                    backup.append(
                        [keypoint[20][0], keypoint[20][1], keypoint[20][2], keypoint[24][0], keypoint[24][1],
                         keypoint[24][2]])
            if len(obj_array) > 0:
                first_object = obj_array[0]
                print("First Person attributes:")
                print(" Confidence (" + str(int(first_object.confidence)) + "/100)")
                position = first_object.position
                velocity = first_object.velocity
                dimensions = first_object.dimensions
                keypoint = first_object.keypoint
                ls_frames.append([keypoint[20][0],keypoint[20][1],keypoint[20][2],keypoint[24][0],keypoint[24][1],keypoint[24][2]])   #20=left ankle, 24=right ankle
                frame_num=frame_num+1
                if keypoint[20][2] >= 7.45 or keypoint[24][2]>=7.45:
                    flag = False
                    end_time = time.time()
    print('--------------------------------------------------------------------------------------------')
    # Close the camera
    zed.close()
    headers = ['left_x','left_y','left_z','right_x','right_y','right_z']
    df = pd.DataFrame(data=ls_frames)
    df.columns = headers
    # DIR = 'temp/'
    # DIR = 'Eldery/'
    DIR = 'Stud/'
    # patient_number = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])/2
    df.to_csv('amir_DATA.csv')
    # if len(backup)>0:
    #     df_new = pd.DataFrame(data=backup)
    #     df_new.to_csv(DIR + str(patient_number) + name + str(width) + '_DATA_prob!!!.csv')
    res_dic ={}
    res_dic['steps_count'] = steps_Count(df['right_z'], df['left_z'], 9) +3
    # res_dic['steps_count'] = steps_Count2(df, 8) +3
    res_dic['wrong_steps'] = wrong_steps_count_pca(df, width / 100, 10)
    res_dic['Time'] = end_time-starting_time
    res_dic['fall_risk'] = predict_risk_probability(res_dic['steps_count'],res_dic['wrong_steps'],res_dic['Time'])
    print(res_dic)
    # results = pd.DataFrame(data=res_dic.items())
    # results.to_csv(DIR+name+str(width)+'_Analysis.csv',index=False)
    return res_dic

