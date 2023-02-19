import streamlit as st
import pickle
import numpy as np
import pandas as pd

st.title('Bank Customer Churn Prediction')

def churn_pred(pred_input):
    
    pickled_model = pickle.load(open('model.pkl', 'rb'))
    pickled_scaler = pickle.load(open('scaler.pkl', 'rb'))
    
    
    feature_columns = ['credit_score', 'country', 'gender', 'age', 'tenure', 'balance','products_number', 'credit_card','active_member', 'estimated_salary']
    
    df_input = pd.DataFrame([pred_input], feature_columns)  
    
    scale_input = pickled_scaler.transform(df_input)
    
    df_scale = pd.DataFrame(scale_input, feature_columns) 
     
    prediction = pickled_model.predict(df_scale)
    
    return prediction
    

def main():
    st.sidebar.info('Created By: P. KOMAL SAI ANURAG')
    st.sidebar.image('https://s16353.pcdn.co/wp-content/uploads/2018/06/Churn.png')
    st.sidebar.subheader("Github repositorty of the the project : ")


    
    st.subheader("Enter the details of the customer")
    
    col1, col2 = st.columns(2)
    
    col3,col4 = st.columns(2)
    
    col5,col6 = st.columns(2)
    
    with col1:
        g = st.selectbox('Select the Gender', ['Select','Male', 'Female'])
        
        if(g == "Male"):
            gender = 0
        else:
            gender = 1
    
    with col2:
        c = st.selectbox('Select a country', ['Select','France', 'Spain','Germany'])
        
        if(c == 'France'):
            country = 0
        elif(c == 'Germany'):
            country = 1
        else:
            country = 2
        
    with col1:
        age = st.number_input('Enter the Age',0,100,0,1,'%d')
        
    with col2:
        tenure = st.number_input('Number of Year as a Customer',0,50,0,1,'%d')
        
    with col3:
        credit_score = st.number_input('Enter the Credit Score',0,2000,0,1,'%d')
        
    with col4:
        balance = st.number_input('Enter the Account Balance',0,1000000,0,5000,'%d')
        
    with col3:
        product_number = st.number_input('Enter number of Products',0,20,0,1,'%d')
        
    with col4:
        credit_card = st.selectbox('Customer has an Credit card or not', ['Select','Yes', 'No'])
        
        if(credit_card == 'Yes'):
            card = 1
        else:
            card = 0
        
    with col5:
        bank_member = st.selectbox('Is Customer an active Bank Member', ['Select','Yes', 'No'])
        
        if(bank_member == 'Yes'):
            active = 1
        else:
            active = 0
        
    with col6:
        salary = st.number_input('Enter the Estimated Salary',0,1000000,0,5000,'%d')
    
    
    button = st.button("Predict")
    
    if button:
        
        input_churn = np.array([credit_score,country,gender,age,tenure,balance,product_number,card,active,salary])
        
        prediction = churn_pred(input_churn)
        
        if(prediction.all() == 1):
            st.subheader("Churn")
            
        else:
            st.subheader("No Churn")        
        

        
if __name__ == '__main__':
    main()