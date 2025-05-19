import gradio as gr
from app.prompt_manager import generate_response

def chat_with_ai(user_input, chat_history):
    response = generate_response(user_input, chat_history)
    chat_history.append((user_input, response))
    return chat_history, chat_history

def create_interface():
    with gr.Blocks() as interface:
        gr.Markdown("# CIAO-AI: Your Italian History and Language Assistant")
        chatbot = gr.Chatbot()
        user_input = gr.Textbox(label="Ask a question:")
        submit_button = gr.Button("Submit")
        clear_button = gr.Button("Clear Chat")

        chat_history = gr.State([])

        submit_button.click(chat_with_ai, inputs=[user_input, chat_history], outputs=[chatbot, chat_history])
        clear_button.click(lambda: ([], []), inputs=[], outputs=[chatbot, chat_history])

    return interface

