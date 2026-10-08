# Persian AI Toolkit 🇮🇷

**ابزارهای هوش مصنوعی مخصوص زبان فارسی**

یک پروژه اوپن‌سورس جدی برای پردازش زبان طبیعی فارسی، تشخیص احساس، خلاصه‌سازی متن، تولید کپشن و ابزارهای کاربردی AI برای فارسی‌زبانان.

---

## ✨ قابلیت‌های فعلی (نسخه ۰.۲)

- [x] **تشخیص احساس (Sentiment Analysis)** — با لغات کلیدی غنی فارسی
- [x] **خلاصه‌سازی متن** — استخراجی سبک و سریع
- [x] **تولید کپشن و هشتگ اینستاگرام**
- [x] **استخراج کلمات کلیدی**
- [x] **پاکسازی و نرمال‌سازی متن فارسی**
- [ ] تبدیل گفتار به متن (Speech-to-Text)
- [ ] API با FastAPI
- [ ] مدل‌های واقعی HuggingFace (ParsBERT و ...)

---

## 🚀 شروع سریع

```bash
git clone https://github.com/sinajr2011-prog/persian-ai-toolkit.git
cd persian-ai-toolkit

python -m venv venv
source venv/bin/activate          # Linux / Mac
# venv\Scripts\activate         # Windows

pip install -r requirements.txt

# اجرای مثال
python examples/basic_usage.py
```

---

## 📦 استفاده در کد

```python
from persian_ai import (
    analyze_sentiment,
    summarize,
    generate_caption,
    extract_keywords,
    clean_persian_text,
)

# تشخیص احساس
result = analyze_sentiment("این محصول عالیه و محشره!")
print(result["label"], result["score"])

# خلاصه‌سازی
summary = summarize(long_text, max_sentences=2)
print(summary["summary"])

# کپشن اینستاگرام
caption = generate_caption("غروب شمال")
print(caption["full_post"])

# کلمات کلیدی
keywords = extract_keywords(text)
```

---

## 📁 ساختار پروژه

```
persian-ai-toolkit/
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
├── src/
│   └── persian_ai/
│       ├── __init__.py
│       ├── sentiment.py      # تشخیص احساس
│       ├── summarizer.py     # خلاصه‌سازی
│       ├── caption.py        # کپشن و هشتگ
│       └── utils.py          # ابزارهای کمکی
├── examples/
│   └── basic_usage.py
└── tests/
```

---

## 🛠️ تکنولوژی‌ها

- Python 3.10+
- آماده برای FastAPI + Hugging Face Transformers
- فعلاً کاملاً سبک و بدون نیاز به GPU (rule-based + extractive)

---

## 🗺️ نقشه راه

1. اضافه کردن مدل واقعی Sentiment با ParsBERT
2. API کامل با FastAPI
3. پشتیبانی از Speech-to-Text
4. نسخه سبک‌تر برای موبایل و CPU ضعیف

---

## 🤝 مشارکت

هر ایده‌ای داری Issue باز کن یا مستقیم PR بفرست.  
هدف ساخت بهترین ابزار اوپن‌سورس AI برای زبان فارسیه.

---

ساخته شده با ❤️ توسط [SinaJr](https://github.com/sinajr2011-prog)
