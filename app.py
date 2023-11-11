import gradio as gr
import torch

from scripts.inference import Infer

demo = gr.Interface(
    fn=Infer().translate,
    inputs=[
        gr.components.Textbox(label="Text"),
    ],
    outputs=["text"],
    examples=[["Building a translation demo with Gradio is so easy!", "eng_Latn", "spa_Latn"]],
    cache_examples=False,
    title="Mozhi",
    description="This demo is a simplified version of the original [NLLB-Translator](https://huggingface.co/spaces/Narrativaai/NLLB-Translator) space"
)

demo.launch()