import openai
import pandas as pd
import streamlit as st
from data_utils import load_data, clean_data, select_columns
from visualization import plot_histogram, plot_bar_chart

# Load OpenAI API Key (replace 'your-api-key' with your actual API key)
openai.api_key = "your-api-key"

st.title("Advanced LLM-Powered Data Analysis")
st.write("Upload a CSV file, clean data, visualize, and analyze with LLM integration.")

# Step 1: Data Upload and Cleaning Options
uploaded_file = st.file_uploader("Upload CSV file", type="csv")
if uploaded_file:
    df = load_data(uploaded_file)
    st.write("Data Preview:")
    st.dataframe(df.head())

    # Data Cleaning
    st.subheader("Data Cleaning")
    fill_method = st.selectbox("Handle Missing Values By:", ["mean", "median", "drop", "none"])
    if fill_method != "none":
        df = clean_data(df, fill_method)

    # Column Selection for Analysis
    st.subheader("Column Selection")
    columns = st.multiselect("Select columns for analysis", df.columns.tolist(), default=df.columns.tolist())
    if columns:
        df = select_columns(df, columns)
        st.write("Updated Data Preview:")
        st.dataframe(df.head())

        # Step 2: Visualization
        st.subheader("Data Visualization")
        chart_type = st.selectbox("Choose Chart Type", ["Histogram", "Bar Chart"])
        column_to_plot = st.selectbox("Select Column for Visualization", columns)
        if chart_type == "Histogram":
            plot_histogram(df, column_to_plot)
        elif chart_type == "Bar Chart":
            plot_bar_chart(df, column_to_plot)

        # Step 3: LLM Query Input
        st.subheader("Ask a Question")
        query = st.text_input("Ask a question related to your data:")
        if query:
            # Prepare the prompt for the LLM
            data_sample = df.head(10).to_string()  # Limiting data sample size for prompt efficiency
            prompt = f"Here is a data sample:\n{data_sample}\n\nAnalyze this dataset and answer the query: {query}"

            # Call OpenAI API
            try:
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=prompt,
                    max_tokens=200,
                    temperature=0.5
                )
                answer = response.choices[0].text.strip()
                st.write("LLM Response:", answer)
            except Exception as e:
                st.write("An error occurred:", e)
