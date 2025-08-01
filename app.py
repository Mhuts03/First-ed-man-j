import streamlit as st
import pandas as pd

st.set_page_config(page_title="Manual J HVAC App", layout="wide")

st.title("Manual J Load Calculator")

st.markdown("""
Welcome to the Manual J HVAC Load Calculator.  
This tool helps HVAC professionals estimate heating and cooling loads by room or for the entire house.
""")

# Sidebar: Basic info
st.sidebar.header("🏠 Building Info")
home_type = st.sidebar.selectbox("Home Type", ["Single-family", "Multi-family", "Mobile Home", "Apartment"])
zipcode = st.sidebar.text_input("Zip Code", value="14604")  # Rochester default
orientation = st.sidebar.selectbox("Home Orientation", ["North", "South", "East", "West"])

# Room-by-room entry
st.header("📋 Room Inputs")

with st.form("room_form"):
    col1, col2, col3 = st.columns(3)
    room_name = col1.text_input("Room Name", value="Living Room")
    sqft = col2.number_input("Room Area (sqft)", min_value=0)
    windows = col3.number_input("Window Area (sqft)", min_value=0)

    insulation = st.selectbox("Insulation Quality", ["Poor", "Average", "Good", "Excellent"])
    occupants = st.number_input("Number of Occupants", min_value=0, value=1)
    submit = st.form_submit_button("Add Room")

    if submit and sqft > 0:
        st.success(f"{room_name} added successfully (not yet stored — full version will allow saving).")

st.info("🔧 Full functionality is still being built, including load calculation, equipment sizing, and duct design.")

# Streamlit app code here
