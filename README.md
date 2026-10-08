# Persian AI Toolkit 🇮🇷

**Open-source AI tools specially designed for the Persian (Farsi) language**

A production-ready toolkit for Persian NLP: sentiment analysis, text summarization, Instagram caption & hashtag generation, keyword extraction, text cleaning, Speech-to-Text, and a beautiful web dashboard.(Wait for more options...)

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-ready-green)
![Gradio](https://img.shields.io/badge/Gradio-Dashboard-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Version](https://img.shields.io/badge/Version-1.1.0-brightgreen)

---

## ✨ Features (v1.1.0)

| Feature                      | Status | Description                                      |
|-----------------------------|--------|--------------------------------------------------|
| Sentiment Analysis          | ✅     | Rule-based + multiple Persian HF models          |
| Text Summarization          | ✅     | Lightweight extractive summarizer                |
| Caption & Hashtag Generator | ✅     | Perfect for Instagram                            |
| Keyword Extraction          | ✅     | Ready to use                                     |
| Persian Text Cleaning       | ✅     | Arabic-to-Persian normalization                  |
| **Speech-to-Text**          | ✅     | Whisper with Persian / Iranian accent support    |
| **Web Dashboard**           | ✅     | Beautiful Gradio UI                              |
| Full FastAPI                | ✅     | Production-ready API with CORS & health check    |
| Docker Support              | ✅     | Dockerfile + docker-compose                      |
| Benchmarks                  | ✅     | Sentiment evaluation suite                       |

---

## 🚀 Quick Start

```bash
git clone https://github.com/sinajr2011-prog/persian-ai-toolkit.git
cd persian-ai-toolkit

python -m venv venv
source venv/bin/activate

pip install -e .
# For ML models + Whisper:
pip install -e ".[ml]"
```

### Run the Web Dashboard (recommended)
```bash
python app/dashboard.py
```
Open → http://localhost:7860

### Run the API
```bash
uvicorn app.main:app --reload --port 8000
```
Swagger → http://localhost:8000/docs

### Run Benchmark
```bash
python benchmarks/sentiment_benchmark.py
```

### Docker
```bash
docker compose up --build
```

---

## 📡 API Endpoints

| Method | Endpoint     | Description              |
|--------|--------------|--------------------------|
| GET    | `/`          | Service info             |
| GET    | `/health`    | Health check             |
| POST   | `/sentiment` | Sentiment analysis       |
| POST   | `/summarize` | Text summarization       |
| POST   | `/caption`   | Caption & hashtags       |
| POST   | `/keywords`  | Keyword extraction       |
| POST   | `/clean`     | Text cleaning            |

---

## 📦 Python Usage

```python
from persian_ai import (
    analyze_sentiment,
    summarize,
    generate_caption,
    extract_keywords,
    speech_to_text,
    list_available_models,
)

# Sentiment (rule-based or real model)
print(analyze_sentiment("عاشق این اپ شدم!", use_model=True))

# Speech-to-Text (requires openai-whisper)
result = speech_to_text("audio.wav", model_size="base")
print(result["text"])

# Available models
print(list_available_models())
```

---

## 📁 Project Structure

```
persian-ai-toolkit/
├── app/
│   ├── main.py                 # FastAPI
│   └── dashboard.py            # Gradio Web UI
├── src/persian_ai/
│   ├── sentiment.py
│   ├── summarizer.py
│   ├── caption.py
│   ├── speech.py               # Whisper STT
│   ├── models.py               # Model registry
│   └── utils.py
├── benchmarks/
│   └── sentiment_benchmark.py
├── Dockerfile
├── docker-compose.yml
└── pyproject.toml
```

---

## 🗺️ Roadmap

- [x] Better Persian transformer models out of the box
- [x] Speech-to-Text with Iranian accent support
- [x] Simple web dashboard
- [x] More evaluation benchmarks
- [ ] Even better models & fine-tuning scripts
- [ ] Full web dashboard with audio upload

---

## 📄 License

MIT License © 2026 [SinaJr](https://github.com/sinajr2011-prog)

---

Made with ❤️ for the Persian-speaking developer community
