"""
FastAPI application for Persian AI Toolkit
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import sys
import os

# Add package path
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
    description="Open-source AI tools specially designed for the Persian (Farsi) language",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Allow all origins for easy testing (restrict in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class TextRequest(BaseModel):
    text: str = Field(..., min_length=1, description="Persian text")
    use_model: bool = Field(False, description="Use HuggingFace model (slower but more accurate)")


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
        "version": "1.0.0",
        "docs": "/docs",
        "endpoints": ["/sentiment", "/summarize", "/caption", "/keywords", "/clean"]
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/sentiment")
def sentiment_endpoint(req: TextRequest):
    """Persian sentiment analysis"""
    try:
        return analyze_sentiment(req.text, use_model=req.use_model)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/summarize")
def summarize_endpoint(req: SummarizeRequest):
    """Extractive text summarization"""
    try:
        return summarize(req.text, max_sentences=req.max_sentences)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/caption")
def caption_endpoint(req: CaptionRequest):
    """Generate Instagram caption and hashtags"""
    try:
        return generate_caption(req.text, style=req.style)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/keywords")
def keywords_endpoint(req: TextRequest):
    """Extract keywords from Persian text"""
    try:
        keywords = extract_keywords(req.text)
        return {"keywords": keywords, "count": len(keywords)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/clean")
def clean_endpoint(req: TextRequest):
    """Clean and normalize Persian text"""
    try:
        cleaned = clean_persian_text(req.text)
        return {"original": req.text, "cleaned": cleaned}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
