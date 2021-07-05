import streamlit as st
# streamlit package in venk environment variable inside virtualenv folder
st.title("Streamlit example")

st.write(""" Explore different classifier which one is the best""")
dataset_name=st.sidebar.selectbox("Select Dataset",("iris","Breast Cancer", "wine"))
classifier_name=st.sidebar.selectbox("Select classifier",("KNN","SVM", "Random Forest"))
print(dataset_name)