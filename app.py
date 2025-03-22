import streamlit as st

# Title of the app
st.title("📏 Unit Converter")

# Sidebar for unit selection
st.sidebar.header("⚙️ Settings")
conversion_type = st.sidebar.selectbox(
    "Choose a conversion type",
    ["Length", "Weight", "Temperature"]
)

# Add a description or instructions
st.markdown("""
Welcome to the **Unit Converter**! This tool helps you convert between different units of measurement. 
Select the conversion type from the sidebar, choose the units, and enter the value to convert.
""")

# Function to convert length
def convert_length(value, from_unit, to_unit):
    if from_unit == "Meters" and to_unit == "Feet":
        return value * 3.28084
    elif from_unit == "Feet" and to_unit == "Meters":
        return value / 3.28084
    elif from_unit == "Meters" and to_unit == "Inches":
        return value * 39.3701
    elif from_unit == "Inches" and to_unit == "Meters":
        return value / 39.3701
    else:
        return value

# Function to convert weight
def convert_weight(value, from_unit, to_unit):
    if from_unit == "Kilograms" and to_unit == "Pounds":
        return value * 2.20462
    elif from_unit == "Pounds" and to_unit == "Kilograms":
        return value / 2.20462
    elif from_unit == "Kilograms" and to_unit == "Ounces":
        return value * 35.274
    elif from_unit == "Ounces" and to_unit == "Kilograms":
        return value / 35.274
    else:
        return value

# Function to convert temperature
def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    else:
        return value

# Main conversion logic
if conversion_type == "Length":
    st.header("📏 Length Conversion")
    length_units = ["Meters", "Feet", "Inches"]
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", length_units)
    with col2:
        to_unit = st.selectbox("To", length_units)
    value = st.number_input("Enter value", value=1.0, min_value=0.0)
    result = convert_length(value, from_unit, to_unit)
    st.success(f"**Result:** {value} {from_unit} = {result:.2f} {to_unit}")

elif conversion_type == "Weight":
    st.header("⚖️ Weight Conversion")
    weight_units = ["Kilograms", "Pounds", "Ounces"]
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", weight_units)
    with col2:
        to_unit = st.selectbox("To", weight_units)
    value = st.number_input("Enter value", value=1.0, min_value=0.0)
    result = convert_weight(value, from_unit, to_unit)
    st.success(f"**Result:** {value} {from_unit} = {result:.2f} {to_unit}")

elif conversion_type == "Temperature":
    st.header("🌡️ Temperature Conversion")
    temp_units = ["Celsius", "Fahrenheit", "Kelvin"]
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", temp_units)
    with col2:
        to_unit = st.selectbox("To", temp_units)
    value = st.number_input("Enter value", value=1.0)
    result = convert_temperature(value, from_unit, to_unit)
    st.success(f"**Result:** {value} {from_unit} = {result:.2f} {to_unit}")

# Add a footer
st.markdown("---")
st.markdown("© 2023 Unit Converter. All rights reserved.")