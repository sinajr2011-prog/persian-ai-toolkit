"""
تولید کپشن و هشتگ برای اینستاگرام و شبکه‌های اجتماعی (فارسی)
"""

from typing import Dict, Any, List
import random


# قالب‌های ساده کپشن
CAPTION_TEMPLATES = [
    "{text} ✨", 
    "لحظه‌ای از زندگی: {text} 🌟",
    "{text} | چی فکر می‌کنی؟ 💭",
    "این یکی رو دوست داشتم ❤️\n{text}",
    "{text}\nنظرتون چیه؟ 👇",
]

# هشتگ‌های عمومی فارسی
GENERAL_HASHTAGS = [
    "#فارسی", "#ایران", "#تهران", "#عکس_روز", "#زندگی", 
    "#حس_خوب", "#لحظه_ها", "#ایرانی", "#پرسیان", "#دوست_دارم"
]


def generate_caption(text: str, style: str = "casual") -> Dict[str, Any]:
    """
    تولید کپشن و هشتگ از روی متن.

    Args:
        text: متن اصلی یا توضیح عکس
        style: سبک کپشن (فعلاً فقط casual)

    Returns:
        دیکشنری شامل کپشن نهایی و لیست هشتگ‌ها
    """
    if not text or not text.strip():
        return {
            "caption": "",
            "hashtags": [],
            "full_post": "",
            "message": "متن خالی است"
        }

    clean_text = text.strip()

    # انتخاب تصادفی قالب
    template = random.choice(CAPTION_TEMPLATES)
    caption = template.format(text=clean_text)

    # هشتگ‌ها (ساده: کلمات کلیدی + عمومی)
    words = [w for w in clean_text.split() if len(w) > 2][:4]
    custom_tags = [f"#{w}" for w in words]

    hashtags = list(dict.fromkeys(custom_tags + random.sample(GENERAL_HASHTAGS, 4)))

    full_post = caption + "\n\n" + " ".join(hashtags)

    return {
        "caption": caption,
        "hashtags": hashtags,
        "full_post": full_post,
        "style": style
    }
