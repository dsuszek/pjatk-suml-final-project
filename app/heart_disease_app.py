"""
Heart Disease Evaluation App

This module implements a web application using Streamlit
that allows users to assess their risk of having
coronary heart disease (CHD) or myocardial infarction (MI)
based on a variety of personal health indicators.

Functions:
- get_input_from_user(): Collects input data from the user.
- display_user_inputs(df): Displays the user inputs.

Application Flow:
1. Load the pre-trained model.
2. Define the column names for the input DataFrame.
3. Set up the Streamlit app interface,
   including the title, image, and introductory text.
4. Collect user input parameters through the sidebar interface.
5. Display the collected user input parameters in expandable sections.
6. When the user clicks the 'Predict' button,
   use the pre-trained model to make predictions and display the results.

Usage:
To run the app, execute the script using a Streamlit command such as:
    streamlit run path_to_this_script.py
"""

import time

import joblib
import pandas as pd
import streamlit as st

# Load the pre-trained model
model = joblib.load('model/model_rfc.joblib')

# Define the column names
columns = [
    'HeartDisease', 'BMI', 'Smoking', 'AlcoholDrinking', 'Stroke',
    'PhysicalHealth', 'MentalHealth', 'DiffWalking', 'Sex', 'AgeCategory',
    'Race', 'Diabetic', 'PhysicalActivity', 'GenHealth', 'SleepTime',
    'Asthma', 'KidneyDisease', 'SkinCancer'
]

st.title('Heart Disease Evaluation App')
st.image(
    "https://assets.clevelandclinic.org/transform/LargeFeatureImage/"
    "1b3152fa-e4e8-49fc-98b4-b4e9d6dc1422/HeartDiseaseFactors-1345978894-770x533-1_jpg",
    use_column_width=True)
