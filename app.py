import streamlit as st
import joblib
import os
from sklearn.preprocessing import LabelEncoder
logreg = joblib.load(open(os.path.join("logreg.pkl"),"rb"))


form = st.container()
header =  st.container()
classify = st.container()
with header:
    title  = st.header("Salary Prediction")
with form:  
    sno = st.number_input("S No.")
    gender = st.selectbox('Gender : 0 = Female , 1 = Male', (0, 1))
    ssc_p =  st.number_input("12th % : ")
    ssc_b = st.selectbox("12th Board : 0 = Central , 1 = Others " , (0 , 1))
    hsc_p = st.number_input("10th % : ")
    hsc_b = st.selectbox("10th Board : 0 = Central , 1 = Others ",(0, 1))
    stream = st.selectbox("Stream : 0 = Commerce , 1 =  Science , 2 = Arts" ,(0,1,2))
    degree_p =  st.number_input("Degree %")
    degree = st.selectbox("Degree : 0 - Comm&Mgmt , 1 - Others , 3 - Sci&Tech" ,(0,1,2))
    workex =  st.selectbox("Work Exp : 0 - No , 1 - Yes", (0,1))
    etest_p = st.number_input("Eligiblity Test Score")
    spc = st.selectbox("MBA Specialisation : 0 - Mkt&Fin , 1 - Mkt&Hr" , (0,1))
    mba_p = st.number_input("MBA %")

input = [[sno , gender,ssc_p,ssc_b,hsc_p,hsc_b,stream,degree_p,degree,workex,etest_p,spc,mba_p]]
# le = LabelEncoder()
# for i in input:
#     if (input[i].dtypes == str):
#         input = le.fit_transform(input[i])




with classify:
    if st.button("Classify"):
        prediction = logreg.predict(input)
        if prediction == [0]:
            st.success("Placed")
        else:
            st.error("Not Placed")

        


    