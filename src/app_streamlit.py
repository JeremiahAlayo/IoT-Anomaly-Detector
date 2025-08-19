import streamlit as st
import pandas as pd

st.title("IoT Anomaly Detector (Demo)")
uploaded = st.file_uploader("Upload CSV logs", type=["csv"])

if uploaded:
    df = pd.read_csv(uploaded)
    st.subheader("Preview")
    st.write(df.head())
    st.subheader("Numeric columns (quick chart)")
    numeric = df.select_dtypes("number")
    if not numeric.empty:
        st.line_chart(numeric)
    else:
        st.info("No numeric columns to chart.")
else:
    st.info("Upload a CSV to explore basic charts.")
