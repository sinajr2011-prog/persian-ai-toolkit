"""
ماژول تشخیص احساس برای متن فارسی
پشتیبانی از حالت rule-based (سبک) و مدل واقعی HuggingFace (اختیاری)
"""

from typing import Dict, Any, List
import re

# لغات مثبت و منفی گسترش‌یافته (حالت سبک)
POSITIVE_WORDS: List[str] = [
    "عالی", "عالیه", "عالی بود", "عالی هست", "محشر", "محشره", "فوق‌العاده", "فوق العاده",
    "دوست داشتم", "دوست دارم", "عاشق", "عاشقشم", "عاشقتم", "خوشحال", "خوشحالم",
    "ممنون", "مرسی", "دمت گرم", "عالی کار کردی", "حرف نداره", "بی‌نظیر", "بینظیر",
    "خوب", "خوبه", "خوب بود", "عالیه واقعا", "پیشنهاد می‌کنم", "پیشنهاد میکنم",
    "راضی", "راضی هستم", "عالیه دیگه", "بهترین", "بهترینه", "لذت بردم", "لذت‌بخش",
    "فوق‌العاده‌ست", "عاشقتم", "دمتش گرم"
]

NEGATIVE_WORDS: List[str] = [
    "بد", "بده", "بد بود", "افتضاح", "افتضاحه", "افتضاح بود", "مزخرف", "مزخرفه",
    "ضعیف", "ضعیفه", "متنفرم", "متنفرم از", "ناراحت", "ناراحتم", "عصبانی", "عصبانی‌ام",
    "پشیمون", "پشیمونم", "اصلا خوب نبود", "افتضاح مطلق", "خراب", "خرابه",
    "نپسندیدم", "دوست نداشتم", "بدرد نخور", "بی‌ارزش", "افتضاح کار کرد", "ناامید",
    "افتضاحه واقعا", "خیلی بده"
]

_pipeline = None


def _load_hf_model() -> bool:
    """بارگذاری مدل HuggingFace در صورت امکان"""
    global _pipeline
    if _pipeline is not None:
        return True
    try:
        from transformers import pipeline
        _pipeline = pipeline(
            "sentiment-analysis",
            model="HooshvareLab/bert-fa-base-uncased-sentiment-digikala",
            tokenizer="HooshvareLab/bert-fa-base-uncased-sentiment-digikala"
        )
        return True
    except Exception:
        return False


def analyze_sentiment(text: str, use_model: bool = False) -> Dict[str, Any]:
    """
    تشخیص احساس متن فارسی.

    Args:
        text: متن فارسی ورودی
        use_model: اگر True باشد از مدل HuggingFace استفاده می‌کند (نیاز به نصب transformers و دانلود مدل)

    Returns:
        دیکشنری نتیجه
    """
    if not text or not str(text).strip():
        return {
            "label": "neutral",
            "score": 0.0,
            "method": "none",
            "message": "متن خالی است",
            "text_preview": ""
        }

    cleaned = re.sub(r"\s+", " ", text.strip())

    # تلاش برای مدل واقعی
    if use_model and _load_hf_model() and _pipeline is not None:
        try:
            result = _pipeline(cleaned[:512])[0]
            label_map = {
                "positive": "positive", "negative": "negative", "neutral": "neutral",
                "POS": "positive", "NEG": "negative", "NEU": "neutral"
            }
            label = label_map.get(result["label"], str(result["label"]).lower())
            return {
                "label": label,
                "score": round(float(result["score"]), 3),
                "method": "huggingface",
                "text_preview": cleaned[:120] + ("..." if len(cleaned) > 120 else "")
            }
        except Exception:
            pass

    # حالت rule-based (همیشه کار می‌کند و سریع است)
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
        "method": "rule-based",
        "positive_hits": pos_count,
        "negative_hits": neg_count,
        "matched_positive": pos_hits[:5],
        "matched_negative": neg_hits[:5],
        "text_preview": cleaned[:120] + ("..." if len(cleaned) > 120 else "")
    }
