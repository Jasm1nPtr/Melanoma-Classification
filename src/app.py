import streamlit as st

pg = st.navigation([
    st.Page("cnn.py", title="Model CNN"),
    st.Page("mobilenet.py", title="Model MobileNetV2"),
])
pg.run()

# import streamlit as st

# def main():
#     st.sidebar.title("Pilihan Model")
#     # Menambahkan navigasi di sidebar
#     page = st.sidebar.radio("Pilih model Anda", ("CNN", "MobileNetV2"))

#     if page == "CNN":
#         halaman_cnn()
#     elif page == "MobileNetV2":
#         halaman_mobilenet()

# def halaman_cnn():
#     st.title("Model CNN untuk Klasifikasi Melanoma")
#     st.write("Halaman ini menampilkan model CNN yang digunakan untuk klasifikasi citra melanoma.")
#     # Di sini Anda bisa menambahkan uploader file dan fungsi prediksi untuk CNN

# def halaman_mobilenet():
#     st.title("Model MobileNetV2 untuk Klasifikasi Melanoma")
#     st.write("Halaman ini menampilkan model MobileNetV2 yang digunakan untuk klasifikasi citra melanoma.")
#     # Di sini Anda bisa menambahkan uploader file dan fungsi prediksi untuk MobileNetV2

# if __name__ == "__main__":
#     main()

