import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from keras.models import load_model
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from unidecode import unidecode
import pickle
import re

# Load the dataset
dataset = pd.read_csv('hate_speech_dataset.csv')

# Load the trained model
model = load_model('hspeechmodel.h5')

# Load the vectorizer used during training
with open('vectorizer.pkl', 'rb') as file:
    vectorizer = pickle.load(file)

# Function for cleaning and preprocessing input text


def clean_and_preprocess(text):
    # Remove accents and convert non-English characters
    text = unidecode(text)

    # Remove special characters and digits using regex
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # Tokenize the text
    tokens = word_tokenize(text)

    # Remove stopwords and lemmatize
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word.lower()) for word in tokens if word.lower(
    ) not in stopwords.words('english')]

    return ' '.join(tokens)


# Get input text from the user
input_text = input("Enter the text you want to classify: ")

# Preprocess the input text
cleaned_text = clean_and_preprocess(input_text)

# Vectorize the processed text using the loaded vectorizer
vectorized_text = vectorizer.transform([cleaned_text]).toarray()

# Make predictions
prediction = model.predict(vectorized_text)
predicted_class = np.round(prediction)

# Display the prediction result
if predicted_class == 1:
    print("The input text is classified as Positive.")
else:
    print("The input text is classified as Negative.")
