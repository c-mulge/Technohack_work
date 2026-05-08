import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('lead_model.pkl', 'rb'))

st.title("Lead Scoring System")

gender = st.selectbox("Gender", [0,1])

income = st.number_input("Monthly Income")

loan_amount = st.number_input("Loan Amount")

interest_rate = st.number_input("Interest Rate")

emi = st.number_input("EMI")

age = st.number_input("Age")

if st.button("Predict"):

    features = np.array([[gender,
                          income,
                          loan_amount,
                          interest_rate,
                          emi,
                          age]])

    prediction = model.predict(features)

    if prediction[0] == 1:
        st.success("Lead Likely to Convert")
    else:
        st.error("Lead Not Likely to Convert")