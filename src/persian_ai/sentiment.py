"""
ماژول تشخیص احساس برای متن فارسی
"""

from typing import Dict, Any


def analyze_sentiment(text: str) -> Dict[str, Any]:
    """
    تشخیص احساس متن فارسی (نسخه ساده و پایه).

    در نسخه‌های بعدی با مدل‌های واقعی مثل ParsBERT جایگزین می‌شود.

    Args:
        text: متن فارسی ورودی

    Returns:
        دیکشنری شامل احساس و امتیاز
    """
    if not text or not text.strip():
        return {
            "label": "neutral",
            "score": 0.0,
            "message": "متن خالی است"
        }

    # نسخه ساده مبتنی بر کلمات کلیدی (موقت)
    positive_words = ["عالی", "خوب", "دوست داشتم", "عالیه", "محشر", "عالی بود", "ممنون", "عالی هست", "خوشحال", "عاشق"]
    negative_words = ["بد", "افتضاح", "متنفرم", "ضعیف", "مزخرف", "ناراحت", "عصبانی", "افتضاحه", "بد بود"]

    text_lower = text.lower()

    pos_count = sum(1 for word in positive_words if word in text_lower)
    neg_count = sum(1 for word in negative_words if word in text_lower)

    if pos_count > neg_count:
        label = "positive"
        score = min(0.6 + pos_count * 0.1, 0.95)
    elif neg_count > pos_count:
        label = "negative"
        score = min(0.6 + neg_count * 0.1, 0.95)
    else:
        label = "neutral"
        score = 0.5

    return {
        "label": label,
        "score": round(score, 3),
        "text": text[:100] + ("..." if len(text) > 100 else "")
    }