st.markdown("""
<style>
.intro-text {
    font-size: 16px;
    line-height: 1.5;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="intro-text">Heart Disease Risk Evaluation app is a '
            'user-friendly tool designed to help individuals assess their '
            'risk of having coronary heart disease (CHD) or '
            'myocardial infarction (MI) based on a variety of personal health indicators.</div>',
            unsafe_allow_html=True)

st.sidebar.header('User Input Parameters')


def get_input_from_user():
    """
    Collects input data from the user and returns it as a DataFrame.

    Returns:
        pd.DataFrame: A DataFrame containing user input data.
    """
    with st.sidebar.expander("General information"):
        sex = st.selectbox('Sex', [0, 1], format_func=lambda x: 'Male' if x == 1 else 'Female')
        age_category = st.selectbox(
            'Age Category', list(range(1, 14)), format_func=lambda x: f'Category {x}'
        )
        race = st.selectbox(
            'Race', list(range(1, 6)), format_func=lambda x: f'Race {x}'
        )
        bmi = st.slider('Body Mass Index (BMI)', 10.0, 50.0, 25.0)
        gen_health = st.selectbox(
            'Would you say that in general your health is...', list(range(1, 6)),
                                          format_func=lambda x: f'Health Level {x}')

    with st.sidebar.expander("Addictions"):
        smoking = st.selectbox(
            'Have you smoked at least 100 cigarettes in your entire life?', [0, 1],
                                       format_func=lambda x: 'Yes' if x == 1 else 'No')
        alcohol_drinking = st.selectbox('Do you drink alcohol regularly?', [0, 1],
                                            format_func=lambda x: 'Yes' if x == 1 else 'No')

    with st.sidebar.expander("Medical history"):
        stroke = st.selectbox('Have you ever had a stroke?', [0, 1],
                                      format_func=lambda x: 'Yes' if x == 1 else 'No')
        diabetic = st.selectbox(
            'Are you diabetic?', [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
        asthma = st.selectbox(
            'Do you have asthma?', [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
        kidney_disease = st.selectbox(
            'Do you have any kidney disease?',
            [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
        skin_cancer = st.selectbox('Do you have skin cancer?', [0, 1],
                                           format_func=lambda x: 'Yes' if x == 1 else 'No')

    with st.sidebar.expander("Current health status"):
        physical_health = st.slider('Physical Health (days with poor health)', 0, 30, 0)
        mental_health = st.slider('Mental Health (days with poor health)', 0, 30, 0)
        diff_walking = st.selectbox('Do you have difficulty walking?', [0, 1],
                                            format_func=lambda x: 'Yes' if x == 1 else 'No')

    with st.sidebar.expander("Way of life"):
        physical_activity = st.selectbox(
            'Do you engage in physical activity other than your regular job?', [0, 1],
                                                 format_func=lambda x: 'Yes' if x == 1 else 'No')
        sleep_time = st.slider('Sleep Time (hours) in a 24-hour period', 0, 24, 8)

    data = {
        'BMI': bmi,
        'Smoking': smoking,
        'AlcoholDrinking': alcohol_drinking,
        'Stroke': stroke,
        'PhysicalHealth': physical_health,
        'MentalHealth': mental_health,
        'DiffWalking': diff_walking,
        'Sex': sex,
        'AgeCategory': age_category,
        'Race': race,
        'Diabetic': diabetic,
        'PhysicalActivity': physical_activity,
        'GenHealth': gen_health,
        'SleepTime': sleep_time,
        'Asthma': asthma,
        'KidneyDisease': kidney_disease,
        'SkinCancer': skin_cancer
    }

    features = pd.DataFrame(data, index=[0])
    return features


df = get_input_from_user()

st.subheader('User Input Parameters')

# Display input parameters in expanders
with st.expander("General information"):
    st.write(f"**Sex**: {df['Sex'][0]}")
    st.write(f"**Age Category**: {df['AgeCategory'][0]}")
    st.write(f"**Race**: {df['Race'][0]}")
    st.write(f"**BMI**: {df['BMI'][0]}")
    st.write(f"**General Health**: {df['GenHealth'][0]}")

with st.expander("Addictions"):
    st.write(f"**Smoking**: {'Yes' if df['Smoking'][0] == 1 else 'No'}")
    st.write(f"**Alcohol Drinking**: {'Yes' if df['AlcoholDrinking'][0] == 1 else 'No'}")

with st.expander("Medical history"):
    st.write(f"**Stroke**: {'Yes' if df['Stroke'][0] == 1 else 'No'}")
    st.write(f"**Diabetic**: {'Yes' if df['Diabetic'][0] == 1 else 'No'}")
    st.write(f"**Asthma**: {'Yes' if df['Asthma'][0] == 1 else 'No'}")
    st.write(f"**Kidney Disease**: {'Yes' if df['KidneyDisease'][0] == 1 else 'No'}")
    st.write(f"**Skin Cancer**: {'Yes' if df['SkinCancer'][0] == 1 else 'No'}")

with st.expander("Current health status"):
    st.write(f"**Physical Health**: {df['PhysicalHealth'][0]}")
    st.write(f"**Mental Health**: {df['MentalHealth'][0]}")
    st.write(f"**Difficulty Walking**: {'Yes' if df['DiffWalking'][0] == 1 else 'No'}")

with st.expander("Way of life"):
    st.write(f"**Physical Activity**: {'Yes' if df['PhysicalActivity'][0] == 1 else 'No'}")
    st.write(f"**Sleep Time (hours)**: {df['SleepTime'][0]}")

if st.button('Predict'):
    with st.spinner('Calculating...'):
        time.sleep(1)

        # Make predictions
        prediction = model.predict(df)
        prediction_proba = model.predict_proba(df)

        # Display the result of prediction
        st.subheader('Prediction')
        st.write('Positive' if prediction[0] == 1 else 'Negative')

        # Display the probabilities of being positive and negative
        st.subheader('Prediction Probability')
        st.write(f'Probability of being positive: {prediction_proba[0][1]:.2f}')
        st.write(f'Probability of being negative: {prediction_proba[0][0]:.2f}')
