import streamlit as st
import pandas as pd
import plotly.express as px
import re
import json
import requests

# -------------------------------
# APP TITLE
# -------------------------------
st.title("📊 Industrial Human Resource Geo-Visualization Dashboard")
st.write("Analyze India's Industrial Workforce using NLP, EDA, and Geo-Visualization")

# -------------------------------
# FILE UPLOAD
# -------------------------------
uploaded_files = st.file_uploader(
    "Upload All State CSV Files",
    type="csv",
    accept_multiple_files=True
)

final_df = pd.DataFrame()

if uploaded_files:
    st.info("Reading & merging CSV files...")

    for file in uploaded_files:
        try:
            temp = pd.read_csv(file, encoding="utf-8")
        except UnicodeDecodeError:
            try:
                temp = pd.read_csv(file, encoding="ISO-8859-1")
            except Exception as e:
                st.error(f"Error reading {file.name}: {e}")
                continue

        # -------------------------------------------
        # EXTRACT STATE NAME FROM FILE NAME
        # -------------------------------------------
        clean_name = file.name.upper()
        match = re.search(r"STATE_([A-Z_]+)-?2011", clean_name)

        if match:
            state_name = match.group(1).replace("_", " ").title()
        else:
            state_name = "Unknown"

        temp["State"] = state_name  # <-- ADD STATE COLUMN HERE
        # -------------------------------------------

        final_df = pd.concat([final_df, temp], ignore_index=True)

    st.success("Files uploaded and merged successfully!")
    st.subheader("Preview of Merged Data")
    st.dataframe(final_df.head())

# -------------------------------
# NLP COLUMN EXTRACTION
# -------------------------------
if not final_df.empty:
    st.subheader("🔍 NLP Feature: Smart Column Search")
    user_query = st.text_input("Enter a keyword (ex: 'Main Workers', 'Urban', 'Females')")

    if user_query:
        pattern = re.compile(user_query, re.IGNORECASE)
        matched_cols = [col for col in final_df.columns if pattern.search(col)]
        st.write("### Matching Columns:")
        st.write(matched_cols if matched_cols else "No matching columns found")

# -------------------------------
# EDA SECTION
# -------------------------------
if not final_df.empty:
    st.subheader("📈 Exploratory Data Analysis")
    numeric_cols = final_df.select_dtypes(include=['int64', 'float64']).columns.tolist()

    if numeric_cols:
        column = st.selectbox("Select a numeric column to visualize", numeric_cols)
        fig = px.histogram(final_df, x=column, nbins=40, title=f"Distribution of {column}")
        st.plotly_chart(fig)
        st.write("### Summary Statistics")
        st.write(final_df[column].describe())

# -------------------------------
# GEO-VISUALIZATION SECTION
# -------------------------------
if not final_df.empty:
    st.subheader("🗺 Geo Visualization (Requires 'State' column)")
    possible_state_cols = [col for col in final_df.columns if 'state' in col.lower()]

    if possible_state_cols:
        state_col = st.selectbox("Select State Column", possible_state_cols)
        value_cols = final_df.select_dtypes(include=['int64', 'float64']).columns.tolist()
        metric = st.selectbox("Select Metric to Plot", value_cols)

        st.write("### Choropleth Map")

        # Load India states GeoJSON
        url = "https://raw.githubusercontent.com/geohacker/india/master/state/india_telengana.geojson"
        # You can replace above with a full India GeoJSON for all states
        try:
            india_geojson = requests.get(url).json()
        except Exception as e:
            st.error(f"Error loading India GeoJSON: {e}")
            india_geojson = None

        if india_geojson:
            fig = px.choropleth(
                final_df,
                geojson=india_geojson,
                locations=state_col,
                color=metric,
                featureidkey="properties.ST_NM",  # GeoJSON state property
                projection="mercator",
                title=f"{metric} by State"
            )
            fig.update_geos(fitbounds="locations", visible=False)
            st.plotly_chart(fig)
        else:
            st.warning("GeoJSON not loaded. Cannot display map.")
    else:
        st.warning("No state column found. Please verify the state column name.")

# -------------------------------
# END OF APP
# -------------------------------


