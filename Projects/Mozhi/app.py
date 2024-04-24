import gradio as gr
from scripts.inference import Infer
import yaml

if __name__ == '__main__':
    with open('config.yaml', 'r') as f:
        x = yaml.safe_load(f)
        config = x['infer']
        model_config = x['model']['parameters']

    model = Infer(config, model_config)

    demo = gr.Interface(
        fn=model.translate,
        inputs=[
            gr.components.Textbox(label="Text"),
        ],
        outputs=["text"],
        examples=[["Building a translation demo with Gradio is so easy!", "eng_Latn", "spa_Latn"]],
        cache_examples=False,
        title="Mozhi",
        description="English to Tamil Translator"
    )

    demo.launch()