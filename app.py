import streamlit as st # type: ignore
import pickle
import string
from  nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()
def transform_text_data(text):
    # making our text lowercase
    text = text.lower()
    
    # Tokenization of our data
    text = nltk.word_tokenize(text)

    y = []
    # removing special characters and punctuation
    for i in text:
        if i.isalnum():
            y.append(i)
    text = y[:]
    y.clear()
    for i in text:
        if i not in stopwords.words("english") and i not in string.punctuation:
            y.append(i)
    text = y[:]
    # stemmer
    y.clear()
    for i in text:
        y.append(ps.stem(i))
        
    text = y[:]
    
    return " ".join(text)

tfidf = pickle.load(open("vectorizer.pkl", "rb"))
model = pickle.load(open("model.pkl", "rb"))
st.title("Spam Or not a Spam")

input_sms = st.text_area("Enter the Message: ")

if st.button("Predict"):
    # preprocess
    transformed_sms = transform_text_data(input_sms)

    #vectorize
    vector_input = tfidf.transform([transformed_sms])

    # predict
    result = model.predict(vector_input)[0]

    # Display
    if result == 1:
        st.header("It's a Spam. Be carefull.", divider = True)
    else:
        st.header("it's not a Spam", divider = True)



