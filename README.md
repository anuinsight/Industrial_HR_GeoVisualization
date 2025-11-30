Industrial Human Resource Geo-Visualization Dashboard
Project Overview

This project analyzes the distribution and composition of India's industrial workforce using data preprocessing, NLP techniques, machine learning, and geo-visualization. The aim is to provide actionable insights into workforce distribution by state, industry, gender, and rural/urban status and to categorize industries into meaningful groups using both rule-based and machine learning approaches.

The final output is an interactive Streamlit dashboard with exploratory data analysis (EDA) and geo-visualization features.

Problem Statement

India has a large and diverse industrial workforce spread across multiple states and sectors.

Workforce data is often scattered in multiple CSV files, with missing and inconsistent values.

Industry names are unstructured, making classification and insights challenging.

Decision-makers need a centralized, visual, and interactive tool to analyze workforce data effectively.

Objectives

Merge multiple CSV files containing state-wise industrial workforce data.

Clean and preprocess the data (handle missing values, duplicates, and inconsistent names).

Categorize industries using rule-based and ML-based NLP techniques.

Generate EDA insights: top industries, top states, gender distribution, rural vs urban workforce.

Build an interactive Streamlit dashboard with geo-visualization of workforce metrics.

Tools & Libraries Used

Languages: Python

Data Processing:

pandas, numpy, re

NLP & Machine Learning:

nltk, TfidfVectorizer, KMeans, UMAP, RandomForestClassifier, TruncatedSVD

Visualization:

plotly, matplotlib, seaborn, wordcloud

Dashboard:

streamlit

Environment:

Google Colab (data preprocessing)

GitHub (project versioning)

Approach
1. Data Preprocessing

Upload and merge multiple state-wise CSV files.

Add State and Source_File columns for better tracking.

Fill missing values and remove duplicates.

2. Exploratory Data Analysis (EDA)

Calculate total workers per industry, state, and division.

Analyze gender distribution (male vs female).

Analyze rural vs urban workforce ratio.

Generate heatmaps, bar charts, and pie charts.

3. NLP-Based Industry Grouping

Clean and lemmatize industry names.

Apply rule-based keyword matching for known industry types.

Use TF-IDF + KMeans + UMAP for clustering uncategorized industries.

Combine both approaches for final industry group classification.

4. Machine Learning Classification

Train a Random Forest Classifier on the labeled industry data.

Predict industry groups for unknown entries.

Save model and vectorizer for future use.

5. Geo-Visualization

Build interactive choropleth maps for Indian states.

Display workforce metrics by state using Plotly.

Integrate all visualizations into a Streamlit dashboard.

EDA Insights

Top Industries: Manufacturing, Construction, Retail.

Top States: States with the highest industrial workforce identified.

Gender Distribution: Insights into male and female workers.

Rural vs Urban: Majority of workforce resides in rural areas.

Industry Clusters: Distinct clusters identified using NLP and ML techniques.

Word Cloud: Most common keywords in industry names visualized.

Streamlit Dashboard Features

CSV Upload: Upload multiple state CSV files at once.

Smart Column Search: Search for columns with keywords.

Numeric Visualizations: Histograms and summary statistics for numeric columns.

Geo-Visualization: Choropleth maps showing workforce metrics across states.

Interactive Filtering: Filter data by industry group, gender, rural/urban.

File Structure
project/
│
├── merged_with_industry_group.csv   # Preprocessed & labeled dataset
├── Industrial_HR_Geo_Visualization.pptx   # Auto-generated PowerPoint slides
├── industry_classifier.joblib       # Trained ML model
├── tfidf_vectorizer.joblib          # TF-IDF vectorizer
├── app.py                           # Streamlit dashboard script
├── README.md                        # Project documentation
└── requirements.txt                 # Required Python libraries

How to Run the Dashboard

Install required packages:

pip install -r requirements.txt


Run Streamlit app:

streamlit run app.py


Upload your CSV files when prompted and explore EDA & geo-visualizations.

Future Enhancements

Include more recent workforce data.

Predict future workforce trends using ML models.

Add district-level geo-visualizations.

Enable advanced filtering by multiple metrics simultaneously.

Incorporate interactive dashboards with drill-down capabilities.

Author

Name: Anupriya R

LinkedIn: https://www.linkedin.com/in/anupriya-anupriya-391072257

GitHub: https://github.com/anuinsight/Industrial_HR_GeoVisualization
