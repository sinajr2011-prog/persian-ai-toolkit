"""
ابزارهای کمکی پردازش متن فارسی
"""

import re
from typing import List


def clean_persian_text(text: str) -> str:
    """پاکسازی و نرمال‌سازی ساده متن فارسی"""
    if not text:
        return ""

    # حذف کاراکترهای کنترل و فاصله‌های اضافی
    text = re.sub(r"[\u200c\u200f\u202a-\u202e]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_keywords(text: str, top_n: int = 8) -> List[str]:
    """
    استخراج کلمات کلیدی ساده (بر اساس طول و تکرار).
    نسخه پیشرفته‌تر بعداً با TF-IDF یا مدل اضافه می‌شود.
    """
    if not text:
        return []

    cleaned = clean_persian_text(text)
    words = re.findall(r"[\u0600-\u06FF]{3,}", cleaned)

    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1

    sorted_words = sorted(freq.items(), key=lambda x: (x[1], len(x[0])), reverse=True)
    return [w for w, _ in sorted_words[:top_n]]


def normalize_arabic_chars(text: str) -> str:
    """تبدیل کاراکترهای عربی به فارسی استاندارد"""
    if not text:
        return ""
    replacements = {
        "ي": "ی",
        "ك": "ک",
        "ة": "ه",
        "أ": "ا",
        "إ": "ا",
        "آ": "ا",
    }
    for ar, fa in replacements.items():
        text = text.replace(ar, fa)
    return text
