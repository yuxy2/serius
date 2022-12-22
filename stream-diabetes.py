import pickle
import streamlit as st

# membaca model
diabetes_model = pickle.load(open('diabetes_moodel.sav','rb'))

# Judul Web
st.title('Prediksi Penyakit Diabetes')
col1,col2= st.columns(2)

with col1:
    Pregnancies = st.number_input ('Input Nilai pregnancies')
with col2:
    Glucose = st.number_input ('Input Nilai Glucose')
with col1:
    BloodPressure = st.number_input('Input Nilai BloodPressure')
with col2:
    SkinThickness = st.number_input ('Input NIlai SkinThickness')
with col1:
    Insulin = st.number_input ('Input Nilai Insulin')
with col2:
    BMI = st.number_input('Input Nilai Indeks Masa Tubuh')
with col1:
    DiabetesPedigreeFunction = st.number_input ('Input NIlai DiabetesPedigreeFunction')
with col2:
    Age = st.number_input ('Input Nilai Age')


# code prediksi
diab_diagnosis =''

# button
if st.button('Test Prediksi Diabetes'):
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure,	SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])


    if(diab_prediction[0] == 1) :
        diab_diagnosis = 'Pasien Terkena Diabetes'
    else :
        diab_diagnosis = 'Pasien Tidak Terkena Diabetes'
        
st.success(diab_diagnosis)
