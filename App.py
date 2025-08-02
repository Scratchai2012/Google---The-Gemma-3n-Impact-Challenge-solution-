# app.py
from llama_cpp import Llama

# Path to the Gemma 3b 4-bit GGUF model (you must download separately)
MODEL_PATH = "models/gemma-3b-it-Q4_K_M.gguf"

# Initialize the model (modify n_ctx depending on memory)
llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=2048,
    n_threads=6,
    use_mlock=True  # Optional: locks model in memory to speed up inference
)

# Prompt template for educational use
TUTOR_PROMPT = """
You are an offline AI tutor for students aged 12–16. Your job is to help explain school topics clearly, in simple language, and generate practice questions. Be concise and educational.

Student's topic:
"{topic}"

Your output should include:
1. A short explanation
2. 3 important points
3. 2 practice questions
"""

def run_tutor(topic: str):
    prompt = TUTOR_PROMPT.format(topic=topic)
    output = llm(prompt, max_tokens=512, temperature=0.7, stop=["</s>"])
    print("\n📘 AI Tutor Response:\n")
    print(output["choices"][0]["text"].strip())

if __name__ == "__main__":
    print("🧠 Welcome to GemmaLearn (Offline Tutor)\n")
    topic = input("Enter a school topic or textbook line: ")
    run_tutor(topic)
