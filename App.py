from models.model_config import load_model
from ui.gradio_ui import launch_ui

if __name__ == "__main__":
    llm = load_model()
    launch_ui(llm)
