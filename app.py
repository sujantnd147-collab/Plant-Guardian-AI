import json
from pathlib import Path
import numpy as np
import streamlit as st
from PIL import Image

from src.predictor import load_model, predict_image
from src.care import care_advice

st.set_page_config(page_title="Plant Guardian AI", page_icon="🌱", layout="wide")

st.markdown("""
<style>
.hero {padding: 1.5rem 1.8rem; border-radius: 18px; background: linear-gradient(120deg,#e8f5e9,#f1f8e9);}
.hero h1 {color:#1b5e20; margin-bottom:.2rem;}
.small-muted {color:#55715a;}
.card {padding:1rem; border:1px solid #dce9dc; border-radius:14px; background:#fbfffb;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="hero"><h1>🌱 Plant Guardian AI</h1><p class="small-muted">AI-assisted plant leaf screening and practical care guidance</p></div>', unsafe_allow_html=True)
st.write("Upload a clear leaf photo to receive a model prediction and suggested next steps.")

with st.sidebar:
    st.header("About this project")
    st.write("A computer-vision demo built with TensorFlow and Streamlit.")
    st.info("Predictions are screening suggestions, not a confirmed diagnosis. Image quality, lighting, and unseen diseases can affect results.")
    st.caption("For best results, photograph one leaf in natural light against a plain background.")

uploaded = st.file_uploader("Upload a plant leaf image", type=["jpg", "jpeg", "png"])
model_path = Path("models/plant_guardian_mobilenet.keras")
labels_path = Path("models/class_names.json")

if uploaded:
    image = Image.open(uploaded).convert("RGB")
    left, right = st.columns([1, 1])
    with left:
        st.image(image, caption="Uploaded leaf image", use_container_width=True)
    with right:
        st.subheader("Analysis")
        if not model_path.exists() or not labels_path.exists():
            st.warning("The trained model is not installed yet. Follow the README to download the dataset and train the model first.")
            st.code("python train.py --data_dir data/PlantVillage")
        else:
            try:
                model = load_model(str(model_path))
                labels = json.loads(labels_path.read_text())
                label, confidence, top3 = predict_image(model, image, labels)
                st.metric("Model prediction", label.replace("___", " — ").replace("_", " "))
                st.metric("Prediction score", f"{confidence:.1%}")
                st.caption("The score is the model's confidence for its selected class, not a guarantee of correctness.")
                st.subheader("Other possible classes")
                for name, score in top3[1:]:
                    st.write(f"- {name.replace('___', ' — ').replace('_', ' ')}: {score:.1%}")
                st.subheader("Suggested next steps")
                for item in care_advice(label):
                    st.write(f"• {item}")
            except Exception as exc:
                st.error(f"Could not analyse this image: {exc}")

st.divider()
st.subheader("How to use the result")
st.write("Compare the prediction with the whole plant, inspect multiple leaves, and seek local agricultural guidance if symptoms are spreading or the plant is valuable.")
st.caption("Plant Guardian AI • Educational prototype")
