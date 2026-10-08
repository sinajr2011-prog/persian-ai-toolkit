"""
Speech-to-Text module for Persian with Iranian accent support.
Uses OpenAI Whisper (optional) – best open-source option for Persian currently.
"""

from typing import Dict, Any, Optional
import os

_whisper_model = None


def _load_whisper(model_size: str = "base"):
    """Lazy load Whisper model"""
    global _whisper_model
    if _whisper_model is not None:
        return True
    try:
        import whisper
        _whisper_model = whisper.load_model(model_size)
        return True
    except Exception:
        return False


def speech_to_text(
    audio_path: str,
    model_size: str = "base",
    language: str = "fa"
) -> Dict[str, Any]:
    """
    Convert speech to text with Persian (Iranian accent) support.

    Args:
        audio_path: Path to audio file (wav, mp3, m4a, ...)
        model_size: Whisper model size (tiny, base, small, medium, large)
        language: Language code (default 'fa' for Persian)

    Returns:
        Dictionary with transcription and metadata
    """
    if not os.path.exists(audio_path):
        return {
            "text": "",
            "success": False,
            "message": f"Audio file not found: {audio_path}"
        }

    if not _load_whisper(model_size):
        return {
            "text": "",
            "success": False,
            "message": "Whisper is not installed. Run: pip install openai-whisper"
        }

    try:
        result = _whisper_model.transcribe(
            audio_path,
            language=language,
            fp16=False  # better compatibility
        )
        return {
            "text": result.get("text", "").strip(),
            "language": result.get("language", language),
            "success": True,
            "model": f"whisper-{model_size}",
            "segments": len(result.get("segments", []))
        }
    except Exception as e:
        return {
            "text": "",
            "success": False,
            "message": str(e)
        }


def list_supported_formats() -> list:
    """Return list of supported audio formats"""
    return ["wav", "mp3", "m4a", "ogg", "flac", "webm"]
