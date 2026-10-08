"""
Persian AI Toolkit
Open-source AI tools specially designed for the Persian (Farsi) language
"""

__version__ = "1.1.0"

from .sentiment import analyze_sentiment
from .summarizer import summarize
from .caption import generate_caption
from .utils import clean_persian_text, extract_keywords, normalize_arabic_chars
from .speech import speech_to_text, list_supported_formats
from .models import list_available_models, get_pipeline

__all__ = [
    "analyze_sentiment",
    "summarize",
    "generate_caption",
    "clean_persian_text",
    "extract_keywords",
    "normalize_arabic_chars",
    "speech_to_text",
    "list_supported_formats",
    "list_available_models",
    "get_pipeline",
]
