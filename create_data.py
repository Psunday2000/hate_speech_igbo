from faker import Faker
import random
import pandas as pd

fake = Faker('en_US')  # Using English locale for Faker, but replacing some words with Igbo

# Igbo animal names and their English meanings
animal_names = {
    'Edi Ụra/Edi': 'African Civet',
    'Ele': 'Antelope',
    'Ụsụ': 'Bat',
    'aṅụ': 'Bee',
    'Chinchi': 'Bed bug',
    'ebe': 'Beetle',
    'Nnụnụ': 'Bird',
    'Agbịsị': 'Black ant',
    'Eke ọgba': 'Boa constrictor',
    'Erembụbara/Ilokolo ịbụba/Ukukolo bụba': 'Butterfly',
    'Ịnyịnya ibu': 'Camel',
    'Nwamba/Nwologbo': 'Cat',
    'Eruru': 'Caterpillar',
    'Agbakụrụ nwoke, ya ọ bụrụ nwanyị': 'Centipede',
    'Ogwumagala/Ugwumagana/Oyimagana': 'Chameleon',
    'Ọkụkọ': 'Chicken',
    'Adaka': 'Chimpanzee',
    'Okeọkpa': 'Cock',
    'Ọchịcha/Ụchịcha': 'Cockroach',
    'Okporoko/Okpoloko': 'Cod fish',
    'Ehi/Efi': 'Cow',
    'Ịsha': 'Crayfish',
    'Nshịkọ': 'Crab',
    'Mbụzụ/Abụzụ': 'Cricket',
    'Agụ iyi': 'Crocodile',
    'Mgbada': 'Deer',
    'Nkịta': 'Dog',
    'Jakị': 'Donkey',
    'Ndo': 'Dove',
    'Tatambeneke': 'Dragon fly',
    'Ọbọgwụ': 'Duck',
    'Idide': 'Earthworm',
    'Ugo': 'Eagle',
    'Ebi Iyi': 'Eel',
    'Chekeleke': 'Egret',
    'Enyi': 'Elephant',
    'Azụ': 'Fish',
    'Ijiji': 'Fly',
    'Nnanwuruede/Nyanwuruede': 'Fox',
    'Mbara/Mbala/Akịrị': 'Frog',
    'Echi eteka': 'Gaboon viper',
    'Ikiri/Ikili': 'Galago/Bush baby',
    'Ewu': 'Goat',
    'Ọkwa': 'Goose /Bush fowl',
    'Ọzọdimgba': 'Gorilla',
    'Nchi': 'Grasscutter',
    'Ụkpara/Ụkpana': 'Grasshopper',
    'Oke bekee': 'Guinea pig',
    'Ọgazị': 'Guinea fowl',
    'Egbe': 'Hawk',
    'Nnekwu': 'Hen',
    'Enyi mmiri': 'Hippopotamus',
    'Ezi ọhịa/Ezi ọfịa': 'Hog',
    'Ịnyịnya': 'Horse',
    'Nkịta ọhịa': 'Hyena',
    'Ngwere aghụ/Ngwele aghụ': 'Iguana',
    'Nkwọ': 'Kite',
    'Agụ': 'Leopard',
    'Ngwere': 'Lizard',
    'Ọdụm': 'Lion',
    'Igurube': 'Locust',
    'Ikpuru/Ikpulu': 'Maggot',
    'Esu': 'Millipede',
    'Enwe': 'Monkey',
    'Anwụ nta': 'Mosquito',
    'Enyi nnụnụ': 'Ostrich',
    'Ikwikwi/Iyi Ochi': 'Owl',
    'Icheoku': 'Parrot',
    'Ịsam': 'Periwinkle',
    'Ezi': 'Pig',
    'Nduru': 'Pigeon',
    'Ebi ogwu': 'Porcupine',
    'Okongono/Okongolo/Oti ọkpọ': 'Praying Mantis',
    'Eke': 'Python',
    'Ewi': 'Rabbit',
    'Ebule/ebune': 'Ram',
    'Oke': 'Rat',
    'Akpị': 'Scorpion',
    'Atụrụ': 'Sheep',
    'Nkapị/Nkakwụ': 'Shrew',
    'Eju/Ejula/Ejune': 'Snail',
    'Agwọ': 'Snake',
    'Ududo': 'Spider',
    'Ọsa': 'Squirrel',
    'Okpoko': 'Stork',
    'Eneke ntị oba': 'Swallow',
    'Agụ': 'Tiger',
    'Azụ asa': 'Tilapia',
    'Awọ': 'Toad',
    'Mbe/Nnabe': 'Tortoise',
    'Torotoro': 'Turkey',
    'Mbe mmiri/ Mbe mmili': 'Turtle',
    'Ajụanị/Ajụala': 'Viper',
    'Udele': 'Vulture',
    'Nchịkị/ Agụụlọ': 'Wall gecko',
    'Ebu': 'Wasp',
    'Nnụnụ ọka/Egule': 'Weaver bird',
    'Ahụhụ ọcha/Arụrụ ọcha': 'White Ant',
    'Agụ owulu': 'Wolf',
    'Ọtụrụ kpọkpọ': 'Wood pecker',
    'Ọkpọ': 'Worm',
}

# Function to generate a sentence with a random Igbo animal name
def generate_sentence():
    animal_name = random.choice(list(animal_names.keys()))
    sentence = fake.sentence()  # Generate a random English sentence
    # Replace a word in the sentence with the Igbo animal name
    sentence_with_igbo = sentence.replace(fake.word(), animal_name)
    return sentence_with_igbo

# Generate the dataset
num_non_hate = 500
num_hate = 1500

non_hate_samples = [generate_sentence() for _ in range(num_non_hate)]
hate_samples = [generate_sentence() for _ in range(num_hate)]

# Create a DataFrame
df = pd.DataFrame({'Text': non_hate_samples + hate_samples, 'Label': [0] * num_non_hate + [1] * num_hate})

# Shuffle the DataFrame
df = df.sample(frac=1).reset_index(drop=True)

# Save the dataset to a CSV file
df.to_csv('hate_speech_dataset.csv', index=False)
