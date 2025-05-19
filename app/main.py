import gradio as gr
from app.gradio_interface import create_interface

if __name__ == "__main__":
    # Launch the Gradio interface
    interface = create_interface()
    interface.launch()

