import random
# import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pyjokes

def load_data(file_paths):

    questions = []
    answers = []

    for data_filepath in file_paths:
        with open(data_filepath, 'r') as file:
            lines = file.readlines()

        i = 0
        while i < len(lines):
            if lines[i].startswith('Q: ') and (i + 1) < len(lines) and lines[i + 1].startswith('A: '):
                question_text = lines[i].strip().replace('Q: ', '')
                answer_text = lines[i + 1].strip().replace('A: ', '')
                questions.append(question_text)
                answers.append(answer_text)
                i += 2  # Move to the next question
            else:
                i += 1  # Skip invalid lines and move to the next line

    return questions, answers

def generate_answer(question, data_file_paths):
    questions, answers = load_data(data_file_paths)

    # Preprocess the data and the input question
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(questions)
    question_vector = vectorizer.transform([question])

    # Calculate cosine similarities between the input question and all questions in the dataset
    similarities = cosine_similarity(X, question_vector)

    # Find the most similar question
    most_similar_index = similarities.argmax()
    max_similarity = similarities[most_similar_index]

    # You can set a threshold for similarity to determine if the answer is relevant
    similarity_threshold = 0.1  # Adjust as needed
    if max_similarity < similarity_threshold:
        return "I'm sorry, I couldn't find a relevant answer to your question."

    answer = answers[most_similar_index]
    return answer

def chatbot_response(query, data_file_paths):

    if "hello" in query or "hii" in query or "hey" in query:
        responses = [
            "Hii", "Hello", "Hello, How are you", "Hello Dear, how can I help you.",
            "Hello Dear", "Hey, I was really waiting for your presence",
            "Hello, Nice to meet you", "Hello Dear, How Are You"
        ]
        return random.choice(responses)

    elif "how are you" in query or "are you fine" in query:
        responses = [
            "I am fine", "I am fine, how are you dear", "Fine, dear!"
        ]
        return random.choice(responses)
    
    elif 'joke' in query:
        return pyjokes.get_joke()

    elif "see you later" in query or "goodbye" in query or "bye" in query or "good night" in query \
            or "sleep" in query or "stop" in query or "not now" in query or "break" in query:
        responses = [
            "Good Bye!", "Bye Bye!", "See You Later", "Thanks for using me, have a good day...",
            "See You", "See you again..."
        ]
        return random.choice(responses)

    else:
        return generate_answer(query, data_file_paths)

# Example usage
data_file_paths = [
    
    'eralink\\BrainData\\physics-a-level-definitions.txt',
    'eralink\\BrainData\\qa_data.txt',
    'eralink\\BrainData\\gk_que.txt',
    'eralink\\BrainData\\interesting.txt',
    # 'additional-file.txt',
    # Add more file paths here
]

# Comment below code

# while True:
#     user_query = input("You: ")
#     response = chatbot_response(user_query, data_file_paths)
#     print("Bot:", response)
