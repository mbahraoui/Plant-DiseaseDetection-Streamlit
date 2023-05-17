from keras.models import load_model
import numpy as np
from keras.utils import load_img,img_to_array
import streamlit as st

# Load the trained model
model = load_model('./plant_disease.h5')

# Define the function to make predictions
def predict(image):
    # Get the image URL from the request
    image_path = image

    # Use the Keras function `load_img()` to load the image and resize it to the
    # size expected by the model

    image = load_img(image_path, target_size=(64, 64))

    # Convert the image to a Numpy array
    image_array = img_to_array(image)

    #   Add an extra dimension to the array (since Keras expects a 4D array as input)
    image_array = np.expand_dims(image_array, axis=0)

    resultdict = {
        0 : 'Strawberry: Leaf_scorch',
        1 : 'Tomato: Tomato_Yellow_Leaf_Curl_Virus',
        2 : 'Tomato: Target_Spot',
        3 : 'Tomato: Late_blight',
        4 : 'Tomato: Spider_mites Two-spotted_spider_mite',
        5 : 'Tomato: Leaf_Mold',
        6 : 'Strawberry: healthy',
        7 : 'Apple: Cedar_apple_rust',
        8 : 'Apple: Black_rot',
        9 : 'Apple: Apple_scab	',
        10 : 'Potato: Late_blight',
        11 : 'Tomato: healthy',
        12 : 'Tomato: Early_blight',
        13 : 'Tomato: Tomato_mosaic_virus',
        14 : 'Tomato: Septoria_leaf_spot',
        15 : 'Potato: Early_blight',
        16 : 'Potato: healthy',
        17 : 'Tomato: Bacterial_spot',
        18 : 'Apple: healthy'
    }

    image_array /= 255

    # Use the model to predict the class of the image
    predictions = model.predict(image_array)
    return resultdict[np.argmax(predictions)]

# # Define the Streamlit app
# def app():
#     # Define the UI elements
#     st.title('Plant Disease Detection')
#     image = st.file_uploader('Upload an image')

#     # Make predictions on the uploaded image
#     if image is not None:
#         predictions = predict(image)
#         st.write(predictions)

# if __name__ == '__main__':
#     app()

# Define the Streamlit app
def app():
    # Set the page title and icon
    st.set_page_config(page_title='Plant Disease Detector', page_icon=':seedling:')

    # Define the app header
    # st.image('./logo.png', width=200)

    # Add a fixed logo image
    st.markdown(
        """
        <style>
        .logo-container {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 1rem;
        }

        .logo-container img {
            width: 150px;
            margin-right: 1rem;
        }

        .logo-container p {
            font-size: 2rem;
            font-weight: bold;
            color: white;
            margin: 0;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.write(
        f"""
        <div class="logo-container">
            <img src="https://user-images.githubusercontent.com/30645315/68544440-37ffdd80-03e9-11ea-8acd-3f3f9b6fc8b3.png" alt="Logo">
            <p>Plant Disease Detector</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.title('Plant Disease Detector')
    st.write('Upload an image of a plant leaf and we will predict if it is healthy or diseased.')

    # Define the UI elements
    image = st.file_uploader('Choose an image', type=['jpg', 'jpeg', 'png'])

    # Make predictions on the uploaded image
    if image is not None:
        prediction = predict(image)
        st.write('Prediction:', prediction)
        # st.image(image, caption='Uploaded image', width='200px')

# Run the app
if __name__ == '__main__':
    app()









