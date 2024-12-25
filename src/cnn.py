import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import load_img, img_to_array
import os

# --- CUSTOM STYLING 
st.set_page_config(page_title="Klasifikasi Citra Melanoma", layout="centered")
st.markdown("""
    <style>
    .stButton>button {
        color: white;
        background-color: #4CAF50;
        border-radius: 10px;
    }
    .stSuccess, .stInfo {
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.title("Model CNN untuk Klasifikasi Melanoma")
st.write("Halaman ini menampilkan model CNN yang digunakan untuk klasifikasi citra melanoma")

# --- FILE UPLOADER ---
upload = st.file_uploader("📤 Unggah citra melanoma di sini (PNG/JPG)", type=['png', 'jpg', 'jpeg'])

# --- PREDICT FUNCTION ---
def preprocess_image(image_path):
    """Preprocess input image to match the model's requirements."""
    img = load_img(image_path, target_size=(224, 224))
    img_array = img_to_array(img) / 255.0  
    img_array = np.expand_dims(img_array, axis=0)  
    return img_array

def predict(image_file, threshold=0.4):  
    class_names = ['Benign', 'Malignant']
    img_array = preprocess_image(image_file)

    # Load model
    model_path = "src/model/CNN.h5"
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file tidak ditemukan di {model_path}")
    model = load_model(model_path)

    # Predict
    predictions = model.predict(img_array)
    confidence = np.max(predictions)
    if confidence < threshold:
        predicted_class = "Uncertain"
    else:
        predicted_class = class_names[np.argmax(predictions)]

    return predicted_class, confidence

# --- MAIN LOGIC ---
if upload is not None:
    col1, col2 = st.columns(2)
    with col1:
        st.image(upload, caption="📸 Gambar yang diunggah", use_container_width=True)  

    with col2:
        st.subheader("🔍 Hasil Prediksi:")
        with st.spinner("⏳ Sedang memproses..."):
            try:
                result, confidence = predict(upload)
                st.success(f"✅ **Kelas Prediksi**: {result}")
                st.info(f"🔎 **Kepercayaan Prediksi**: {confidence:.2f}")
            except Exception as e:
                st.error(f"❌ Terjadi kesalahan: {str(e)}")
else:
    st.warning("⚠️ Silakan unggah gambar terlebih dahulu!")

# --- FOOTER ---
st.markdown("---")
st.markdown("Terima kasih ❤️")
