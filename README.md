# Hate Speech Detection System

## Overview

This project implements a Hate Speech Detection System using natural language processing (NLP) and machine learning techniques. The system is capable of classifying text as hate speech or non-hate speech. It includes a trained model, a TF-IDF vectorizer, and a graphical user interface (GUI) built using Kivy.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the GUI](#running-the-gui)
- [Contributing](#contributing)
- [License](#license)

## Features

- Hate speech classification using a trained model.
- User-friendly GUI for easy interaction.
- Preprocessing pipeline for cleaning and vectorizing text.
- Word clouds and visualizations for better understanding.

## Getting Started

### Prerequisites

- Python 3.x
- Install required Python packages:
  ```bash
  pip install -r requirements.txt
  ```

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/psunday2000/hate_speech_igbo.git
   cd hate_speech_igbo
   ```
2. Download the [hate_speech_dataset.csv](#) file and place it in the project root.

## Usage

### Running the GUI

1. Open a terminal in the project directory.
2. Run the following command:
   ```bash
   python main.py
   ```
3. The GUI will launch. Enter the text you want to classify, and click the "Submit" button.

## Contributing

Contributions are welcome! Please follow the [Contribution Guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).
