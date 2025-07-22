import streamlit as st
import pickle
import dill
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import string
ps = PorterStemmer()



tfidf=pickle.load(open('vectorizer.pkl','rb'))
model=pickle.load(open('model.pkl','rb')) # file will not close automatically
st.title("Email/SMS Classifier" )
with open('transform_text.pkl', 'rb') as f:
    transform_text = dill.load(f) #  creates a context manager and it close  file . So here will close automatically

input_sms=st.text_area("Enter the message")




# preprocess
transform_sms_preprocess=transform_text(input_sms)
# vectorize
vector_input=tfidf.transform([transform_sms_preprocess]) # calling the transform function using the object
#predict
result=model.predict(vector_input)[0]
#display
if st.button('Predict'):
    if result==1:
        st.header("Spam")
    else:
        st.header("Not Spam")