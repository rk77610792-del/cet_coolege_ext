import streamlit as st
import pandas as pd
from utils import extract_from_pdf

st.set_page_config(page_title="CET College Extractor", layout="wide")

st.title("📊 CET College Data Extractor")

uploaded_file = st.file_uploader("Upload PDF File", type=["pdf"])

if uploaded_file:
    st.success("File uploaded successfully!")

    if st.button("Extract Data"):
        with st.spinner("Processing..."):
            data = extract_from_pdf(uploaded_file)

            if data:
                df = pd.DataFrame(data)

                st.subheader("📋 Extracted Data")
                st.dataframe(df)

                csv = df.to_csv(index=False).encode("utf-8")

                st.download_button(
                    label="📥 Download CSV",
                    data=csv,
                    file_name="cet_colleges.csv",
                    mime="text/csv"
                )
            else:
                st.error("No data extracted. Check format or regex.")
