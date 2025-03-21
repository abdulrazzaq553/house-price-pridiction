import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open("House_price_pred", "rb") as file:
    model = pickle.load(file)

# Load the cleaned data
cleaned_data = pd.read_csv("cleaned_data1.csv")

# Extract unique locations for dropdown
locations = sorted(cleaned_data["location"].unique())

# Streamlit UI
st.title("🏠 Bangalore House Price Predictor")
st.write("Want to predict the price of a new house in Bangalore? Try filling in the details below:")

# User Inputs
location = st.selectbox("Select the Location:", locations)
bhk = st.number_input("Enter BHK:", min_value=1, max_value=10, step=1)
bath = st.number_input("Enter Number of Bathrooms:", min_value=1, max_value=10, step=1)
total_sqft = st.number_input("Enter Total Square Feet:", min_value=300, max_value=10000, step=50)

# Predict Button
if st.button("Predict Price"):
    # Prepare input data as DataFrame
    input_data = pd.DataFrame([[location, total_sqft, bath, bhk]], columns=["location", "total_sqft", "bath", "bhk"])
    
    # Predict using the model
    prediction = model.predict(input_data)[0]
    
    # Display prediction
    st.success(f"Predicted Price: ₹{prediction:,.2f}")
