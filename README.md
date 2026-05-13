# Intelligent Drug Recommendation System using Machine Learning and NLP

## Project Overview
The Intelligent Drug Recommendation System is an AI-powered healthcare application that recommends suitable medicines based on patient reviews, ratings, sentiment analysis, and drug popularity.

The system analyzes real patient experiences and recommends the most effective medicines for different medical conditions using Machine Learning and Natural Language Processing (NLP).

---

# What I Did in This Project

## Data Understanding
- Analyzed dataset structure and features
- Identified missing values and datatypes
- Understood review, rating, and condition relationships

---

# Data Cleaning
- Handled missing values
- Filled missing condition values using drug names
- Removed duplicates
- Converted date column into datetime format

---

# Exploratory Data Analysis (EDA)
Performed:
- Rating distribution analysis
- Useful review analysis
- Top medical conditions analysis
- Most reviewed drugs analysis
- Correlation analysis
- Univariate, Bivariate, and Multivariate EDA

---

# NLP Processing
Applied NLP techniques such as:
- Lowercasing
- Removing special characters
- Stopword removal
- Text cleaning
- Sentiment analysis using TextBlob
- TF-IDF vectorization
- N-gram feature extraction

---

# Feature Engineering
Created features like:
- Review length
- Word count
- Character count
- Sentence count
- Sentiment score
- Drug popularity
- Condition frequency
- Average drug rating
- Useful review classification

---

# Machine Learning
Built and evaluated multiple ML models:
- Logistic Regression
- XGBoost
- Linear SVM

Best model accuracy achieved:

76.35%

---

# Recommendation Engine
Developed intelligent drug ranking logic using:
- Drug ratings
- Sentiment scores
- Useful review count
- Drug popularity

The system recommends top medicines for a given medical condition.

---

# Streamlit Dashboard
Developed and deployed an interactive Streamlit dashboard where users can:
- Enter medical conditions
- View recommended medicines
- Compare ratings and sentiment scores

---

# Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- NLTK
- TextBlob
- Scikit-learn
- XGBoost
- SVM
- Streamlit

---

# Project Structure

```text
drug_project/
│
├── app.py
├── recommendation_data.csv
├── requirements.txt
├── Intelligent Drug Recommendation System using Machine Learning and NLP.ipynb
└── README.md
---
## ⚙️ Installation

```bash
pip install -r requirements.txt
streamlit run app.py
```
# Can see my streamlit
```
```
https://57tnsvzzgnyatgcdka2hrw.streamlit.app/
```
```
<img width="1920" height="1080" alt="Screenshot (36)" src="https://github.com/user-attachments/assets/eb483381-2b5b-41cf-9537-7cd48f829da4" />
"
<img width="1920" height="1080" alt="Screenshot (35)" src="https://github.com/user-attachments/assets/ba16a83e-f13b-4784-880e-00b2f03ee133" />
"
<img width="1920" height="1080" alt="Screenshot (37)" src="https://github.com/user-attachments/assets/ac8b54c0-aa84-498b-b61e-9f1aab3c7ead" />
```
