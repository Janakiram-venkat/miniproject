import streamlit as st
import pandas as pd

st.title("📄 CSV File Viewer")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("File uploaded successfully!")
    except Exception as e:
        st.error(f"Error reading CSV: {e}")
        st.stop()

    st.markdown("#### 🔹 Data Preview (First 5 Rows)")
    st.container().markdown("""
        <div style="
            padding: 10px;
            border-radius: 10px;
            background-color: #ffffff;
            border: 1px solid #ddd;
            box-shadow: 0px 2px 4px rgba(0,0,0,0.05);
            margin-bottom: 20px;
        ">
    """, unsafe_allow_html=True)
    st.dataframe(df.head())

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("#### 🔹 Summary Statistics")
    st.container().markdown("""
        <div style="
            padding: 10px;
            border-radius: 10px;
            background-color: #ffffff;
            border: 1px solid #ddd;
            box-shadow: 0px 2px 4px rgba(0,0,0,0.05);
            margin-bottom: 20px;
        ">
    """, unsafe_allow_html=True)
    st.write(df.describe(include='all'))
    st.markdown("</div>", unsafe_allow_html=True)
    dtypes = pd.DataFrame(df.dtypes, columns=["Data Type"])
    st.markdown("#### 🔹 Column Data Types")
    st.container().markdown("""
        <div style="
            padding: 10px;
            border-radius: 10px;
            background-color: #ffffff;
            border: 1px solid #ddd;
            box-shadow: 0px 2px 4px rgba(0,0,0,0.05);
            margin-bottom: 20px;
        ">
    """, unsafe_allow_html=True)
    st.write(dtypes)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("### Missing Values")
    missing = pd.DataFrame(df.isnull().sum(), columns=["Missing Values"])
    st.container().markdown("""
        <div style="
            padding: 10px;
            border-radius: 10px;
            background-color: #ffffff;
            border: 1px solid #ddd;
            box-shadow: 0px 2px 4px rgba(0,0,0,0.05);
            margin-bottom: 20px;
        ">
    """, unsafe_allow_html=True)
    st.write(missing)
    st.markdown("</div>", unsafe_allow_html=True)
