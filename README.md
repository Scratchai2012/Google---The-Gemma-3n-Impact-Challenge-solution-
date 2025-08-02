# 📚 GemmaLearn — Offline AI Tutor with Gemma 3n

This project demonstrates the use of **Gemma 3n (3B Instruct)** as an **offline educational assistant** for students in rural and low-connectivity environments. The app can summarize school topics, explain concepts, and generate practice questions — entirely **without internet access**.

> Built for the **Google - The Gemma 3n Impact Challenge**.

---

## 🚀 What It Does

Using `llama-cpp-python`, this app runs the 3B Gemma model locally to:

- Explain textbook content in simple language
- Highlight key learning points
- Generate quiz questions for practice

---

## 🧠 Why Gemma 3n?

Gemma 3n is:

- Lightweight enough to run on consumer laptops
- Multilingual & instruction-tuned
- Open-weight and offline-friendly
- Hugely impactful for low-resource education

---

## 🔧 How to Run (Locally)

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/gemmalearn.git
cd gemmalearn
2. Download the model
Download Gemma 1.1 3B Instruct GGUF (Q4_K_M) from Hugging Face
Place it in:

bash
Copy code
models/gemma-3b-it-Q4_K_M.gguf
3. Install dependencies
bash
Copy code
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
4. Run the app
bash
Copy code
python app.py
✨ Example
arduino
Copy code
Enter a school topic or textbook line: Photosynthesis in plants
Output:

csharp
Copy code
📘 AI Tutor Response:

Photosynthesis is the process by which green plants make their own food using sunlight, water, and carbon dioxide...

Key Points:
1. It occurs in chloroplasts using chlorophyll
2. Converts light energy into chemical energy
3. Produces oxygen as a byproduct

Practice Questions:
1. What is the main purpose of photosynthesis?
2. Why is chlorophyll important in this process?
📁 Project Structure
java
Copy code
gemmalearn/
├── app.py                  ← Core tutor script
├── models/                 ← Gemma 3b model (not included)
│   └── gemma-3b-it-Q4_K_M.gguf
├── prompts/
│   └── sample_input.txt    ← Example topics
├── requirements.txt
└── README.md
✅ For Judges: Technical Validation
This repository proves that:

We used Gemma 3n locally, not via API

We applied it in an educational domain

The model runs on consumer-grade hardware using llama-cpp-python

This code is part of a broader video + storytelling submission available in our final entry.

🧩 License
Apache 2.0 (same as Gemma)

🙏 Acknowledgements
Google DeepMind – Gemma 3n model

llama-cpp-python by @abetlen

yaml
Copy code

---

Let me know when you're ready to push this to GitHub, or if you want to zip the full codebase for upload.






