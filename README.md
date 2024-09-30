## Sms-spam-classifier
This repository contains an SMS Spam Classifier that uses machine learning to predict whether a given SMS message is spam or not. The project covers the entire process from data cleaning to deployment.
# Introduction
The SMS Spam Classifier predicts whether an SMS is spam or not based on its text content. It uses machine learning models and natural language processing (NLP) techniques to achieve this. This project includes data cleaning, model training, evaluation, and deployment on a web platform.

# Dataset
The dataset is sourced from Kaggle. It consists of labeled SMS messages as either spam or ham (non-spam).
Here is the link of dataset i used for this project: 
https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset

# Steps
# 1. Data cleaning:
* Removed unnecessary columns and handled missing values.
* Dropped duplicate entries to ensure the dataset was clean.
* Renamed columns for clarity (v1 to target, v2 to message).
* Converted the target column (spam or ham) into numeric form using label encoding.


