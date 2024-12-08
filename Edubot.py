import os
import json
import datetime
import csv
import nltk
import ssl
import streamlit as st
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


ssl._create_default_https_context = ssl._create_unverified_context
nltk.download('punkt')

file_path = os.path.abspath("./intents.json")
with open(file_path, "r") as file:
    intents = json.load(file)


vectorizer = TfidfVectorizer(ngram_range=(1, 4))
clf = LogisticRegression(random_state=0, max_iter=10000)


tags = []
patterns = []
for intent in intents["intents"]:
    for pattern in intent['patterns']:
        tags.append(intent['tag'])
        patterns.append(pattern)


x = vectorizer.fit_transform(patterns)
y = tags
clf.fit(x, y)


def chatbot(input_text):
    input_text = vectorizer.transform([input_text])
    tag = clf.predict(input_text)[0]
    for intent in intents["intents"]:
        if intent['tag'] == tag:
            response = random.choice(intent['responses'])
            return response


counter = 0


def main():
    global counter
    st.title("Edubot - Your Educational Assistant 🤖")


    menu = ["Home", "Conversation History", "About"]
    choice = st.sidebar.selectbox("Menu", menu)


    if choice == "Home":
        st.write("Welcome to Edubot! Ask me any Educational questions, and I'll do my best to assist you.")

        if not os.path.exists('chat_log.csv'):
            with open('chat_log.csv', 'w', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(['User Input', 'Chatbot Response', 'Timestamp'])

        counter += 1
        user_input = st.text_input("You:", key=f"user_input_{counter}")

        if user_input:
            
            response = chatbot(user_input)
            st.text_area("Edubot:", value=response, height=120, max_chars=None, key=f"chatbot_response_{counter}")

            
            timestamp = datetime.datetime.now().strftime(f"%Y-%m-%d %H:%M:%S")
            with open('chat_log.csv', 'a', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow([user_input, response, timestamp])

            
            if response.lower() in ['goodbye', 'bye']:
                st.write("Thank you for chatting with Edubot! Have a Bright Future!")
                st.stop()

    
    elif choice == "Conversation History":
        st.header("Conversation History")
        if os.path.exists('chat_log.csv'):
            with open('chat_log.csv', 'r', encoding='utf-8') as csvfile:
                csv_reader = csv.reader(csvfile)
                next(csv_reader)
                for row in csv_reader:
                    st.text(f"User: {row[0]}")
                    st.text(f"Edubot: {row[1]}")
                    st.text(f"Timestamp: {row[2]}")
                    st.markdown("---")
        else:
            st.write("No conversation history found.")

    
    elif choice == "About":
        st.subheader("About Edubot")
        st.write("EduBot is a Educational chatbot designed to provide quick responses to common education related queries.")
        st.write("It uses Natural Language Processing (NLP) and Logistic Regression to understand user queries and generate appropriate responses.")
        st.subheader("Features:")
        st.write("- Intent-based response generation.")
        st.write("- Logs conversations for review.")
        st.write("- User-friendly interface built with Streamlit.")

if __name__ == '__main__':
    main()