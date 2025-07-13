# Solar Panel DC Power Predictor

This project is a machine learning-powered application that predicts the DC power output of a solar panel based on environmental inputs like irradiation, ambient temperature, module temperature, and hour of the day. It features a user-friendly interface developed with Streamlit.

# Features

* Predicts DC power output using a Random Forest Regression model
* Clean, light-themed Streamlit web interface
* Sliders for easy input of environmental parameters
* Real-time prediction output with input summary chart
* Downloadable PNG chart of input data for reports

# Project Structure

* app.py – Main Streamlit web application
* solar\_model.pkl – Trained machine learning model
* Plant\_1\_Generation\_Data.csv – Solar plant generation data
* Plant\_1\_Weather\_Sensor\_Data.csv – Environmental sensor data
* requirements.txt – Python package dependencies
* README – Project overview and instructions

# Technologies Used

* Python
* Pandas
* Scikit-learn
* Matplotlib
* Joblib
* Streamlit

# How to Run

1. Clone the repository
   git clone [https://github.com/YAZHINI-K19/solar-panel-predictor](https://github.com/YAZHINI-K19/solar-panel-predictor)
   
   cd solar-panel-predictor

3. Install dependencies
   pip install -r requirements.txt

4. Launch the application
   streamlit run app.py

# Input Parameters

* Irradiation (kW/m²)
* Ambient Temperature (°C)
* Module Temperature (°C)
* Hour of Day (0–23)

# Output

* Predicted DC Power Output (kW)
* Input summary as a horizontal bar chart
* PNG export option for the chart

# Developed By

Yazhini
Project Title: Solar Panel DC Power Predictor

GitHub: [https://github.com/YAZHINI-K19](https://github.com/YAZHINI-K19)
