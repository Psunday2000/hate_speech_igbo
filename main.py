from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
import numpy as np
from keras.models import load_model
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from unidecode import unidecode
import re


class HateSpeechClassifierApp(App):
    def build(self):
        self.vectorizer = self.load_vectorizer()
        self.model = self.load_model()

        # Input layout
        input_layout = BoxLayout(orientation='vertical', spacing=10)
        self.text_input = TextInput(
            hint_text='Enter text here', multiline=False)
        submit_button = Button(text='Submit', on_press=self.process_text)
        input_layout.add_widget(self.text_input)
        input_layout.add_widget(submit_button)

        # Result layout
        self.result_layout = GridLayout(cols=2, spacing=10)
        self.result_label = Label(text='', halign='center', valign='middle')
        self.result_image = Image(source='', size=(100, 100))
        self.result_layout.add_widget(self.result_label)
        self.result_layout.add_widget(self.result_image)

        # Main layout
        main_layout = BoxLayout(orientation='vertical', spacing=10)
        main_layout.add_widget(input_layout)
        main_layout.add_widget(self.result_layout)

        return main_layout

    def load_vectorizer(self):
        with open('vectorizer.pkl', 'rb') as file:
            vectorizer = pickle.load(file)
        return vectorizer

    def load_model(self):
        model = load_model('hspeechmodel.h5')
        return model

    def process_text(self, instance):
        input_text = self.text_input.text
        cleaned_text = self.clean_and_preprocess(input_text)
        vectorized_text = self.vectorizer.transform([cleaned_text]).toarray()
        prediction = self.model.predict(vectorized_text)
        predicted_class = np.round(prediction)

        if predicted_class == 1:
            self.show_result('Positive', 'positive_image.png')
        else:
            self.show_result('Negative', 'negative_image.png')

    def clean_and_preprocess(self, text):
        text = unidecode(text)
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        tokens = word_tokenize(text)
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(word.lower()) for word in tokens if word.lower(
        ) not in stopwords.words('english')]
        return ' '.join(tokens)

    def show_result(self, result_text, image_source):
        self.result_label.text = result_text
        self.result_image.source = image_source


if __name__ == '__main__':
    HateSpeechClassifierApp().run()
