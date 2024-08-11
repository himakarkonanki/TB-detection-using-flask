
Tuberculosis Detection using cbAM DenseNet 169 and Flask

 Overview

This project leverages a deep learning model based on the cbAM (Convolutional Block Attention Module) DenseNet 169 architecture to detect tuberculosis (TB) from chest X-ray images. A Flask web application is provided to allow users to upload X-ray images and receive predictions on whether the images show signs of tuberculosis.
 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [Results](#results)
- [Dataset](#dataset)
- [Contributing](#contributing)
- [License](#license)

 Features

- Efficient TB Detection: Uses cbAM DenseNet 169 for accurate tuberculosis detection.
- Web Interface: Simple Flask-based interface for image upload and result display.
- Data Augmentation: Enhances model generalization with various augmentation techniques.
- Evaluation Metrics: Provides accuracy, precision, recall, and F1 score for model performance assessment.
Architecture

The project uses cbAM DenseNet 169, a combination of DenseNet's powerful feature extraction with the attention mechanism of cbAM, to focus on the most relevant parts of the image. 

Key Components:
- cbAM Module: Enhances feature maps by applying channel and spatial attention mechanisms.
- DenseNet 169: A deep convolutional neural network architecture that strengthens gradient flow and feature reuse.

Installation

To set up the project on your local machine, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/tuberculosis-detection-cbam-densenet-flask.git
    cd tuberculosis-detection-cbam-densenet-flask
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask application:
    ```bash
    python app.py
    ```

Usage

1. Start the Flask application by running `python app.py`.
2. Open your browser and navigate to `http://127.0.0.1:5000`.
3. Upload a chest X-ray image through the web interface.
4. The model will analyze the image and display the result, indicating whether the image shows signs of tuberculosis.

Model Training

The model was trained using a dataset of chest X-ray images. Data augmentation techniques were applied to enhance the generalization of the model. The model was trained for 60 epochs with the SGD optimizer.

Training History:
- Accuracy and Loss: Visualized using matplotlib to show the training and validation performance over epochs.
- Evaluation: Performance on the test set is evaluated using accuracy, precision, recall, and F1 score.

 Results

The model demonstrated high accuracy and robustness in detecting tuberculosis. Detailed evaluation metrics are provided within the project.

 Dataset

The model was trained and evaluated on a publicly available dataset of chest X-ray images. The dataset contains both TB-positive and TB-negative cases. 

