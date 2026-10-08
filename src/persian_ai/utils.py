"""
ابزارهای کمکی
"""

def clean_persian_text(text: str) -> str:
    """پاکسازی ساده متن فارسی"""
    if not text:
        return ""
    # حذف فاصله‌های اضافی
    text = " ".join(text.split())
    return text.strip()
