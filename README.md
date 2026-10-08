# Persian AI Toolkit 🇮🇷

**Open-source AI tools specially designed for the Persian (Farsi) language**

A complete toolkit for Persian Natural Language Processing: sentiment analysis, text summarization, Instagram caption & hashtag generation, keyword extraction, text cleaning, and a ready-to-use FastAPI.

---

## ✨ Features (v0.3)

| Feature | Status | Description |
|---------|--------|-------------|
| Sentiment Analysis | ✅ | Strong rule-based + optional HuggingFace model |
| Text Summarization | ✅ | Lightweight extractive summarizer |
| Caption & Hashtag Generator | ✅ | Perfect for Instagram |
| Keyword Extraction | ✅ | Ready to use |
| Persian Text Cleaning | ✅ | Arabic-to-Persian normalization |
| **Full FastAPI** | ✅ | All features available as API endpoints |
| Speech-to-Text | ⏳ | On the roadmap |

---

## 🚀 Installation

```bash
git clone https://github.com/sinajr2011-prog/persian-ai-toolkit.git
cd persian-ai-toolkit

python -m venv venv
source venv/bin/activate          # Linux / Mac
# venv\Scripts\activate         # Windows

pip install -r requirements.txt
```

### Run the example
```bash
python examples/basic_usage.py
```

### Run the API
```bash
cd app
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Then open: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📡 API Endpoints

- `POST /sentiment` → Sentiment analysis
- `POST /summarize` → Text summarization
- `POST /caption` → Caption & hashtags
- `POST /keywords` → Keyword extraction
- `POST /clean` → Text cleaning

Example request:
```bash
curl -X POST "http://localhost:8000/sentiment" \
  -H "Content-Type: application/json" \
  -d '{"text": "این محصول عالیه و محشره!", "use_model": false}'
```

---

## 📦 Usage in Python

```python
from persian_ai import analyze_sentiment, summarize, generate_caption, extract_keywords

print(analyze_sentiment("عاشق این اپ شدم!"))
print(summarize(long_text, max_sentences=2))
print(generate_caption("غروب شمال"))
print(extract_keywords(text))
```

For higher accuracy using a real model (requires model download):
```python
analyze_sentiment("your text", use_model=True)
```

---

## 📁 Project Structure

```
persian-ai-toolkit/
├── app/
│   └── main.py              # FastAPI application
├── src/persian_ai/
│   ├── __init__.py
│   ├── sentiment.py         # Sentiment (rule-based + HF)
│   ├── summarizer.py
│   ├── caption.py
│   └── utils.py
├── examples/
│   └── basic_usage.py
├── requirements.txt
└── README.md
```

---

## 🗺️ Roadmap

- [ ] Better Persian transformer models
- [ ] Speech-to-Text with Iranian accent support
- [ ] Docker support
- [ ] Simple web dashboard

---

Made with ❤️ by [SinaJr](https://github.com/sinajr2011-prog)
