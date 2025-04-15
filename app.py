
import streamlit as st
import numpy as np
import pickle

# Load the trained Random Forest model
model = pickle.load(open('rf_model.pkl', 'rb'))

st.title('Diabetes Prediction System')

st.markdown("Fill in the values below to check if the person is likely to have diabetes.")

# Input fields
pregnancies = st.number_input('Pregnancies', min_value=0)
glucose = st.number_input('Glucose Level', min_value=0)
bp = st.number_input('Blood Pressure', min_value=0)
skin = st.number_input('Skin Thickness', min_value=0)
insulin = st.number_input('Insulin Level', min_value=0)
bmi = st.number_input('BMI', min_value=0.0)
dpf = st.number_input('Diabetes Pedigree Function', min_value=0.0)
age = st.number_input('Age', min_value=1)

# Predict button
if st.button('Predict'):
    input_data = np.array([[pregnancies, glucose, bp, skin, insulin, bmi, dpf, age]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error('🔴 The person is diabetic')
    else:
        st.success('🟢 The person is not diabetic')
