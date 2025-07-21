import json, os

SETTINGS_FILE = os.path.join("translations", "local_settings.json")

def load_saved_language():
    if os.path.exists(SETTINGS_FILE):
        try:
            with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
                return json.load(f).get("language", "en")
                # return json.load(f).get("language", "he")
        except Exception as e:
            print(f"⚠️ Failed to load language settings. Defaulting to 'he'. Error: {e}")
            return "en"
            # return "he"
    else:
        # קובץ לא קיים — ניצור עם ברירת מחדל
        # save_language("he", announce_creation=True)
        save_language("en", announce_creation=True)
        return "en"
        # return "he"

def save_language(lang_code, announce_creation=False):
    try:
        with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
            json.dump({"language": lang_code}, f, ensure_ascii=False, indent=2)
        if announce_creation:
            print(f"📄 local_settings.json created with default language '{lang_code}'")
    except Exception as e:
        print(f"❌ Failed to save language setting: {e}")

