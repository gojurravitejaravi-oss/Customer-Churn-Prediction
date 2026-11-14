import streamlit as st

st.title("Customer Churn Prediction")
st.write("Month-to-Month customer")

tenure = st.slider("Tenure (Months)", 0, 72, 10)
monthly = st.number_input("Monthly Charges", 20, 120, 70)
contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])

if st.button("Predict"):
    if contract == "Month-to-month" and tenure < 12:
        st.error("HIGH RISK - Customer will Churn! Give Offer!")
    else:
        st.success("LOW RISK - Customer will Stay")
