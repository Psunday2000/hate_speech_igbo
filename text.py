from unidecode import unidecode
import re


def clean_and_remove_special_chars(text):
    # Remove accents and convert non-English characters
    text = unidecode(text)

    # Remove special characters and digits using regex
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    return text


# Example usage
somestring = "Nkịta 123"
cleaned_string = clean_and_remove_special_chars(somestring)
print(cleaned_string)
