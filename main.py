import pandas as pd
import numpy as np
import random
import pickle
import streamlit as st
from PIL import Image
  
pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)
  
def welcome():
    return 'welcome all'
  

def prediction(SEX,PATIENT_TYPE,INTUBED,PNEUMONIA,AGE,PREGNANT,DIABETES,COPD,ASTHMA,INMSUPR,HYP,OD,CARDIOVASCULAR,OBESITY,RENAL_CHRONIC,TOBOCCO):  
   
    prediction = classifier.predict(
        [[SEX,PATIENT_TYPE,INTUBED,PNEUMONIA,AGE,PREGNANT,DIABETES,COPD,ASTHMA,INMSUPR,HYP,OD,CARDIOVASCULAR,OBESITY,RENAL_CHRONIC,TOBOCCO]])
    print(prediction)
    return prediction
      
  
 
def main():
    st.title("COVID-19 Validator")
    html_temp = """
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;">Streamlit COVID-19 Classifier ML App </h1>
    </div>
    """

    st.markdown(html_temp, unsafe_allow_html = True)
      
    st.write("")
    # USMER = random.randint(1,2)
    # MEDICAL_UNIT = random.randint(1,13)
    # print(USMER," ",MEDICAL_UNIT)
    sex = st.radio("SEX ?",('Male','Female'))
    AGE = st.text_input("AGE ?")
    if sex=='Male':
        PREGNANT = 97 
        SEX = 1
    else:
        pregnant  = st.radio("Is the Patient Pregnant ?",('Yes','No'))
        SEX = 2
        if pregnant == 'Yes':
            PREGNANT = 1
        else:
            PREGNANT = 2
    patient_type = st.radio("Patient Type ?",('Returned Home','Hospitalized'))
    if patient_type == 'Returned Home' :
        PATIENT_TYPE = 1
    else:
        PATIENT_TYPE = 2
    intubed = st.radio  ("Is the Patient in Ventilator Support ?",('Yes','No'))
    if intubed == 'Yes':
        INTUBED = 1
    else:
        INTUBED = 2
    pneumonia = st.radio("Does the patient already have air sacs inflammation ?",('Yes','No'))
    if pneumonia == 'Yes':
        PNEUMONIA = 1
    else:
        PNEUMONIA = 2
    diabetes = st.radio("Does the patient have Diabetes ?",('Yes','No'))
    if diabetes == 'Yes':
        DIABETES = 1 
    else :
        DIABETES = 2
    copd = st.radio("Does the patient has Chronic Obstructive Pulmonary disease ?",('Yes','No'))
    if copd == 'Yes':
        COPD = 1 
    else :
        COPD = 2
    asthma = st.radio("Does the patient has Asthma ?",('Yes','No'))
    if asthma == 'Yes':
        ASTHMA = 1
    else:
        ASTHMA = 2
    inmsupr = st.radio("Is the patient Immunosuppressed ?",('Yes','No'))
    if inmsupr == 'Yes':
        INMSUPR = 1 
    else:
        INMSUPR = 2
    hyp = st.radio("Does the patient has Hypertension ?",('Yes','No'))
    if hyp == 'Yes':
        HYP = 1
    else :
        HYP = 2
    cardio = st.radio("Does the patient has Heart or Blood Vessels related disease ?",('Yes','No'))
    if cardio == 'Yes' :
        CARDIOVASCULAR = 1 
    else:
        CARDIOVASCULAR = 2
    obese = st.radio("Is the patient Obese ?",('Yes','No'))
    if obese == 'Yes':
        OBESITY = 1 
    else :
        OBESITY = 2
    renal_chronic = st.radio("Does the patient has Chronic Renal disease ?",('Yes','No'))
    if renal_chronic == 'Yes':
        RENAL_CHRONIC = 1 
    else :
        RENAL_CHRONIC = 2
    od = st.radio("Does the patient has other disease ?",('Yes','No'))
    if od == 'Yes':
        OD = 1
    else :
        OD = 2
    tobocco = st.radio("Is the patient a Tobacco user",('Yes','No'))
    if tobocco == 'Yes':
        TOBOCCO = 1 
    else :
        TOBOCCO = 2 
    res_inp = st.radio("COVID-19 Positive/Negative",('Positive','Negative'))

    #  = st.text_input("", "Type Here")
    result =""
    
    if st.button("Submit"):
        result = prediction(SEX,PATIENT_TYPE,INTUBED,PNEUMONIA,AGE,PREGNANT,DIABETES,COPD,ASTHMA,INMSUPR,HYP,OD,CARDIOVASCULAR,OBESITY,RENAL_CHRONIC,TOBOCCO)
    if(result in[1,2,3]):
        result = 'Positive'
    else:
        result = 'Negative'
    if res_inp == result :
        st.success("File uploaded Successfully")
    else:
        st.error("Invalid Data Entered")
     
if __name__=='__main__':
    main()