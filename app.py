import streamlit as st
from PIL import Image
from pathlib import Path

st.set_page_config(page_title="Plant Guardian AI", page_icon="🌱", layout="centered")

st.markdown("""
<style>
.main {max-width: 900px; padding-top: 1.5rem;}
.hero {padding: 1.3rem; border-radius: 16px; background: #eaf8ed;}
.hero h1 {color: #176b38; margin-bottom: .25rem;}
div.stButton > button {width:100%; border-radius:10px;}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="hero"><h1>🌱 Plant Guardian AI</h1>'
    '<p>Smart plant-health checking prototype</p></div>',
    unsafe_allow_html=True,
)
st.write("Upload a clear photo of a plant leaf to get started.")

MODEL_PATH = Path("plant_disease_model.keras")
LABELS_PATH = Path("class_names.txt")

uploaded = st.file_uploader("Choose a leaf photo", type=["jpg", "jpeg", "png"])

if uploaded:
    image = Image.open(uploaded).convert("RGB")
    st.image(image, caption="Your uploaded leaf photo", use_container_width=True)

    if st.button("Analyse plant"):
        if MODEL_PATH.exists() and LABELS_PATH.exists():
            try:
                import numpy as np
                from tensorflow.keras.models import load_model

                @st.cache_resource
                def load_plant_model(path):
                    return load_model(path)

                model = load_plant_model(str(MODEL_PATH))
                labels = [
                    line.strip()
                    for line in LABELS_PATH.read_text(encoding="utf-8").splitlines()
                    if line.strip()
                ]
                resized = image.resize((224, 224))
                pixels = np.asarray(resized, dtype="float32") / 255.0
                probabilities = model.predict(np.expand_dims(pixels, 0), verbose=0)[0]
                best_index = int(np.argmax(probabilities))

                if best_index >= len(labels):
                    st.error("Model labels do not match the model output. Please check class_names.txt.")
                else:
                    st.success(f"Model prediction: **{labels[best_index]}**")
                    st.write(f"Model confidence: **{float(probabilities[best_index]) * 100:.1f}%**")
                    st.warning(
                        "This is an AI estimate, not a confirmed diagnosis. "
                        "Check the plant carefully and consult an agricultural expert for important decisions."
                    )
            except Exception as error:
                st.error("The model could not be loaded. Check that the model file and dependencies are valid.")
                st.caption(f"Technical detail: {error}")
        else:
            st.info(
                "Photo uploaded successfully. The trained disease-detection model has not been added yet, "
                "so this app will not guess a disease."
            )
            st.markdown(
                "**To enable AI predictions:** add `plant_disease_model.keras` and "
                "`class_names.txt` to the root of this GitHub repository. See README.md."
            )

st.divider()
st.subheader("🌿 General plant-care checklist")
col1, col2 = st.columns(2)
with col1:
    st.markdown("**💧 Watering**")
    st.write("Check soil moisture before watering. Avoid leaving soil waterlogged.")
    st.markdown("**☀️ Light**")
    st.write("Provide light suitable for the plant species and avoid sudden changes.")
with col2:
    st.markdown("**🍃 Leaf checks**")
    st.write("Check both sides of leaves for spots, pests, or unusual colour changes.")
    st.markdown("**🧹 Cleanliness**")
    st.write("Remove fallen leaves and keep tools clean.")

st.caption(
    "Educational prototype only. Photo-based predictions may be wrong and are not a substitute "
    "for advice from a local agricultural expert."
)
