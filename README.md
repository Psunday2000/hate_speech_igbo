# Igbo-English Hate Speech Detection

A proof-of-concept machine learning system that classifies Igbo-English code-mixed text as hate speech or non-hate speech. Built as an HND final-year project, this is the first labeled dataset and detection baseline published for the Igbo-English language pair, contributing to NLP research for low-resource African languages.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Keras-orange)
![License](https://img.shields.io/badge/License-MIT-green)

## What this project contributes

1. **A labeled Igbo-English code-mixed dataset** (268 examples) built by the author from scratch, the first of its kind publicly available.
2. **A trained binary classifier** (TF-IDF features into a dense neural network) with a working evaluation pipeline.
3. **A desktop GUI application** built with Kivy, so anyone can install and try the classifier without writing code.
4. **All research artifacts published** including the Kaggle notebook and Kaggle dataset, in addition to this repository.

## Why it matters

Most NLP research targets high-resource languages like English. Igbo, spoken by over 40 million people in Nigeria, has very limited NLP resources. Igbo-English code-mixing, which is how most Igbo speakers actually communicate online, has almost no published work at all. This project is a small step toward filling that gap.

## Dataset

**Source:** Built from scratch by the author using two methods:

- An online Google Form distributed to native Igbo speakers to collect common Igbo hate speech terms and expressions
- Igbo-English dictionary websites to source lexical context for non-hate examples

**Size:** 268 labeled examples (153 hate speech, 115 non-hate)

**Design:** The dataset uses a minimal-pair structure. The same Igbo words (for example, animal names like Nkịta, Ezi, Ọgazị) appear in both classes, requiring the model to learn contextual usage rather than relying on a blacklist of words.

**Example non-hate:** "Nkịta, the dog, barks loudly to alert its owner."

**Example hate:** "You act like a Nkịta, always causing trouble."

**Available on Kaggle:** [Igbo Hate Speech Dataset](https://www.kaggle.com/datasets/nwachipraises/igbo-hate-speech-dataset)

## Model

A lightweight binary classifier:

- **Features:** TF-IDF vectorization
- **Architecture:** Sequential neural network with one hidden Dense layer (128 units, ReLU activation) and a Sigmoid output
- **Optimizer:** Adam
- **Loss:** Binary cross-entropy
- **Training:** 10 epochs, batch size 32, 20% validation split

Full training notebook published on Kaggle: [Igbo Hate Speech Detection notebook](https://www.kaggle.com/code/nwachipraises/igbo-hate-speech-detection)

## Results

Evaluated on a held-out test set of 54 examples:

**Overall test accuracy:** 79.6%

**Per-class metrics:**

| Class | Precision | Recall | F1 |
|-------|-----------|--------|-----|
| Non Hate Speech | 1.00 | 0.56 | 0.72 |
| Hate Speech | 0.72 | 1.00 | 0.84 |

The classifier catches 100% of actual hate speech in the test set. It trades off against precision on the non-hate class, which is a reasonable bias for a content moderation baseline but worth flagging honestly.

### Confusion Matrix

![Confusion Matrix](Confusion%20Matrix.png)

### Classification Metrics by Class

![Classification Metrics](Classifcation%20Metrics%20by%20Class.png)

### Training and Validation Curves

![Training Curves](Training%20and%20Validation%20Accuracy%20and%20Loss%20over%20Epochs.png)

## Limitations and next steps

I want to be transparent about where this project sits as engineering:

- **Dataset size is small.** 268 examples is enough for a proof of concept, not production. Expanding to several thousand examples would meaningfully improve generalization.
- **The model overfits.** Training accuracy reaches ~99% while validation plateaus around 75%. Dropout, L2 regularization, or early stopping would help.
- **TF-IDF is a simple baseline.** Word embeddings (fastText, or an Igbo-aware embedding) or a small transformer would likely outperform TF-IDF on code-mixed text.
- **Binary labels only.** Real hate speech moderation needs more granular categories (offensive, hateful, threatening, and so on).
- **Class imbalance handling.** The 153/115 split is mild, but a production system should use class weights or resampling.

A follow-up version of this project would expand the dataset to at least 2,000 examples and compare the TF-IDF baseline against an embedding-based approach.

## Install and run

### Prerequisites

- Python 3.x
- Dependencies in `requirements.txt`

### Setup

```
git clone https://github.com/Psunday2000/hate_speech_igbo.git
cd hate_speech_igbo
pip install -r requirements.txt
```

### Run the GUI

```
python main.py
```

The Kivy-based GUI launches. Enter a message and click Submit to classify it.

### Run the notebook

Open `hate_speech_model.ipynb` in Jupyter to retrain, modify, or experiment with the model.

## Repository contents

- `hate_speech_dataset.csv` — the full labeled dataset
- `hate_speech_model.ipynb` — training notebook with preprocessing, model, and evaluation
- `hspeechmodel.h5` — trained Keras model
- `vectorizer.pkl` — fitted TF-IDF vectorizer
- `main.py` — Kivy GUI application
- `test.py` — standalone inference script
- `convert.py` — utility script
- Visualization images (confusion matrix, training curves, classification metrics, tokenization, vectorization)

## License

Released under the MIT License. See [LICENSE](LICENSE) for details.

## Citation

If you use this dataset or model in research, please cite:

```
Sunday, P. C. (2024). Igbo-English Hate Speech Detection: A Proof-of-Concept 
Binary Classifier for a Low-Resource Language Pair. HND Final Year Project, 
Akanu Ibiam Federal Polytechnic, Unwana.
Available at: https://github.com/Psunday2000/hate_speech_igbo
```

## Author

Built by **Praise Chiedozie Sunday**.

- Portfolio: [praise-chiedozie-sunday.vercel.app](https://praise-chiedozie-sunday.vercel.app)
- LinkedIn: [praise-sunday](https://www.linkedin.com/in/praise-sunday-179a86224)
- GitHub: [@Psunday2000](https://github.com/Psunday2000)

If you find this project useful, a star on the repo is appreciated.
