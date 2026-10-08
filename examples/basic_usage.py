"""
مثال کامل استفاده از Persian AI Toolkit
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from persian_ai import (
    analyze_sentiment,
    summarize,
    generate_caption,
    extract_keywords,
)


def main():
    print("=" * 60)
    print("🇮🇷  Persian AI Toolkit - نسخه ۰.۲")
    print("=" * 60)

    # ---------- ۱. تشخیص احساس ----------
    print("\n【 ۱. تشخیص احساس 】")
    samples = [
        "این محصول عالیه واقعاً دوست داشتم و محشره!",
        "خیلی ضعیف و افتضاح بود، پشیمون شدم از خرید.",
        "نه خوب بود نه بد، معمولی بود.",
    ]

    for text in samples:
        result = analyze_sentiment(text)
        print(f"\nمتن: {text}")
        print(f"→ احساس: {result['label']} | امتیاز: {result['score']}")
        if result.get("matched_positive"):
            print(f"  کلمات مثبت: {result['matched_positive']}")
        if result.get("matched_negative"):
            print(f"  کلمات منفی: {result['matched_negative']}")

    # ---------- ۲. خلاصه‌سازی ----------
    print("\n\n【 ۲. خلاصه‌سازی متن 】")
    long_text = """
    امروز هوا خیلی عالی بود. رفتم پارک و قدم زدم. 
    بعدش با دوستام قهوه خوردیم و کلی خندیدیم. 
    بعدازظهر هم فیلم دیدم که خیلی محشر بود. 
    کلاً روز فوق‌العاده‌ای داشتم و احساس خوشحالی می‌کنم.
    """
    summary_result = summarize(long_text, max_sentences=2)
    print(f"متن اصلی ({summary_result['original_sentences']} جمله):")
    print(long_text.strip())
    print(f"\nخلاصه ({summary_result['summary_sentences']} جمله):")
    print(summary_result['summary'])
    print(f"نسبت فشرده‌سازی: {summary_result['compression_ratio']}")

    # ---------- ۳. تولید کپشن ----------
    print("\n\n【 ۳. تولید کپشن اینستاگرام 】")
    caption_result = generate_caption("غروب آفتاب توی شمال، لحظه‌ای که همه چی آرومه")
    print("کپشن:")
    print(caption_result['caption'])
    print("\nهشتگ‌ها:")
    print(" ".join(caption_result['hashtags']))
    print("\nپست کامل:")
    print(caption_result['full_post'])

    # ---------- ۴. کلمات کلیدی ----------
    print("\n\n【 ۴. استخراج کلمات کلیدی 】")
    keywords = extract_keywords(long_text)
    print("کلمات کلیدی:", " | ".join(keywords))

    print("\n" + "=" * 60)
    print("تمام! پروژه آماده توسعه بیشتره 🚀")
    print("=" * 60)


if __name__ == "__main__":
    main()
