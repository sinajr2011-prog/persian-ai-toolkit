"""
ماژول خلاصه‌سازی متن فارسی (استخراجی ساده و سبک)
"""

from typing import List, Dict, Any
import re


def _split_sentences(text: str) -> List[str]:
    """جدا کردن جملات فارسی به صورت ساده"""
    # جداکننده بر اساس نقطه، علامت سؤال، تعجب
    sentences = re.split(r'[.!?؟\n]+', text)
    return [s.strip() for s in sentences if s.strip()]


def summarize(text: str, max_sentences: int = 3) -> Dict[str, Any]:
    """
    خلاصه‌سازی استخراجی ساده متن فارسی.

    فعلاً بر اساس طول جمله و موقعیت عمل می‌کند.
    در نسخه‌های بعدی با مدل‌های abstractive جایگزین می‌شود.

    Args:
        text: متن ورودی
        max_sentences: حداکثر تعداد جملات خلاصه

    Returns:
        دیکشنری شامل خلاصه و اطلاعات اضافی
    """
    if not text or not text.strip():
        return {
            "summary": "",
            "original_length": 0,
            "summary_length": 0,
            "message": "متن خالی است"
        }

    sentences = _split_sentences(text)

    if len(sentences) <= max_sentences:
        summary = " ".join(sentences)
    else:
        # جملات اول + جملات بلندتر اولویت دارند (ساده)
        scored = []
        for i, sent in enumerate(sentences):
            score = len(sent) * 0.6  # طول
            if i == 0:
                score += 30  # جمله اول مهم‌تر
            if i == len(sentences) - 1:
                score += 15  # جمله آخر هم مهم
            scored.append((score, sent))

        scored.sort(reverse=True)
        selected = [s for _, s in scored[:max_sentences]]

        # حفظ ترتیب اصلی
        summary_sentences = [s for s in sentences if s in selected]
        summary = " ".join(summary_sentences)

    return {
        "summary": summary,
        "original_sentences": len(sentences),
        "summary_sentences": min(max_sentences, len(sentences)),
        "original_length": len(text),
        "summary_length": len(summary),
        "compression_ratio": round(len(summary) / max(len(text), 1), 3)
    }
