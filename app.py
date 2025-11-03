import streamlit as st

# App title
st.set_page_config(page_title="Simple Calculator", page_icon="🧮", layout="centered")
st.title("🧮 Simple Calculator App")

# Input fields
st.subheader("Enter Numbers:")
num1 = st.number_input("First Number", value=0.0, step=1.0)
num2 = st.number_input("Second Number", value=0.0, step=1.0)

# Operation selection
operation = st.selectbox(
    "Choose Operation",
    ["Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)"]
)

# Calculate button
if st.button("Calculate"):
    if operation == "Addition (+)":
        result = num1 + num2
        st.success(f"✅ Result: {num1} + {num2} = {result}")
    elif operation == "Subtraction (-)":
        result = num1 - num2
        st.success(f"✅ Result: {num1} - {num2} = {result}")
    elif operation == "Multiplication (×)":
        result = num1 * num2
        st.success(f"✅ Result: {num1} × {num2} = {result}")
    elif operation == "Division (÷)":
        if num2 != 0:
            result = num1 / num2
            st.success(f"✅ Result: {num1} ÷ {num2} = {result}")
        else:
            st.error("❌ Division by zero is not allowed!")

# Footer
st.markdown("---")
st.caption("Created with ❤️ using Streamlit")
