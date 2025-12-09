import json
from collections import Counter
import re

def analyze_video_info(file_path="downloads/video_info.json"):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    description = data.get("description", "")
    words = re.findall(r'\b\w+\b', description.lower())
    word_freq = Counter(words).most_common(10)

    analysis = {
        "title": data["title"],
        "author": data["author"],
        "views": data["views"],
        "top_words_in_description": word_freq
    }

    return analysis
