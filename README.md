# Sms-spam-classifier
This repository contains an SMS Spam Classifier that uses machine learning to predict whether a given SMS message is spam or not. The project covers the entire process from data cleaning to deployment.
## Introduction
The SMS Spam Classifier predicts whether an SMS is spam or not based on its text content. It uses machine learning models and natural language processing (NLP) techniques to achieve this. This project includes data cleaning, model training, evaluation, and deployment on a web platform.

## Dataset
The dataset is sourced from Kaggle. It consists of labeled SMS messages as either spam or ham (non-spam).
Here is the link of dataset i used for this project: 
https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset

## Steps
# 1.Data cleaning:
* Removed unnecessary columns and handled missing values.
* Dropped duplicate entries to ensure the dataset was clean.
* Renamed columns for clarity (v1 to target, v2 to message).
* Converted the target column (spam or ham) into numeric form using label encoding.

# 2. Exploratory Data Analysis (EDA)
* Analyzed the distribution of spam vs. ham messages.
* Investigated common word usage patterns in both spam and ham messages.
* Explored message lengths and their impact on classification.

# 3. Text Preprossing
* Tokenized the text messages and removed common stopwords.
* Performed lemmatization to reduce words to their base forms.
* Vectorized the messages using Term Frequency-Inverse Document Frequency (TF-IDF) for input to machine learning models.

# 4. Model Building
Trained multiple machine learning models including:
* Naive Bayes
* Support Vector Machines (SVM)
* Random Forest

# 5. Evaluation
Evaluated the models using standard classification metrics:
* Accuracy
* Precision
* Recall

# 6. Website and Deployment
* Built a web interface using Flask where users can input SMS messages to classify them as spam or ham.
* Deployed the application on Heroku for public access.





