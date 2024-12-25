
import streamlit as st
import tensorflow as tf
import numpy as np
import os

# --- CUSTOM STYLING 
st.set_page_config(page_title="Klasifikasi Citra Melanoma", layout="centered")

# --- HEADER 
st.title("Klasifikasi Citra Melanoma")
st.write("Unggah gambar melanoma untuk prediksi")

# --- FILE UPLOADER 
upload = st.file_uploader("📤 Unggah citra melanoma di sini (PNG/JPG)", type=['png', 'jpg', 'jpeg'])

# --- PREDICT FUNCTION ---
def preprocess_image(image_file):
    img = tf.keras.utils.load_img(image_file, target_size=(224, 224))
    img_array = tf.keras.utils.img_to_array(img) / 255.0  
    img_array = tf.expand_dims(img_array, axis=0)  
    return img_array

def predict(image_file, threshold=0.6):
    class_names = ['Benign', 'Malignant']
    img_array = preprocess_image(image_file)

    # Load model
    model_path = "src/model/Melanoma_MobileNet.h5"
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file tidak ditemukan di {model_path}")
    model = tf.keras.models.load_model(model_path)
    
    # Prediksi
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
