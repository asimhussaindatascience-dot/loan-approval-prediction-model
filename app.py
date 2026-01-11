import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("model.pkl")

st.title("🏦 Loan Approval Prediction App")

st.write("Enter applicant details to predict loan approval")

# User inputs
no_of_dependents = st.number_input("Number of Dependents", 0, 10)
income_annum = st.number_input("Annual Income", 0)
loan_amount = st.number_input("Loan Amount", 0)
loan_term = st.number_input("Loan Term (months)", 0)
cibil_score = st.number_input("CIBIL Score", 300, 900)

residential_assets_value = st.number_input("Residential Assets Value", 0)
commercial_assets_value = st.number_input("Commercial Assets Value", 0)
luxury_assets_value = st.number_input("Luxury Assets Value", 0)
bank_asset_value = st.number_input("Bank Asset Value", 0)

education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])

# Encode inputs
education = 1 if education == "Graduate" else 0
self_employed = 1 if self_employed == "Yes" else 0

# Prediction
if st.button("Predict Loan Status"):
    input_data = np.array([[ 
        no_of_dependents,
        education,
        self_employed,
        income_annum,
        loan_amount,
        loan_term,
        cibil_score,
        residential_assets_value,
        commercial_assets_value,
        luxury_assets_value,
        bank_asset_value
    ]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")
