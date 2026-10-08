# Persian AI Toolkit 🇮🇷

**ابزارهای هوش مصنوعی مخصوص زبان فارسی**

پروژه اوپن‌سورس کامل برای پردازش زبان طبیعی فارسی: تشخیص احساس، خلاصه‌سازی، تولید کپشن، استخراج کلمات کلیدی و API آماده.

---

## ✨ قابلیت‌های فعلی (نسخه ۰.۳)

| قابلیت | وضعیت | توضیح |
|--------|--------|------|
| تشخیص احساس | ✅ | Rule-based قوی + پشتیبانی اختیاری از مدل HuggingFace |
| خلاصه‌سازی متن | ✅ | استخراجی سبک و سریع |
| تولید کپشن + هشتگ | ✅ | مناسب اینستاگرام |
| استخراج کلمات کلیدی | ✅ | آماده |
| پاکسازی متن فارسی | ✅ | نرمال‌سازی عربی به فارسی |
| **FastAPI کامل** | ✅ | همه قابلیت‌ها به صورت API |
| Speech-to-Text | ⏳ | در نقشه راه |

---

## 🚀 نصب و اجرا

```bash
git clone https://github.com/sinajr2011-prog/persian-ai-toolkit.git
cd persian-ai-toolkit

python -m venv venv
source venv/bin/activate          # Linux / Mac
# venv\Scripts\activate         # Windows

pip install -r requirements.txt
```

### اجرای مثال
```bash
python examples/basic_usage.py
```

### اجرای API
```bash
cd app
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

بعد برو به: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📡 اندپوینت‌های API

- `POST /sentiment` → تشخیص احساس
- `POST /summarize` → خلاصه‌سازی
- `POST /caption` → کپشن و هشتگ
- `POST /keywords` → کلمات کلیدی
- `POST /clean` → پاکسازی متن

مثال درخواست:
```bash
curl -X POST "http://localhost:8000/sentiment" \
  -H "Content-Type: application/json" \
  -d '{"text": "این محصول عالیه و محشره!", "use_model": false}'
```

---

## 📦 استفاده در کد پایتون

```python
from persian_ai import analyze_sentiment, summarize, generate_caption, extract_keywords

print(analyze_sentiment("عاشق این اپ شدم!"))
print(summarize(long_text, max_sentences=2))
print(generate_caption("غروب شمال"))
print(extract_keywords(text))
```

برای مدل واقعی (دقیق‌تر ولی نیاز به دانلود مدل):
```python
analyze_sentiment("متن شما", use_model=True)
```

---

## 📁 ساختار پروژه

```
persian-ai-toolkit/
├── app/
│   └── main.py              # FastAPI application
├── src/persian_ai/
│   ├── __init__.py
│   ├── sentiment.py         # تشخیص احساس (rule + HF)
│   ├── summarizer.py
│   ├── caption.py
│   └── utils.py
├── examples/
│   └── basic_usage.py
├── requirements.txt
└── README.md
```

---

## 🗺️ نقشه راه بعدی

- [ ] اتصال کامل به مدل‌های بهتر فارسی
- [ ] Speech-to-Text با پشتیبانی لهجه
- [ ] نسخه Docker
- [ ] داشبورد ساده وب

---

ساخته شده با ❤️ توسط [SinaJr](https://github.com/sinajr2011-prog)
