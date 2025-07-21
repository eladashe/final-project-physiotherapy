import numpy as np
from numpy import random

# Calculates the risk of falling (as a number between 0 and 1) according to a logistic model
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
    return round(probability,4)

def main(name,width):
    res_dic ={}
    res_dic['steps_count'] = random.randint(7,30)
    res_dic['wrong_steps'] = random.randint(0,20)
    res_dic['Time'] = random.rand()*20+5
    res_dic['fall_risk'] = predict_risk_probability(res_dic['steps_count'],res_dic['wrong_steps'],res_dic['Time'])
    # print(res_dic)
    return res_dic

main('Amir',22)