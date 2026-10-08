"""
Simple Web Dashboard for Persian AI Toolkit using Gradio
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import gradio as gr
from persian_ai import (
    analyze_sentiment,
    summarize,
    generate_caption,
    extract_keywords,
    clean_persian_text,
)


def sentiment_ui(text, use_model):
    if not text.strip():
        return "Please enter some text."
    result = analyze_sentiment(text, use_model=use_model)
    return (
        f"**Label:** {result.get('label', 'N/A')}\n\n"
        f"**Score:** {result.get('score', 0)}\n\n"
        f"**Method:** {result.get('method', 'N/A')}\n\n"
        f"**Preview:** {result.get('text_preview', '')}"
    )


def summarize_ui(text, max_sentences):
    if not text.strip():
        return "Please enter some text."
    result = summarize(text, max_sentences=int(max_sentences))
    return result.get("summary", "")


def caption_ui(text):
    if not text.strip():
        return "Please enter some text."
    result = generate_caption(text)
    return result.get("full_post", "")


def keywords_ui(text):
    if not text.strip():
        return "Please enter some text."
    kws = extract_keywords(text)
    return " | ".join(kws) if kws else "No keywords found."


def clean_ui(text):
    if not text.strip():
        return "Please enter some text."
    return clean_persian_text(text)


with gr.Blocks(title="Persian AI Toolkit", theme=gr.themes.Soft()) as demo:
    gr.Markdown(
        """
        # 🇮🇷 Persian AI Toolkit Dashboard
        Open-source AI tools for the Persian language
        """
    )

    with gr.Tab("Sentiment Analysis"):
        with gr.Row():
            sent_input = gr.Textbox(label="Persian Text", lines=4, placeholder="متن خود را اینجا بنویسید...")
        use_model = gr.Checkbox(label="Use HuggingFace model (slower, more accurate)", value=False)
        sent_btn = gr.Button("Analyze", variant="primary")
        sent_output = gr.Markdown()
        sent_btn.click(sentiment_ui, inputs=[sent_input, use_model], outputs=sent_output)

    with gr.Tab("Summarization"):
        sum_input = gr.Textbox(label="Long Persian Text", lines=8)
        max_sent = gr.Slider(1, 8, value=3, step=1, label="Max sentences")
        sum_btn = gr.Button("Summarize", variant="primary")
        sum_output = gr.Textbox(label="Summary", lines=4)
        sum_btn.click(summarize_ui, inputs=[sum_input, max_sent], outputs=sum_output)

    with gr.Tab("Caption Generator"):
        cap_input = gr.Textbox(label="Description / Photo text", lines=3)
        cap_btn = gr.Button("Generate Caption", variant="primary")
        cap_output = gr.Textbox(label="Instagram Post", lines=6)
        cap_btn.click(caption_ui, inputs=cap_input, outputs=cap_output)

    with gr.Tab("Keywords"):
        kw_input = gr.Textbox(label="Text", lines=4)
        kw_btn = gr.Button("Extract Keywords", variant="primary")
        kw_output = gr.Textbox(label="Keywords")
        kw_btn.click(keywords_ui, inputs=kw_input, outputs=kw_output)

    with gr.Tab("Text Cleaner"):
        cl_input = gr.Textbox(label="Messy Text", lines=4)
        cl_btn = gr.Button("Clean", variant="primary")
        cl_output = gr.Textbox(label="Cleaned Text")
        cl_btn.click(clean_ui, inputs=cl_input, outputs=cl_output)

    gr.Markdown("---\nMade with ❤️ by SinaJr | [GitHub](https://github.com/sinajr2011-prog/persian-ai-toolkit)")


if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860, share=False)
