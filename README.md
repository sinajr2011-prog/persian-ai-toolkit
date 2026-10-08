# Persian AI Toolkit 🇮🇷

**Open-source AI tools specially designed for the Persian (Farsi) language**

A production-ready toolkit for Persian NLP: sentiment analysis, text summarization, Instagram caption & hashtag generation, keyword extraction, text cleaning, and a full FastAPI service.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-ready-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Version](https://img.shields.io/badge/Version-1.0.0-orange)

---

## ✨ Features (v1.0.0)

| Feature                      | Status | Description                                      |
|-----------------------------|--------|--------------------------------------------------|
| Sentiment Analysis          | ✅     | Strong rule-based + optional HuggingFace model   |
| Text Summarization          | ✅     | Lightweight extractive summarizer                |
| Caption & Hashtag Generator | ✅     | Perfect for Instagram                            |
| Keyword Extraction          | ✅     | Ready to use                                     |
| Persian Text Cleaning       | ✅     | Arabic-to-Persian normalization                  |
| Full FastAPI                | ✅     | Production-ready API with CORS & health check    |
| Docker Support              | ✅     | Dockerfile + docker-compose included             |
| Installable Package         | ✅     | `pip install -e .` ready                         |

---

## 🚀 Quick Start

### 1. Clone & Install

```bash
git clone https://github.com/sinajr2011-prog/persian-ai-toolkit.git
cd persian-ai-toolkit

python -m venv venv
source venv/bin/activate          # Linux / Mac
# venv\Scripts\activate         # Windows

pip install -e .
# Optional: for real ML models
pip install -e ".[ml]"
```

### 2. Run the example

```bash
python examples/basic_usage.py
```

### 3. Run the API

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Open Swagger UI → [http://localhost:8000/docs](http://localhost:8000/docs)

### 4. Run with Docker

```bash
docker compose up --build
```

---

## 📡 API Endpoints

| Method | Endpoint       | Description                    |
|--------|----------------|--------------------------------|
| GET    | `/`            | Service info                   |
| GET    | `/health`      | Health check                   |
| POST   | `/sentiment`   | Sentiment analysis             |
| POST   | `/summarize`   | Text summarization             |
| POST   | `/caption`     | Caption & hashtags             |
| POST   | `/keywords`    | Keyword extraction             |
| POST   | `/clean`       | Text cleaning                  |

Example:
```bash
curl -X POST "http://localhost:8000/sentiment" \
  -H "Content-Type: application/json" \
  -d '{"text": "این محصول عالیه و محشره!", "use_model": false}'
```

---

## 📦 Python Usage

```python
from persian_ai import (
    analyze_sentiment,
    summarize,
    generate_caption,
    extract_keywords,
    clean_persian_text,
)

# Sentiment
print(analyze_sentiment("عاشق این اپ شدم!"))

# Summarize
print(summarize(long_text, max_sentences=2))

# Instagram caption
print(generate_caption("غروب شمال"))

# Keywords
print(extract_keywords(text))

# Clean text
print(clean_persian_text(messy_text))
```

For higher accuracy (downloads model on first use):
```python
analyze_sentiment("your text", use_model=True)
```

---

## 📁 Project Structure

```
persian-ai-toolkit/
├── app/
│   └── main.py                 # FastAPI application
├── src/persian_ai/
│   ├── __init__.py
│   ├── sentiment.py            # Sentiment (rule-based + HF)
│   ├── summarizer.py
│   ├── caption.py
│   └── utils.py
├── examples/
│   └── basic_usage.py
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── requirements.txt
└── README.md
```

---

## 🗺️ Roadmap

- [ ] Better Persian transformer models out of the box
- [ ] Speech-to-Text with Iranian accent support
- [ ] Simple web dashboard
- [ ] More evaluation benchmarks

---

## 📄 License

MIT License © 2026 [SinaJr](https://github.com/sinajr2011-prog)

---

Made with ❤️ for the Persian-speaking developer community
