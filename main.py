from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.text import LabelBase
import numpy as np
from keras.models import load_model
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from unidecode import unidecode
import re
import pickle


class HateSpeechClassifierApp(App):
    def build(self):
        self.register_custom_font()

        # Set the app title
        self.title = 'Hate Speech Detection System'

        # Load the trained model
        self.model = load_model('hspeechmodel.h5')

        # Load the vectorizer used during training
        with open('vectorizer.pkl', 'rb') as handle:
            self.vectorizer = pickle.load(handle)

        # Create widgets
        # Input layout
        input_layout = BoxLayout(orientation='vertical', spacing=10)
        self.text_input = TextInput(
            hint_text='Enter text here', multiline=False, font_name='MontserratMedium')
        submit_button = Button(
            text='Submit', on_press=self.classify_text, font_name='MontserratMedium')
        input_layout.add_widget(self.text_input)
        input_layout.add_widget(submit_button)

        # Result layout
        self.result_layout = GridLayout(cols=2, spacing=10)
        self.result_label = Label(
            text='', halign='center', valign='middle', font_name='MontserratMedium')
        self.result_image = Image(source='', size=(100, 100))
        self.result_layout.add_widget(self.result_label)
        self.result_layout.add_widget(self.result_image)

        # Main layout
        main_layout = BoxLayout(orientation='vertical', spacing=10)
        main_layout.add_widget(input_layout)
        main_layout.add_widget(self.result_layout)

        return main_layout

    def register_custom_font(self):
        # Register Montserrat-Medium.ttf
        LabelBase.register(name='MontserratMedium',
                           fn_regular='Montserrat-Medium.ttf')

    def classify_text(self, instance):
        # Get input text from the user
        input_text = self.text_input.text.strip()

        # Check if the input text is empty
        if not input_text:
            self.show_result('Invalid text, enter a text',
                             'positive_image.png')
            return
        # Preprocess the input text
        cleaned_text = self.clean_and_preprocess(input_text)

        if any(word not in self.vectorizer.vocabulary_ for word in cleaned_text.split()):
            self.show_result('Input text is out of context.',
                             'positive_image.png')
            return

        # Vectorize the processed text using the same vectorizer
        vectorized_text = self.vectorizer.transform([cleaned_text]).toarray()

        # Make predictions
        prediction = self.model.predict(vectorized_text)
        predicted_class = np.round(prediction)

        # Display the prediction result
        if predicted_class == 1:
            self.show_result('Hate Speech', 'positive_image.png')
        else:
            self.show_result('Non Hate Speech', 'negative_image.png')

    def clean_and_preprocess(self, text):
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

    def show_result(self, result_text, image_source):
        self.result_label.text = result_text
        self.result_image.source = image_source


if __name__ == '__main__':
    HateSpeechClassifierApp().run()
