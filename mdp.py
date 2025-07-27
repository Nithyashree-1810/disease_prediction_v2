# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 21:46:14 2024

@author: fidel
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu



diabetes_model = pickle.load(open(r"C:/Users/fidel/Downloads/diabetes_model (2).sav",'rb'))

heartdis_model = pickle.load(open(r"C:/Users/fidel/Downloads/heart_disease_model.sav",'rb'))


parkinson =  pickle.load(open(r"C:/Users/fidel/Downloads/parkinsons_model (2).sav",'rb'))

cancer=pickle.load(open(r"C:/Users/fidel/Downloads/cancer_model (1).sav",'rb'))


#diabetes disease

with st.sidebar:
    
     selected = option_menu('Multiple Disease Prediction System',
                         
                            ['diabetes disease prediction',
                             'heart disease prediction',
                             'parkinson disease prediction',
                             'cancer disease prediction'],
                              default_index=0)
    
    
if (selected == 'diabetes disease prediction'):
     
    st.title('diabetes prediction using ML')
    
    col1,col2=st.columns(2)
    
    with col1:
         Pregnancies=st.text_input('Number of Pregnancies')
    with col2:
         glucose=st.text_input('Glucose level')
    with col1:
         bloodpressure=st.text_input('Blood Pressure Value')
    with col2:
         skinthickness=st.text_input('Skin Thickness Value')
    with col1:
         insulin = st.text_input('Insulin value')
    with col2:
         BMI=st.text_input('BMI value')
    with col1:
         diabetespedigreefunction=st.text_input('Diabetes Pedigree Function value')
    with col2:
         age = st.text_input('Age of the person')
    
    diab_diagnosis=''
    
    if st.button('Diabetes Test Result'):

            
    
      diab_prediction = diabetes_model.predict([[Pregnancies,glucose,bloodpressure,skinthickness,insulin,BMI,diabetespedigreefunction,age]])
        
      if (diab_prediction[0]==1):
            diab_diagnosis='The person is diabetic'
      else:
            diab_diagnosis = 'The person is not diabetic'
            
    st.success(diab_diagnosis)


#heart disease
       
if (selected == 'heart disease prediction'):
    
    st.title('heart disease prediction using ML')
    
    col1,col2=st.columns(2)
    
    with col1:
         age = st.text_input('AGE OF THE PERSON')
    with col2:
         sex = st.text_input('SEX')
    with col1:
         cp	= st.text_input('chest pain')
    with col2:
        trestbps = st.text_input('RESTING BLOOD PRESSURE')
    with col1:
        chol=st.text_input('SERUM CHOLESTRAL IN mg/dl')
    with col2:
        fbs	=st.text_input('FASTING BLOOD SUGAR > 120 mg/dl')
    with col1:
        restecg	= st.text_input('RESTING ELECTROCARDIOGRAPHIC RESULTS')
    with col2:
        thalach	= st.text_input('MAXIMUM HEART RATE ACHIEVED')
    with col1:
        exang =st.text_input('EXERCISE INDUCED ANGINA')	
    with col2:
        oldpeak=st.text_input('ST DEPRESSION INDUCED BY EXERCISE')
    with col1:
        slope=st.text_input('HEART RATE SLOPE')
    with col2:
        ca=st.text_input('MAJOR VESSELS COLORED BY FLOUROSOPY')
    with col1:
        thal=st.text_input('thal:0 = normal; 1 = fixed defect ; 2 = reversable defect')
        
        heart_diagnosis=''
        
    if st.button('Heart Disease Test Result'):
        heart_prediction = heartdis_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
         
        if(heart_prediction[0] == 1):
            heart_diagnosis='the person is having heart disease'
        else:
            heart_diagnosis='the person does not have any heart disease'
            
    st.success(heart_diagnosis)
#parkinson disease
        
