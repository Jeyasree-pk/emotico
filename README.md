# MoodDecode: Build Your Own NLP API

## 🚀 Description

MoodDecode is a FastAPI-based project for building NLP APIs that analyze mood, detect crisis, and summarize text using OpenAI's GPT models.

---

## 📚 Endpoints

### 1. Analyze Mood

- **POST `/analyze_mood`**
- **Input:**
  ```json
  { "text": "I feel amazing today!" }
  ```
- **Output:**
  ```json
  { "emotion": "happy" }
  ```

### 2. Detect Crisis

- **POST `/detect_crisis`**
- **Input:**
  ```json
  { "text": "I'm feeling hopeless and might hurt myself" }
  ```
- **Output:**
  ```json
  { "crisis_detected": true }
  ```

### 3. Summarize

- **POST `/summarize`**
- **Input:**
  ```json
  { "text": "Long paragraph here..." }
  ```
- **Output:**
  ```json
  { "summary": "Condensed version of input..." }
  ```

---

## 🛠️ Setup & Run

1. **Install dependencies**  
   `pip install -r requirements.txt`

2. **Set your OpenAI API Key**  
   `export OPENAI_API_KEY=your-api-key`

3. **Run the server**  
   `uvicorn app:app --reload`

4. **(Optional) Expose with Ngrok**  
   `ngrok http 8000`

---

## 🧠 How It Works

- **/analyze_mood:** Returns a single-word emotion detected in the text.
- **/detect_crisis:** Returns `true` if the text indicates a crisis or suicidal intent.
- **/summarize:** Returns a concise summary of the input text.

All endpoints are powered by OpenAI's GPT API via async HTTP calls for speed and reliability.

---

## 🫶 Contribution

- Modular, clean code – easy to extend!
- Add more models/providers in `utils/openai_utils.py` if needed.

---

## 📝 Sample Input/Output

See endpoints section above.