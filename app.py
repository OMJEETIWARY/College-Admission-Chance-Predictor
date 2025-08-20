import pickle
import numpy as np # type: ignore
import streamlit as st # type: ignore

model = pickle.load(open("lr.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.title("🎓 Admission Prediction App")


gre = st.number_input("GRE Score", min_value=260, max_value=340, step=1)
toefl = st.number_input("TOEFL Score", min_value=0, max_value=120, step=1)
univ_rating = st.slider("University Rating", 1, 5, 3)
sop = st.slider("SOP Strength", 1.0, 5.0, 3.0, 0.5)
lor = st.slider("LOR Strength", 1.0, 5.0, 3.0, 0.5)
cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0, step=0.01)
research = st.radio("Research Experience", [0, 1])

if st.button("Predict"):
    features = np.array([[gre, toefl, univ_rating, sop, lor, cgpa, research]])

    features_scaled = scaler.transform(features)    
    
    prediction = model.predict(features_scaled)[0]
    prediction = max(0, min(1, prediction))
    
    st.success(f"Chance of Admission: {prediction*100:.2f}%")
    st.progress(int(prediction*100))
