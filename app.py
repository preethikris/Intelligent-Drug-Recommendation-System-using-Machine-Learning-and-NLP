import streamlit as st
import pandas as pd

# Load recommendation data
df = pd.read_csv('recommendation_data.csv')

# Title
st.title("Intelligent Drug Recommendation System")

st.write(
    "Find the best medicines based on patient reviews, ratings, and sentiment analysis."
)

# User input
condition = st.text_input(
    "Enter Medical Condition"
)

# Recommendation logic
if condition:

    filtered = df[
        df['condition'].str.lower() == condition.lower()
    ]

    if len(filtered) > 0:

        recommendations = filtered.sort_values(
            by='recommendation_score',
            ascending=False
        ).head(5)

        st.subheader("Top Recommended Medicines")

        st.dataframe(
            recommendations[
                [
                    'drugName',
                    'rating',
                    'sentiment',
                    'usefulCount',
                    'recommendation_score'
                ]
            ]
        )

    else:
        st.warning("No medicines found for this condition.")