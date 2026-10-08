"""
مثال ساده استفاده از Persian AI Toolkit
"""

import sys
import os

# اضافه کردن مسیر src
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from persian_ai import analyze_sentiment


def main():
    samples = [
        "این محصول عالیه واقعاً دوست داشتم!",
        "خیلی ضعیف و افتضاح بود، پشیمون شدم.",
        "نه خوب بود نه بد، معمولی بود.",
        "عاشق این اپلیکیشن شدم، محشره!",
    ]

    print("=== Persian AI Toolkit - Sentiment Analysis ===\n")

    for text in samples:
        result = analyze_sentiment(text)
        print(f"متن: {text}")
        print(f"احساس: {result['label']} | امتیاز: {result['score']}")
        print("-" * 50)


if __name__ == "__main__":
    main()
