"""
Central model management for better Persian transformer models out of the box.
"""

from typing import Optional, Dict, Any

# Recommended Persian models
PERSIAN_MODELS = {
    "sentiment_digikala": {
        "name": "HooshvareLab/bert-fa-base-uncased-sentiment-digikala",
        "task": "sentiment-analysis",
        "description": "Fine-tuned on Digikala reviews – excellent for product sentiment"
    },
    "sentiment_snappfood": {
        "name": "HooshvareLab/bert-fa-base-uncased-sentiment-snappfood",
        "task": "sentiment-analysis",
        "description": "Fine-tuned on Snappfood reviews"
    },
    "parsbert": {
        "name": "HooshvareLab/bert-fa-base-uncased",
        "task": "fill-mask",
        "description": "Base ParsBERT model"
    },
}

_loaded_pipelines: Dict[str, Any] = {}


def get_pipeline(model_key: str = "sentiment_digikala"):
    """
    Get or load a HuggingFace pipeline for the given model key.
    Returns None if transformers is not installed or model fails to load.
    """
    if model_key in _loaded_pipelines:
        return _loaded_pipelines[model_key]

    if model_key not in PERSIAN_MODELS:
        return None

    try:
        from transformers import pipeline
        info = PERSIAN_MODELS[model_key]
        pipe = pipeline(info["task"], model=info["name"], tokenizer=info["name"])
        _loaded_pipelines[model_key] = pipe
        return pipe
    except Exception:
        return None


def list_available_models() -> Dict[str, str]:
    """Return available model keys and their descriptions"""
    return {k: v["description"] for k, v in PERSIAN_MODELS.items()}
