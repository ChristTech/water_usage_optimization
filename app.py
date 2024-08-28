import streamlit as st
import pandas as pd
import joblib

# Load the model and column names
model = joblib.load('water_requirement_model.pkl')
column_names = joblib.load('column_names.pkl')

# Streamlit app title
st.title('Water Requirement Predictor')

# CSS to add a background image
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0.5)), 
        url("https://plus.unsplash.com/premium_photo-1661825536186-19606cd9a0f1?w=400&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8d2F0ZXIlMjB1c2UlMjBpbiUyMGFncmljdWx0dXJlfGVufDB8fDB8fHww");
        background-size: cover;
        background-position: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Input fields on the main page instead of the sidebar
st.header('Input Parameters')

# Define input fields
crop_type = st.selectbox('CROP TYPE', options=['BANANA', 'BEAN', 'CABBAGE', 'CITRUS', 'COTTON', 'MAIZE'])
soil_type = st.selectbox('SOIL TYPE', options=['DRY', 'WET'])
region = st.selectbox('REGION', options=['DESERT', 'SEMI ARID', 'SEMI HUMID'])
temperature = st.selectbox('TEMPERATURE in degrees', options=['20', '21-30', '30-40', '40-50'])
weather_condition = st.selectbox('WEATHER CONDITION', options=['NORMAL', 'SUNNY', 'WINDY', 'RAINY'])

# Encode input values
input_values = {
    'CROP TYPE_BANANA': 1 if crop_type == 'BANANA' else 0,
    'CROP TYPE_BEAN': 1 if crop_type == 'BEAN' else 0,
    'CROP TYPE_CABBAGE': 1 if crop_type == 'CABBAGE' else 0,
    'CROP TYPE_CITRUS': 1 if crop_type == 'CITRUS' else 0,
    'CROP TYPE_COTTON': 1 if crop_type == 'COTTON' else 0,
    'CROP TYPE_MAIZE': 1 if crop_type == 'MAIZE' else 0,
    'SOIL TYPE_DRY': 1 if soil_type == 'DRY' else 0,
    'SOIL TYPE_WET': 1 if soil_type == 'WET' else 0,
    'REGION_DESERT': 1 if region == 'DESERT' else 0,
    'REGION_SEMI ARID': 1 if region == 'SEMI ARID' else 0,
    'REGION_SEMI HUMID': 1 if region == 'SEMI HUMID' else 0,
    'TEMPERATURE_20': 1 if temperature == '20' else 0,
    'TEMPERATURE_21-30': 1 if temperature == '21-30' else 0,
    'TEMPERATURE_30-40': 1 if temperature == '30-40' else 0,
    'TEMPERATURE_40-50': 1 if temperature == '40-50' else 0,
    'WEATHER CONDITION_NORMAL': 1 if weather_condition == 'NORMAL' else 0,
    'WEATHER CONDITION_SUNNY': 1 if weather_condition == 'SUNNY' else 0,
    'WEATHER CONDITION_WINDY': 1 if weather_condition == 'WINDY' else 0,
    'WEATHER CONDITION_RAINY': 1 if weather_condition == 'RAINY' else 0
}

# Ensure all columns are present
input_df = pd.DataFrame([input_values], columns=column_names).fillna(0)

# Prediction
if st.button('Predict'):
    prediction = model.predict(input_df)[0]

    # Create an expander for the result
    with st.expander("Prediction Result", expanded=True):
        st.markdown(
            f"<h2 style='text-align: center; color: black; font-size: 30px;'>Predicted Water Requirement: {prediction:.2f} litres</h2>",
            unsafe_allow_html=True
        )
