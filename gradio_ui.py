import gradio as gr

TUTOR_PROMPT = """
You are an offline AI tutor for students aged 12–16. Explain the topic simply and generate 3 key points and 2 practice questions.

Student's topic:
"{topic}"

Your output should include:
1. A short explanation
2. 3 important points
3. 2 practice questions
"""

def launch_ui(llm):
    def tutor_response(topic):
        prompt = TUTOR_PROMPT.format(topic=topic)
        output = llm(prompt, max_tokens=512, temperature=0.7, stop=["</s>"])
        return output["choices"][0]["text"].strip()

    demo = gr.Interface(
        fn=tutor_response,
        inputs=gr.Textbox(label="Enter Topic", placeholder="e.g. Photosynthesis"),
        outputs=gr.Textbox(label="AI Tutor Response"),
        title="GemmaLearn: Offline AI Tutor"
    )

    demo.launch()
      