if (selected == 'parkinson disease prediction'):
    
    st.title( 'parkinson disease prediction using ML ')
    
    col1,col2,col3,col4=st.columns(4)
    
    with col1:
        Fo_Hz=st.text_input('MDVP:Fo(Hz)')
    with col2:
       Fhi_Hz=st.text_input('MDVP:Fhi(Hz)')
    with col3 :
        Flo_Hz=st.text_input('MDVP:Flo(Hz)')
    with col4:
         Jitter_percent = st.text_input('MDVP:Jitter(%)')	
    with col1 :
        Jitter_Abs=st.text_input('MDVP:Jitter(Abs)')	
    with col2:
        RAP=st.text_input(	'MDVP:RAP')
    with col3:
        PPQ=st.text_input('MDVP:PPQ')
    with col4:
        DDP=st.text_input('Jitter:DDP')	
    with col1:
        Shimmer=st.text_input('MDVP:Shimmer')	
    with col2:
        Shimmer_dB=st.text_input('MDVP:Shimmer(dB)')	
    with col3:
        APQ3=st.text_input('Shimmer:APQ3')	
    with col4 :
        APQ5=st.text_input('Shimmer:APQ5')	
    with col1:
        APQ=st.text_input('MDVP:APQ')
    with col2:
        DDA=st.text_input('Shimmer:DDA')	
    with col3:
        NHR	=st.text_input('NHR')
    with col4:
        HNR=st.text_input('HNR')
    with col1:
        RPDE = st.text_input('RPDE')	
    with col2:
        DFA = st.text_input('DFA')	
    with col3:
        spread1	=st.text_input('spread1')
    with col4:
        spread2	=st.text_input('spread2')
    with col1:
        D2=st.text_input('D2')	
    with col2:
        PPE=st.text_input('PPE')
       
        

    parkinson_diagnosis=''
     
    if st.button('Parkinson Disease Test Result'):
        parkinson_prediction= parkinson.predict([[Fo_Hz, Fhi_Hz, Flo_Hz, Jitter_percent, Jitter_Abs,RAP,PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,
                                                                               RPDE,DFA,spread1,spread2,D2,PPE]])
        if( parkinson_prediction[0] == 1):
                parkinson_diagnosis='the person is having  parkinson disease'
        else:
                parkinson_diagnosis='the person does not have  parkinson disease'
         
    st.success( parkinson_diagnosis)




#cancer disease

    
if (selected == 'cancer disease prediction'):
     
   st.title('cancer prediction using ML')
    
   col1,col2,col3,col4=st.columns(4)



   with col1:
         radius_mean=st.text_input('enter radius_mean')
   with col2:
         texture_mean=st.text_input('enter texture_mean')
   with col3:
         perimeter_mean=st.text_input('enter perimeter_mean')
   with col4:
         area_mean=st.text_input('enter area_mean')
   with col1:
         smoothness_mean=st.text_input('enter smoothness_mean') 
   with col2:
         compactness_mean=st.text_input('enter compactness_mean')     
   with col3:
         concavity_mean=st.text_input('enter concavity_mean')     
   with col4:
         concave_points_mean=st.text_input('enter concave_points_mean')     
   with col1:
         symmetry_mean=st.text_input('enter symmetry_mean')     
   with col2:
         fractal_dimension_mean=st.text_input('enter fractal_dimension_mean')     
   with col3:
         radius_se=st.text_input('enter radius_se')
   with col4:
         texture_se=st.text_input('enter texture_se"')                                       
   with col1:
         perimeter_se=st.text_input('enter perimeter_se')
   with col2:
        area_se=st.text_input('enter area_se')                                       
   with col3:
         smoothness_se=st.text_input('enter smoothness_se')                                       
   with col4:
         compactness_se=st.text_input('enter compactness_se')                                       
   with col1:
         concavity_se=st.text_input('enter concavity_se')                                       
   with col2:
         concave_points_se=st.text_input('enter concave_points_se')                                       
   with col3:
        symmetry_se =st.text_input('enter symmetry_se')                                       
   with col4:
         fractal_dimension_se=st.text_input('enter fractal_dimension_se')                                       
   with col1:
        radius_worst =st.text_input('enter radius_worst')
   with col2:
         texture_worst=st.text_input('enter texture_worst',key='texture_worst_input')                                                                                                                    
   with col3:
         perimeter_worst=st.text_input('enter perimeter_worst',key='perimeter_worst_input')
   with col4:
         area_worst=st.text_input('enter area_worst', key='area_worst_input')
   with col1:
         compactness_worst=st.text_input('enter compactness_worst', key='compactness_worst_input')         
   with col2:
         smoothness_worst=st.text_input('enter smoothness_worst',key='smoothness_worst_input')     
   with col3:
         concavity_worst=st.text_input('enter concavity_worst', key='concavity_worst_input')         
   with col4:
         concave_points_worst=st.text_input('enter concave_points_worst', key='cancacve_points_worst_input')         
   with col1:
        symmetry_worst=st.text_input('enter symmetry_worst', key='symetry_worst_input')         
   with col2:
         fractal_dimension_worst=st.text_input('enter fractal_dimension_worst', key='fractal_dimension_worst_input')         
   

        
        
   cancer_diagnosis=''
       
    
   if st.button('CANCER Test Result'):
        
       
        cancer_prediction = cancer.predict([[radius_mean,texture_mean,perimeter_mean,area_mean,
        smoothness_mean,compactness_mean,concavity_mean,concave_points_mean,symmetry_mean,fractal_dimension_mean,
        radius_se,texture_se,perimeter_se,area_se,smoothness_se,compactness_se,concavity_se,concave_points_se,symmetry_se,
        fractal_dimension_se,radius_worst,texture_worst,perimeter_worst,area_worst,smoothness_worst,compactness_worst
        ,concavity_worst,concave_points_worst,symmetry_worst,fractal_dimension_worst]])
        
        
        if( cancer_prediction[0] == 1):
              cancer_diagnosis='the person is Malignant'
        else:
              cancer_diagnosis='the person is benign'
       
   st.success( cancer_diagnosis)


    
      
          
    
        