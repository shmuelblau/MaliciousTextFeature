import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import re
from datetime import datetime
nltk.download('vader_lexicon')  # Compute sentiment labels

class Enricher:
    @staticmethod
    def get_emotion(text):
        score = SentimentIntensityAnalyzer().polarity_scores(text)

        return "positive" if score["compound"] > 0.5 else "negative" if score["compound"] < -0.5 else "neutral"

    @staticmethod
    def get_weapon(text: str, weapons):
        weapons_detected = []
        for weapon in weapons:
            if weapon in text:
                weapons_detected.append(weapon)
        if not weapons_detected:
            return ""
        return weapons_detected


    @staticmethod
    def relevant_timestamp(text):
        matches = re.findall(r'\d{2}/\d{2}/\d{4}', text)
        if not matches:
            return ""
        dates = []
        for match in matches:
            dates.append(datetime.strptime(match,"%d/%m/%Y").date())

        return max(dates).strftime("%d/%m/%Y")




    @staticmethod
    def do_all(data:dict,weapons) -> dict:
        data["sentiment"] = Enricher.get_emotion(data["clean_text"])
        data["weapons_detected"] = Enricher.get_weapon(data["clean_text"],weapons)
        data["relevant_timestamp"] = Enricher.relevant_timestamp(data["text"])
        data["original_text"] = data["text"]
        data.pop("text")
        return data

