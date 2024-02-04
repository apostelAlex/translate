import gradio as gr
from transformers import pipeline

def translate(input_text):
    model = f"Helsinki-NLP/opus-mt-de-el"
    pipe = pipeline("translation", model=model)
    translation = pipe(input_text)
    return translation[0]['translation_text']


with gr.Blocks() as demo:
    gr.HTML("""<html>
  <head>
    <style>
      h1 {
        text-align: center;
      }
    </style>
  </head>
  <body>
    <h1>Open Translate</h1>
  </body>
</html>""")
    with gr.Row():
        with gr.Column():
            input_textbox = gr.Textbox(lines=5, placeholder="Enter text to translate", label="Input Text")
        with gr.Column():
            translated_textbox = gr.Textbox(lines=5, placeholder="", label="Translated Text")
    btn = gr.Button("Translate")
    btn.click(translate, inputs=[input_textbox], outputs=translated_textbox)
    gr.Examples(["Wie geht es Ihnen heute?", "Das Meer ist heute sehr kalt."],
                inputs=[input_textbox])

if __name__ == "__main__":
    demo.launch()
