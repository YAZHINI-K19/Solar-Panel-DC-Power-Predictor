import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib
from io import BytesIO

# Load trained model
model = joblib.load("solar_model.pkl")

# Page configuration
st.set_page_config(
    page_title="Solar DC Power Predictor",
    layout="centered"
)

# Title
st.title("Solar Panel DC Power Predictor")
st.markdown("Predict DC power output using environmental factors like irradiation and temperature.")

# Input section
st.subheader("Enter Environmental Conditions")

# Centered input layout
col1, col2 = st.columns(2)
with col1:
    irradiation = st.slider("Irradiation (kW/m²)", 0.0, 1.5, 0.5, step=0.01)
    ambient_temp = st.slider("Ambient Temperature (°C)", 10.0, 50.0, 25.0, step=0.5)

with col2:
    module_temp = st.slider("Module Temperature (°C)", 15.0, 70.0, 40.0, step=0.5)
    hour = st.slider("Hour of Day", 0, 23, 12)

# Predict button
if st.button("Predict"):
    input_data = pd.DataFrame([[irradiation, ambient_temp, module_temp, hour]],
                               columns=['IRRADIATION', 'AMBIENT_TEMPERATURE', 'MODULE_TEMPERATURE', 'HOUR'])

    prediction = model.predict(input_data)[0]
    st.success(f"Predicted DC Power Output: {prediction:.2f} kW")

    # Bar chart of input
    st.subheader("Input Summary")
    st.bar_chart(input_data.T)

    # PNG Export
    fig, ax = plt.subplots(figsize=(6, 4))
    input_data.T.plot(kind='barh', legend=False, ax=ax, color='skyblue')
    ax.set_xlabel("Value")
    ax.set_title("Input Features")
    plt.tight_layout()

    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    st.download_button(
        label="Download Chart as PNG",
        data=buffer.getvalue(),
        file_name="dc_power_input_summary.png",
        mime="image/png"
    )

# Footer
st.markdown("---")
st.caption("Developed by Yazhini | SolaR DC Predictor")
