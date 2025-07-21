import json, os

SETTINGS_FILE = os.path.join("translations", "local_settings.json")

def load_saved_language():
    if os.path.exists(SETTINGS_FILE):
        try:
            with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
                return json.load(f).get("language", "en")
        except Exception as e:
            print(f"⚠️ Failed to load language settings. Defaulting to 'he'. Error: {e}")
            return "he"
    else:
        # File does not exist - we will create it with default
        save_language("en", announce_creation=True)
        return "en"

def save_language(lang_code, announce_creation=False):
    try:
        with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
            json.dump({"language": lang_code}, f, ensure_ascii=False, indent=2)
        if announce_creation:
            print(f"📄 local_settings.json created with default language '{lang_code}'")
    except Exception as e:
        print(f"❌ Failed to save language setting: {e}")

