
import gradio as gr

def run(image, style):
    return "output/demo.mp4"

gr.Interface(
    fn=run,
    inputs=["image", "dropdown"],
    outputs="video",
    title="Image to Video AI"
).launch()
