import cv2
import streamlit as st
import numpy as np
from urllib.request import urlopen

# Page configuration
st.set_page_config(page_title="Image Processing App", page_icon="🎨", layout="wide")

st.title("🎨 Image Processing - Gaussian Blur")
st.markdown("---")

# Sidebar for controls
with st.sidebar:
    st.header("📸 Image Source")
    source = st.selectbox("Select Input Source", ["📷 Webcam", "🌐 Internet URL", "📂 Upload File"])

# Main content
frame = None
if source == "📷 Webcam":
    picture = st.camera_input("Capture an image")
    if picture:
        file_bytes = np.asarray(bytearray(picture.getvalue()), dtype=np.uint8)
        frame = cv2.imdecode(file_bytes, 1)

elif source == "🌐 Internet URL":
    url = st.text_input("Enter Image URL", "https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Wolf_%28Canis_lupus%29_running.jpg/640px-Wolf_%28Canis_lupus%29_running.jpg")
    if url:
        try:
            resp = urlopen(url)
            image = np.asarray(bytearray(resp.read()), dtype=np.uint8)
            frame = cv2.imdecode(image, 1)
        except Exception as e:
            st.error(f"Failed to load image: {e}")

elif source == "📂 Upload File":
    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        frame = cv2.imdecode(file_bytes, 1)

# Gaussian Blur processing
if frame is not None:
    with st.sidebar:
        st.header("🛠️ Processing Parameters")
        ksize = st.slider("Gaussian Blur Kernel Size", 1, 31, 5, step=2)  # ต้องเป็นเลขคี่
    
    blurred = cv2.GaussianBlur(frame, (ksize, ksize), 0)
    
    st.subheader("Original Image")
    st.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), use_column_width=True)
    
    st.subheader("Gaussian Blur Result")
    st.image(cv2.cvtColor(blurred, cv2.COLOR_BGR2RGB), use_column_width=True)
