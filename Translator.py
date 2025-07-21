import json

class Translator:
    def __init__(self, language_code='en'):
        self.language_code = language_code
        self.translations = self.load_translations()

    def load_translations(self):
        try:
            with open(f"translations/{self.language_code}.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            print("⚠️ Translation file not found!")
            return {}

    def tr(self, key, **kwargs):
        text = self.translations.get(key, f"[{key}]")
        try:
            return text.format(**kwargs)
        except KeyError:
            return text  # If dynamic value is missing, return without blowing up
