import gradio as gr

def greet(name):
    return f"Hello, {name}!"

interface = gr.Interface(fn=greet, inputs="text", outputs="text")
interface.launch(share=True)
