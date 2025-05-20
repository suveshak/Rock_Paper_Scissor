# import streamlit as st
# from PIL import Image
# import cv2
# import numpy as np
# from ultralytics import YOLO
# import tempfile

# # Load YOLOv8 model
# model = YOLO("last.pt")  # change to your model path if needed

# st.set_page_config(page_title="Rock Paper Scissor Detection", layout="centered")
# st.title("Rock Paper Scissor Detection App")

# uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

# if uploaded_file is not None:
#     # Read the uploaded image
#     image = Image.open(uploaded_file).convert("RGB")
#     st.image(image, caption="Uploaded Image", use_column_width=True)

#     with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
#         image.save(tmp.name)
#         tmp_path = tmp.name

#     # Run YOLOv8 detection
#     results = model(tmp_path)[0]

#     # Plot results
#     result_image = results.plot()  # this gives back a numpy array
#     st.image(result_image, caption="Detected Objects", use_column_width=True)
import streamlit as st
from PIL import Image
import cv2
import numpy as np
from ultralytics import YOLO
import tempfile

# Load YOLOv8 model
model = YOLO("last.pt")  # Replace with your model path if different

# Set page configuration
st.set_page_config(page_title="🪨📄✂️ Rock Paper Scissor Detector", layout="centered")

# Proper background color set using right selector
st.markdown("""
    <style>
        /* Background fix for Streamlit */
        .stApp {
            background-color: #7CA7EB; /* BLUE */
        }
        .title {
            font-size: 42px;
            color: #000000; /* black */
            text-align: center;
            font-weight: bold;
        }
        .subtitle {
            font-size: 20px;
            color: #000000; /* black */
            text-align: center;
        }
        .stButton>button {
            background-color: #000080; /* navy blue */
            color: white;
            border-radius: 10px;
            padding: 10px 20px;
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)

# App Title
st.markdown('<div class="title">🪨📄✂️ Rock Paper Scissor Detection</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Upload an image to detect gestures using YOLOv8!</div>', unsafe_allow_html=True)
st.markdown("---")

# Sample gesture examples
st.subheader("ROCK, PAPER OR SCISSOR?")
col1, col2, col3 = st.columns(3)
with col1:
    st.image("https://wrpsa.com/wp-content/uploads/2021/08/rock.png", caption="Rock")
with col2:
    st.image("https://wrpsa.com/wp-content/uploads/2021/08/paper.png", caption="Paper")
with col3:
    st.image("https://wrpsa.com/wp-content/uploads/2021/08/scissors.png", caption="Scissor")

st.markdown("---")

# Upload Section
uploaded_file = st.file_uploader("📷 Upload Your Hand Gesture Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display uploaded image
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="🖼️ Uploaded Image", use_column_width=True)

    # Save temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
        image.save(tmp.name)
        tmp_path = tmp.name

    # Run YOLOv8 model
    with st.spinner("🔍 Detecting... Please wait..."):
        results = model(tmp_path)[0]
        result_image = results.plot()  # numpy array

    # Display detection result
    st.image(result_image, caption="✅ Detected Gesture", use_column_width=True)

    # Get predicted class names
    detected_classes = [model.names[int(cls)] for cls in results.boxes.cls]
    st.success(f"🎉 Detected: {', '.join(detected_classes)}")
else:
    st.info("👆 Upload a hand gesture image to begin.")
