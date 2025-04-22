import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Employee Workload Forecaster")

uploaded_file = st.file_uploader("Upload Task CSV", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Raw Data", df.head())

    if all(col in df.columns for col in ['Owner', 'Estimated Hours']):
        workload = df.groupby("Owner")["Estimated Hours"].sum().reset_index()
        fig = px.bar(workload, x="Owner", y="Estimated Hours", title="Total Estimated Hours by Owner")
        st.plotly_chart(fig)
    else:
        st.warning("Missing 'Owner' or 'Estimated Hours' columns in CSV.")
