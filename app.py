import streamlit as st
from features import (
    disease_detection, plant_identification, plant_age_estimation, profit_prediction,
    plant_doctor, organic_treatment, chemical_treatment, weather_monitoring,
    rain_prediction, temperature_monitoring, humidity_monitoring, smart_irrigation,
    image_scanner, pest_detection, fruit_health, root_health, plant_dashboard,
    notifications, crop_recommendation, fertilizer_recommendation, tamil_language,
)

st.set_page_config(page_title="Plant Guardian AI", page_icon="🌱", layout="wide")
st.title("🌱 Plant Guardian AI")
st.caption("A modular Streamlit plant-care and agriculture assistant")

PAGES = {
    "Overview": None,
    "Disease Detection": disease_detection,
    "Plant Species Identification": plant_identification,
    "Plant Age Estimation": plant_age_estimation,
    "Profit & Market Planner": profit_prediction,
    "Virtual Plant Doctor": plant_doctor,
    "Organic Treatment Guide": organic_treatment,
    "Chemical Treatment Safety": chemical_treatment,
    "Live Weather Monitoring": weather_monitoring,
    "Rain Prediction": rain_prediction,
    "Temperature Monitoring": temperature_monitoring,
    "Humidity Monitoring": humidity_monitoring,
    "Smart Water Management": smart_irrigation,
    "Leaf Image Scanner": image_scanner,
    "Pest / Insect Identification": pest_detection,
    "Fruit Health Detection": fruit_health,
    "Root Health Analysis": root_health,
    "Plant Monitoring Dashboard": plant_dashboard,
    "Smart Notifications": notifications,
    "Crop Recommendation": crop_recommendation,
    "Fertilizer Recommendation": fertilizer_recommendation,
    "Tamil / English": tamil_language,
}

with st.sidebar:
    st.header("Navigation")
    page = st.radio("Choose a module", list(PAGES.keys()))
    st.divider()
    st.caption("Demo mode: connect verified AI models, sensors and APIs for live results.")

if PAGES[page] is None:
    st.subheader("Your smart plant-care workspace")
    a, b, c = st.columns(3)
    a.metric("Modules", len(PAGES) - 1)
    b.metric("Plant records", len(st.session_state.get("plants", [])))
    c.metric("Mode", "Prototype")
    st.info("Choose a module from the sidebar to get started.")
    st.markdown("""
    **Included:** image-analysis interfaces, plant care guidance, weather and water tools,
    crop planning, dashboard, reminders, and fertilizer guidance.

    **Important:** Image predictions in this starter project are not AI diagnoses.
    Weather and sensor values are only live when you configure an API or hardware device.
    """)
else:
    PAGES[page].render()
