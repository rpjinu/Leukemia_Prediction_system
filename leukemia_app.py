import streamlit as st
import pandas as pd
import joblib

model=joblib.load(r"C:\Users\Ranjan kumar pradhan\.vscode\Model.pkl")

st.title("Leukemia Prediction System")
st.write("Enter patient details below:")

# Input fields
Age = st.number_input("Age", min_value=1, max_value=100, value=25)
WBC_Count = st.number_input("WBC_Count", min_value=2300, max_value=14000, value=2700)
RBC_Count = st.number_input("RBC_Count", min_value=3, max_value=7, value=5)
Platelet_Count=st.number_input("Platelet_Count",min_value=100000,max_value=350000,value=277877)
Hemoglobin_Level=st.number_input("Hemoglobin_Level",min_value=5,max_value=21,value=13)
Bone_Marrow_Blasts=st.number_input("Bone_Marrow_Blasts",min_value=1,max_value=99,value=32)
BMI=st.number_input("BMI",max_value=50,min_value=4,value=35)

def preprocess_input(Age,WBC_Count,RBC_Count,Platelet_Count,Hemoglobin_Level,Bone_Marrow_Blasts,BMI):
# Create a DataFrame with the input data
    input_data = pd.DataFrame({
        'Age': [Age],
        'WBC_Count': [WBC_Count],
        'RBC_Count': [RBC_Count],
        'Platelet_Count': [Platelet_Count],
        'Hemoglobin_Level': [Hemoglobin_Level],
        'Bone_Marrow_Blasts': [Bone_Marrow_Blasts],
        'BMI': [BMI]
    })
    
    return input_data

# Predict the size
if st.button("Predict Leukemia Disease"):
    input_data = preprocess_input(Age,WBC_Count,RBC_Count,Platelet_Count,Hemoglobin_Level,Bone_Marrow_Blasts,BMI)
    prediction = model.predict(input_data)
    
    # Map the predicted size back to the original labels
    mapping = {0: 'Negative Leukemia', 1: 'Positive Leukemia'}
    predicted_leukemia = mapping.get(prediction[0], 'Unknown')
    
    st.write(f"Predicted Leukemia:- {predicted_leukemia}")