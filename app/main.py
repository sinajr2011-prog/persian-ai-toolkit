"""
FastAPI application for Persian AI Toolkit
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
import sys
import os

# اضافه کردن مسیر پکیج
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from persian_ai import (
    analyze_sentiment,
    summarize,
    generate_caption,
    extract_keywords,
    clean_persian_text,
)

app = FastAPI(
    title="Persian AI Toolkit",
    description="ابزارهای هوش مصنوعی مخصوص زبان فارسی",
    version="0.2.0",
    docs_url="/docs",
    redoc_url="/redoc",
)


class TextRequest(BaseModel):
    text: str = Field(..., min_length=1, description="متن فارسی")
    use_model: bool = Field(False, description="استفاده از مدل HuggingFace (کندتر ولی دقیق‌تر)")


class SummarizeRequest(BaseModel):
    text: str = Field(..., min_length=1)
    max_sentences: int = Field(3, ge=1, le=10)


class CaptionRequest(BaseModel):
    text: str = Field(..., min_length=1)
    style: str = Field("casual")


@app.get("/")
def root():
    return {
        "message": "Persian AI Toolkit API is running 🇮🇷",
        "version": "0.2.0",
        "docs": "/docs",
        "endpoints": ["/sentiment", "/summarize", "/caption", "/keywords", "/clean"]
    }


@app.post("/sentiment")
def sentiment_endpoint(req: TextRequest):
    """تشخیص احساس متن فارسی"""
    try:
        result = analyze_sentiment(req.text, use_model=req.use_model)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/summarize")
def summarize_endpoint(req: SummarizeRequest):
    """خلاصه‌سازی متن"""
    try:
        result = summarize(req.text, max_sentences=req.max_sentences)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/caption")
def caption_endpoint(req: CaptionRequest):
    """تولید کپشن و هشتگ اینستاگرام"""
    try:
        result = generate_caption(req.text, style=req.style)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/keywords")
def keywords_endpoint(req: TextRequest):
    """استخراج کلمات کلیدی"""
    try:
        keywords = extract_keywords(req.text)
        return {"keywords": keywords, "count": len(keywords)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/clean")
def clean_endpoint(req: TextRequest):
    """پاکسازی متن فارسی"""
    try:
        cleaned = clean_persian_text(req.text)
        return {"original": req.text, "cleaned": cleaned}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
