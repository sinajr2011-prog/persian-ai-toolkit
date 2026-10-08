"""
ماژول تشخیص احساس برای متن فارسی
نسخه بهبودیافته مبتنی بر لغات کلیدی + آماده برای مدل‌های واقعی
"""

from typing import Dict, Any, List
import re


# لغات مثبت و منفی گسترش‌یافته
POSITIVE_WORDS: List[str] = [
    "عالی", "عالیه", "عالی بود", "عالی هست", "محشر", "محشره", "فوق‌العاده", "فوق العاده",
    "دوست داشتم", "دوست دارم", "عاشق", "عاشقشم", "عاشقتم", "خوشحال", "خوشحالم",
    "ممنون", "مرسی", "دمت گرم", "عالی کار کردی", "حرف نداره", "بی‌نظیر", "بینظیر",
    "خوب", "خوبه", "خوب بود", "عالیه واقعا", "پیشنهاد می‌کنم", "پیشنهاد میکنم",
    "راضی", "راضی هستم", "عالیه دیگه", "بهترین", "بهترینه", "لذت بردم", "لذت‌بخش"
]

NEGATIVE_WORDS: List[str] = [
    "بد", "بده", "بد بود", "افتضاح", "افتضاحه", "افتضاح بود", "مزخرف", "مزخرفه",
    "ضعیف", "ضعیفه", "متنفرم", "متنفرم از", "ناراحت", "ناراحتم", "عصبانی", "عصبانی‌ام",
    "پشیمون", "پشیمونم", "اصلا خوب نبود", "افتضاح مطلق", "خراب", "خرابه",
    "نپسندیدم", "دوست نداشتم", "بدرد نخور", "بی‌ارزش", "افتضاح کار کرد", "ناامید"
]


def analyze_sentiment(text: str) -> Dict[str, Any]:
    """
    تشخیص احساس متن فارسی.

    Args:
        text: متن فارسی ورودی

    Returns:
        دیکشنری شامل:
        - label: positive / negative / neutral
        - score: امتیاز اطمینان (۰ تا ۱)
        - positive_hits / negative_hits
        - matched words
        - text_preview
    """
    if not text or not str(text).strip():
        return {
            "label": "neutral",
            "score": 0.0,
            "positive_hits": 0,
            "negative_hits": 0,
            "message": "متن خالی است",
            "text_preview": ""
        }

    cleaned = re.sub(r"\s+", " ", text.strip())

    pos_hits = [w for w in POSITIVE_WORDS if w in cleaned]
    neg_hits = [w for w in NEGATIVE_WORDS if w in cleaned]

    pos_count = len(pos_hits)
    neg_count = len(neg_hits)

    if pos_count > neg_count:
        label = "positive"
        score = min(0.55 + pos_count * 0.12, 0.97)
    elif neg_count > pos_count:
        label = "negative"
        score = min(0.55 + neg_count * 0.12, 0.97)
    else:
        label = "neutral"
        score = 0.5

    return {
        "label": label,
        "score": round(score, 3),
        "positive_hits": pos_count,
        "negative_hits": neg_count,
        "matched_positive": pos_hits[:5],
        "matched_negative": neg_hits[:5],
        "text_preview": cleaned[:120] + ("..." if len(cleaned) > 120 else "")
    }
