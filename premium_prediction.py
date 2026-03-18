import streamlit as st
import pandas as pd
import joblib


model = joblib.load("premium_prediction.pkl")    

st.title ("Premium Prediction App")

st.markdown("Please enter the following below and use the prediction button")

st.divider()

st.markdown("Vehicle Information")

TYPE_VEHICLE = st.selectbox("TYPE_VEHICLE",["Pick up","Station Wagones","Truck","Bus","Automobile","Tanker","Trailers and semitrailers"
                             ,"Motor-cycle","Tractor","Special construction","Trade plates"])
INSURED_VALUE = st.number_input("INSURED_VALUE",min_value=0,value=0)
PROD_YEAR = st.number_input("PROD_YEAR",min_value=0,value=0)


st.markdown("Policy Information")

Insurance_type = st.selectbox("Insurance_type",["private","commercial","motor trade road risk"])
USAGE=st.selectbox("USAGE",["Own Goods","Private","General Cartage","Taxi","Car Hires","Own service","Agricultural Own Farm","Special Construction","Others",
                   "Learnes","Ambulance","Agricultural Any Farm","Fire fighting"])


st.markdown("Driver infomation")

Gender = st.selectbox("Gender",["male","female","legal entity"])

st.markdown("Claims Information")

CLAIM_PAID = st.number_input("CLAIM_PAID",min_value=0,value=0)

st.divider()

if st.button("Predict"):
    input_data =pd.DataFrame([{
        "TYPE_VEHICLE":TYPE_VEHICLE,
        "USAGE": USAGE,
        "INSURED_VALUE": INSURED_VALUE,
        "PROD_YEAR": PROD_YEAR,
        "CLAIM_PAID": CLAIM_PAID,
        "Gender":Gender,
        "Insurance_type":Insurance_type
    }])
   
    prediction = model.predict(input_data)
    st.success(f"Predicted Premium: {prediction[0]:,.2f}")
    

