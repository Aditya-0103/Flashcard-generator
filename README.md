# Flashcard Generator

This project was developed as part of a technical evaluation for **ShelfEx**. The goal was to build an intelligent **Flashcard Generator** that uses an LLM (Large Language Model) to summarize input text into 10 concise Q\&A flashcards. It showcases proficiency in Python, LLM integration, prompt engineering, and UI development using Streamlit.

---

## ✅ Objectives

* 📄 Input: Raw textual content (academic or general)
* ⚙️ Process: Use Gemini 1.5 LLM to extract key concepts as flashcards
* 📋 Output: 10 Q\&A pairs rendered interactively
* 🎛️ UI: Web app interface for easy testing and interaction

---

## 🛠️ Tech Stack

* **Frontend/UI**: Streamlit
* **Backend/Logic**: Python
* **AI Model**: Google Gemini 1.5 via GenerativeAI SDK

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Aditya-0103/Flashcard-generator.git
cd Flashcard-generator
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure API Key

Get your [Gemini API Key](https://ai.google.dev/) and add it to `app.py`:

```python
genai.configure(api_key="YOUR_API_KEY")
```

---

## ▶️ Running the Application

```bash
streamlit run app.py
```

Then open your browser and navigate to:
`http://localhost:8501`

---

## 🧪 How It Works

1. Paste any paragraph or topic content into the input box.
2. The system sends the prompt to Gemini 1.5.
3. The model returns structured flashcards.
4. Results are parsed and displayed below.

---

## 📋 Sample Output

**Input Text:**

> "The water cycle describes the continuous movement of water on, above and below the surface of the Earth..."

**Generated Flashcards:**

1. **Q:** What is the water cycle?
   **A:** A continuous movement of water on, above, and below Earth’s surface.

2. **Q:** What are the stages of the water cycle?
   **A:** Evaporation, condensation, precipitation, and collection.

...up to 10 cards.
![image](https://github.com/user-attachments/assets/4f2a86ed-e596-4ad8-8a4c-ae580ab4be4c)

---

## 📂 File Structure

```
Flashcard-generator/
├── README.md             # Project documentation
├── app.py                # Main Streamlit app logic
├── file_parser.py        # Function to parse LLM response
├── flashcard_gen.        # Function to parse LLM response
├── requirements.text
├── sample_output.md      # Sample output
└── utils.py              # Function to parse LLM response    
```

---

## 💡 Highlights

* Minimal latency in API response
* Smart prompt format ensures consistent flashcard style
* Easily extensible for Anki export, PDF upload, or multi-language support

---

## 🔄 Future Enhancements (If Extended)

* PDF/Text file ingestion
* CSV export for flashcards
* Support for additional LLM providers (OpenAI, Claude)
* Theme customization and dark mode

---

## 👨‍💻 Author

**Aditya Singh**
B.Tech CSE | AI/ML & Web Dev Enthusiast
[Portfolio](https://aditya-0103.github.io/Portfolio/) | [GitHub](https://github.com/Aditya-0103)

---

## 📝 Disclaimer

This project was submitted solely for the purpose of **technical skill evaluation** by **ShelfEx**.

---
