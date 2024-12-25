import streamlit as st

pg = st.navigation([
    st.Page("cnn.py", title="Model CNN"),
    st.Page("mobilenet.py", title="Model MobileNetV2"),
])
pg.run()


