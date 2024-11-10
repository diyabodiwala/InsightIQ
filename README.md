# InsightIQ

**InsightIQ** is an AI-powered data analysis tool that leverages large language models (LLMs) to provide actionable insights from complex datasets. Designed for intuitive interaction, InsightIQ allows users to query datasets in natural language, identify trends, and visualize patterns, making data-driven decisions faster and more accessible.

## Features

- **Natural Language Queries**: Ask questions directly about your data for instant insights.
- **Data Visualization**: Generate interactive visualizations for a more in-depth analysis.
- **Automated Insights**: Identify trends, patterns, and key metrics from raw data.
- **Real-time Analysis**: Process data quickly with OpenAI’s API for real-time insights.

## Technologies Used

- **Python**: Core programming for data processing.
- **Streamlit**: For the interactive web interface.
- **OpenAI API**: Powers natural language understanding and response generation.
- **Pandas**: Data manipulation and cleaning.
- **Matplotlib**: Data visualization.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/InsightIQ.git
    cd InsightIQ
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up your OpenAI API key:
    - Sign up on [OpenAI](https://platform.openai.com/) and obtain an API key.
    - Add your API key to `app.py`:
      ```python
      openai.api_key = "your-api-key"
      ```

4. Run the app:
    ```bash
    streamlit run app.py
    ```

## Usage

1. **Upload a CSV file**: Upload your dataset to start the analysis.
2. **Ask Questions**: Type in questions about trends, patterns, or metrics directly in the query box.
3. **View Insights and Visualizations**: See generated insights and visualizations in real-time.

## Example Queries

- "What are the main sales trends over the past year?"
- "Identify any seasonal patterns in customer purchases."
- "Summarize key insights about customer churn."

## Future Enhancements

- **Expanded Query Capabilities**: Support more complex, multi-dataset queries.
- **Advanced Visualizations**: Integrate more sophisticated data visualizations.
- **Real-Time Data Integration**: Enable continuous data updates and monitoring.

## License

This project is licensed under the MIT License.
