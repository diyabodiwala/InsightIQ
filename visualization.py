import matplotlib.pyplot as plt
import streamlit as st

def plot_histogram(df, column):
    fig, ax = plt.subplots()
    df[column].hist(bins=20, ax=ax)
    ax.set_title(f"Histogram of {column}")
    ax.set_xlabel(column)
    ax.set_ylabel("Frequency")
    st.pyplot(fig)

def plot_bar_chart(df, column):
    fig, ax = plt.subplots()
    df[column].value_counts().plot(kind='bar', ax=ax)
    ax.set_title(f"Bar Chart of {column}")
    ax.set_xlabel(column)
    ax.set_ylabel("Count")
    st.pyplot(fig)
