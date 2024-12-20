# -*- coding: utf-8 -*-
"""
Created on Tue May 10 01:55:28 2024

@author: Dmwin
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model = pickle.load(open('C:/Users/Dmwin/OneDrive/Desktop/stream lit/diabates/trained_model.sav', 'rb'))

#you can add more anytime ^^

with st.sidebar:
    
    selected=option_menu('Disease Prediction System',
                         ['Diabetes Prediction'],
                         
                         icons=['activity'],
                         
                         default_index=0)
 
#Diabetes Prediction Page
if (selected =='Diabetes Prediction'):
    
    #page title
    st.title('Diabetes Prediction using ML')
    
    #getting the input data from the user
    #column for input fields
    col1,col2,col3=st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value ')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of Individual')
    
    #code for Prediction
    diab_diagnosis=''
    
    #creating a button for prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction=diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0]==1):
            diab_diagnosis='The Individual is Diabetic'
            
        else:
            diab_diagnosis='The Individual is Not Diabetic'
            
    
    st.success(diab_diagnosis)