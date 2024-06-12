import streamlit as st
import pandas as pd
import os

# Function to save questions to CSV
def save_to_csv(questions, language):
    df = pd.DataFrame(questions, columns=['Question'])
    df['Language'] = language

    # Check if CSV file exists
    if not os.path.exists('questions.csv'):
        df.to_csv('questions.csv', index=False)
    else:
        df.to_csv('questions.csv', mode='a', header=False, index=False)

# Main Streamlit app
def main():
    st.title("Question Storage App")

    language = st.radio("Select language:", ('French', 'Arabic'))

    question = st.text_area(f"Enter your question in {language}:")
    if st.button("Submit"):
        if question:
            save_to_csv([question], language.lower())

            st.success(f"Question '{question}' in {language} successfully stored!")

if __name__ == '__main__':
    main()
