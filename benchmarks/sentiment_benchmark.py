"""
Simple evaluation benchmark for Sentiment Analysis
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from persian_ai import analyze_sentiment

# Small gold-standard test set (label: positive / negative / neutral)
TEST_CASES = [
    ("این محصول عالیه و واقعاً دوست داشتم", "positive"),
    ("خیلی ضعیف و افتضاح بود، پشیمون شدم", "negative"),
    ("نه خوب بود نه بد، معمولی بود", "neutral"),
    ("عاشق این اپلیکیشن شدم، محشره!", "positive"),
    ("اصلاً بدرد نخور و بیارزش بود", "negative"),
    ("ممنون از زحماتتون، عالی کار کردید", "positive"),
    ("ناراحت شدم از این رفتار", "negative"),
    ("فیلم خوبی بود", "positive"),
    ("افتضاح مطلق", "negative"),
    ("نظری ندارم", "neutral"),
]


def run_benchmark(use_model: bool = False):
    correct = 0
    total = len(TEST_CASES)
    results = []

    for text, expected in TEST_CASES:
        pred = analyze_sentiment(text, use_model=use_model)
        label = pred.get("label", "neutral")
        is_correct = label == expected
        if is_correct:
            correct += 1
        results.append({
            "text": text[:40] + "...",
            "expected": expected,
            "predicted": label,
            "score": pred.get("score"),
            "correct": is_correct
        })

    accuracy = correct / total
    print("=" * 60)
    print(f"Sentiment Benchmark (use_model={use_model})")
    print(f"Accuracy: {accuracy:.2%}  ({correct}/{total})")
    print("=" * 60)
    for r in results:
        status = "✅" if r["correct"] else "❌"
        print(f"{status} [{r['expected']} → {r['predicted']}] {r['text']}")
    print("=" * 60)
    return accuracy


if __name__ == "__main__":
    print("\n>>> Rule-based model:")
    run_benchmark(use_model=False)

    print("\n>>> Trying HuggingFace model (if available):")
    try:
        run_benchmark(use_model=True)
    except Exception as e:
        print(f"HF model not available: {e}")
