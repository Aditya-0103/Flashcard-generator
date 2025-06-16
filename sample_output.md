# 📋 Sample Execution – Flashcard Generator

This file demonstrates how the Flashcard Generator processes real-world educational input into concise Q&A flashcards using a Large Language Model (Gemini 1.5 in this case).

---

## 🧾 Sample Input

**Topic:** The Water Cycle  
**Input Source:** Textbook Excerpt (Environmental Science)


The water cycle, also known as the hydrological cycle, describes the continuous movement of water on, above, and below the surface of the Earth. This cycle includes processes such as evaporation, condensation, precipitation, infiltration, and runoff. The sun drives the entire cycle by providing energy for evaporation. Water vapor condenses into clouds, which eventually release precipitation. Some of the water seeps into the ground (infiltration), while the rest flows into rivers and oceans (runoff), where the process repeats.

---

## ✅ Generated Flashcards (via Gemini 1.5)

1. **Q:** What is the water cycle?  
   **A:** It is the continuous movement of water on, above, and below the Earth's surface.

2. **Q:** What are the key processes in the water cycle?  
   **A:** Evaporation, condensation, precipitation, infiltration, and runoff.

3. **Q:** What drives the water cycle?  
   **A:** The sun provides energy for evaporation, driving the cycle.

4. **Q:** What happens during evaporation?  
   **A:** Water turns into vapor and rises into the atmosphere.

5. **Q:** What is condensation?  
   **A:** It's the process where water vapor cools and turns into clouds.

6. **Q:** How does precipitation occur?  
   **A:** Clouds release water as rain, snow, sleet, or hail.

7. **Q:** What is infiltration?  
   **A:** It is the process where water seeps into the ground.

8. **Q:** What is runoff?  
   **A:** Water that flows over the land into rivers, lakes, or oceans.

9. **Q:** Where does water go after precipitation?  
   **A:** Some infiltrates the ground; the rest becomes runoff.

10. **Q:** Why is the water cycle important?  
    **A:** It maintains Earth's water balance and supports all forms of life.

---

## 🛠️ Technical Details

- **Model Used:** Gemini 1.5 via `google.generativeai`
- **Prompt Strategy:** Structured format with clear instruction for Q&A output
- **UI:** Streamlit Web Interface

---

## 📌 Notes

- Flashcards are clean, factual, and suitable for academic review.
- The tool is scalable for longer inputs (e.g., full chapters or notes).
- Easy to extend for subject tagging, difficulty levels, or exports.
