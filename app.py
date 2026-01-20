import streamlit as st
import pandas as pd
from topsis1 import run_topsis

st.set_page_config(page_title="TOPSIS Web App")

st.title("TOPSIS Decision Support System")

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

weights = st.text_input("Enter Weights (comma separated)", "1,1,1,1")
impacts = st.text_input("Enter Impacts (comma separated)", "+,+,+,+")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Input Data")
    st.dataframe(df)

    if st.button("Run TOPSIS"):
        try:
            w = weights.split(",")
            i = impacts.split(",")

            if len(w) != len(i):
                st.error("Number of weights must be equal to number of impacts")
            elif any(x not in ['+', '-'] for x in i):
                st.error("Impacts must be + or - only")
            else:
                result = run_topsis(df, weights, impacts)

                st.success("TOPSIS executed successfully!")
                st.subheader("Result")
                st.dataframe(result)

                # Download result
                csv = result.to_csv(index=False).encode("utf-8")
                st.download_button(
                    label="Download Result CSV",
                    data=csv,
                    file_name="topsis_result.csv",
                    mime="text/csv"
                )

        except Exception as e:
            st.error(str(e))
