## CODRELATE 2025 - AI-Powered Content Analysis and Recommendation

## Project Overview

This project is developed as part of the CODRELATE-2025 Hackathon under the track "AI-powered Content Analysis and Recommendation". Our solution provides a machine learning pipeline to predict content tags based on news articles using NLP techniques and builds a user-friendly frontend for interactive predictions.

## Problem Statement

Given a dataset of news articles containing title, text, authors, tags, and timestamp, the task is to:

Analyze and preprocess the content

Predict relevant tags for a given article

Build an innovative frontend for interaction

## Dataset Description

File: AI-Powered Content Analysis and Recommendation.csv

Columns: title, text, url, authors, timestamp, tags

Size: 192,368 articles

## Approach

1. Preprocessing

Text cleaning: Lowercasing, punctuation removal, stopword removal

Tags cleaning: Removing empty/missing tags, multi-label encoding

2. Feature Extraction

TF-IDF Vectorization on cleaned text

3. Model Training

Multi-label classification using Logistic Regression with OneVsRestClassifier

Evaluation metrics: Hamming loss, precision, recall, F1-score

4. Frontend

Built using Gradio

Users can input an article and get predicted tags

## Technologies Used

Python

Scikit-learn

Pandas / NumPy

NLTK

Gradio

## Innovation

User-friendly Gradio app for predictions

Focus on multi-label learning with scalable preprocessing

Explains which tags are predicted and their confidence

## Model Performance

Metric

Score

Hamming Loss

~0.08

Precision (macro avg)

~0.81

Recall (macro avg)

~0.78

F1-score (macro avg)

~0.79

## Folder Structure

├── app/
│   └── gradio_ui.py
├── data/
│   └── AI-Powered_Content_Cleaned.csv
├── models/
│   └── tfidf_vectorizer.pkl
│   └── classifier_model.pkl
│   └── multilabel_binarizer.pkl
├── notebooks/
│   └── EDA_and_Model_Training.ipynb
├── screenshots/
│   └── ui_screenshot.png
├── README.md
├── requirements.txt

## How to Run

Clone the repo:

>> git clone https://github.com/ShaikJasmin11/CodeCrafters_Round2.git

Install dependencies:

>> pip install -r requirements.txt

Run the app:

>> python app/gradio_ui.py

## Team Members

Shaik Jasmin

Sravani Somayagari.

## Final Notes

We believe this project will be impactful for digital publishers and content platforms to enhance content tagging and personalized recommendations.
