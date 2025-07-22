# Spam-Message-Detection
This project is a machine learning-based web app that classifies text messages (like emails or SMS) as Spam or Not Spam. It uses Natural Language Processing (NLP) techniques to preprocess the text and a trained classifier to predict the message category.

# Key Features
 --Input any message through a simple Streamlit web app

 --Text preprocessing using nltk (stopword removal, stemming, etc.)

-- Custom function (transform_text) for cleaning input text

 --Feature extraction using TF-IDF Vectorizer

 Trained classification model (e.g., Naive Bayes / SVM / Logistic Regression)

--High accuracy on detecting spam vs. ham (non-spam)

# Tools & Libraries Used Python

-NLTK for text preprocessing

--Scikit-learn for machine learning models

--TF-IDF for converting text to numerical features

--Streamlit for deploying the app

--Pickle & Dill for saving/loading models and functions

# Workflow

--Text Input: User enters a message.

--Preprocessing: Custom transform_text function applies NLP cleaning.

--Vectorization: TF-IDF converts cleaned text into numerical form.

--Prediction: Trained model predicts whether it's Spam or Not Spam.

--Result Display: Output is shown on the web page.
