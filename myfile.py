import streamlit as st
import numpy as np
from PIL import Image
import pickle

# Load the saved model

model1 = pickle.load(open("family_model.pkl","rb"))


# Mapping numeric labels back to names
family = {0: "Chote papa", 1: "Lakshay", 2: "Mummy", 3: "Pita ji", 4: "Taniya"}


# Streamlit UI

st.title("🎉 Family Image Classifier")

uploaded_file = st.file_uploader("Upload an image of your family member ", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Show uploaded image
    img = Image.open(uploaded_file).convert("RGB").resize((128, 128))
    st.image(img, caption="Uploaded Image", use_column_width=True)

    # Convert to numpy and predict
    img_array = np.array(img).flatten().reshape(1, -1)
    pred = model1.predict(img_array)[0]

    st.success(f"✅ Predicted Member Name: {family[pred]}")
    
    st.error(f"")

 
