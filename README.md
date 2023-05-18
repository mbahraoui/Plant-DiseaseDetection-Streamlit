# Plant Disease Detection - Streamlit

This repository contains the source code and trained models for the Plant Disease Detection application using Convolutional Neural Networks (CNN). The application is deployed and can be accessed at [https://plantdiseasedetection.streamlit.app/](https://plantdiseasedetection.streamlit.app/).

## About

The Plant Disease Detection application utilizes deep learning techniques, specifically CNNs, to identify diseases in plant images. By analyzing the visual features of plant images, the application can accurately classify and detect various diseases or health conditions that affect plants. This can help farmers and plant enthusiasts identify and address plant diseases promptly, leading to improved crop yield and healthier plants.

The application provides a user-friendly web interface where users can upload plant images for analysis. The image is then processed using a trained CNN model, which predicts the presence of any diseases or health issues. The results are displayed to the user, indicating the detected disease.

## How to Use

To use the Plant Disease Detection application, follow these steps:

1. Access the application at [https://plantdiseasedetection.streamlit.app/](https://plantdiseasedetection.streamlit.app/).
2. The landing page will guide you through the process.
3. Click on the "Upload Image" button to select an image from your device.
4. Wait for the image to be processed and analyzed by the CNN model.
5. Once the analysis is complete, the application will display the detected disease or health condition.

## Training

The CNN model used in the Plant Disease Detection application was trained using a labeled dataset of plant images. The training process was performed using Google Colaboratory.

To access the training notebook and reproduce the training process, follow this link: [https://colab.research.google.com/drive/166xQ-6AybNGNeDIcF3mbh2LI0Y3iFeAc](https://colab.research.google.com/drive/166xQ-6AybNGNeDIcF3mbh2LI0Y3iFeAc).

The notebook provides detailed steps on data preprocessing, model architecture, hyperparameter tuning, and training. You can modify the notebook as needed to experiment with different configurations or extend the capabilities of the model.

## Requirements

To run the Plant Disease Detection application locally, make sure you have the following dependencies installed:

- Python (version 3.6 or higher)
- pip (Python package installer)

To install the required Python libraries, navigate to the repository root directory and run the following command:

```bash
pip install -r requirements.txt
```

## Run Locally

To run the Plant Disease Detection application on your local machine, follow these steps:

1. Clone this repository:

   ```bash
   git clone https://github.com/mbahraoui/Plant-DiseaseDetection-Streamlit.git
   ```

2. Navigate to the repository directory:

   ```bash
   cd Plant-DiseaseDetection-Streamlit
   ```

3. Install the required Python libraries (if not already installed):

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit application:

   ```bash
   streamlit run app.py
   ```

5. Open your web browser and access the application at [http://localhost:8501](http://localhost:8501).
