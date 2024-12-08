# Implementation-of-ChatBot-using-NLP

# Edubot - Your Educational Assistant 🤖

EduBot is an AI-driven educational assistant that combines Natural Language Processing (NLP), PyTorch, Python, and Streamlit to create an interactive learning platform. It uses NLP to understand student queries and generate accurate, personalized responses while leveraging PyTorch for deep learning-based recommendations. Streamlit powers the user-friendly interface, making EduBot accessible and engaging for students across various subjects.

---

## Features
<ol>
EduBot adapts to individual learning needs, offering tailored explanations, resources, and quizzes to match each student's progress and understanding.
It uses advanced NLP to understand and interpret student queries, providing contextually accurate answers in natural language.
Powered by Streamlit, EduBot offers an intuitive and easy-to-use interface, allowing students to interact with the bot seamlessly across various devices.
Leveraging PyTorch, EduBot suggests relevant learning materials, exercises, and topics based on student performance and preferences, enhancing the learning experience.
</ol>

---

## How It Works

1. **Ask Questions:**  
   Users type their health-related queries into the input box on the "Home" screen.

2. **Receive Responses:**  
   MediBot analyzes the input and provides a text-based response.

3. **Review History:**  
   Users can review the conversation history in the "Conversation History" section, which displays all previous interactions.

4. **Learn More About MediBot:**  
   The "About" section provides an overview of the chatbot’s purpose and features.

---

## Technologies Used

- **Programming Language:** Python
- **Framework:** Streamlit
- **NLP Techniques:** Intent recognition using Logistic Regression
- **Libraries:**  
  - `streamlit`: For building the interactive user interface  
  - `csv`: For logging and reading conversation history  
  - `datetime`: For timestamping user interactions

---

## Installation and Setup

Follow these steps to set up and run the MediBot project on your local machine:

### 1. Clone the Repository  
   ```bash
   git <repository-url>
   cd <repository-directory>
   ```

### 2. Create a Virtual Environment (Optional)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Required Packages
```bash
pip install -r requirements.txt
```

### 4. Download NLTK Data
```python
import nltk
nltk.download('punkt')
```

---

## Usage
To run the chatbot application, execute the following command:
```bash
python -m streamlit run MediBot.py
```

Once the application is running, you can interact with the chatbot through the web interface. Type your message in the input box and press Enter to see the chatbot's response.

---

## Intents Data
The chatbot's behavior is defined by the `intents.json` file, which contains various tags, patterns, and responses. You can modify this file to add new intents or change existing ones for your cahtbot.

---

## Conversation History
The chatbot saves the conversation history in a CSV file (`chat_log.csv`). You can view past interactions by selecting the "Conversation History" option in the sidebar.

---

## Contributing
Contributions to this project are welcome! If you have suggestions for improvements or features, feel free to open an issue or submit a pull request.

---

## Acknowledgments
- **NLTK** for natural language processing.
- **Scikit-learn** for machine learning algorithms.
- **Streamlit** for building the web interface.

---

Replace `<repository-url>` and `<repository-directory>` with the actual URL of repository and the name of the directory where the project is located. 

---

### HAPPY CODING AND LEARNING 😊
