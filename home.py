import streamlit as st
from streamlit_lottie import st_lottie
import requests

st.set_page_config(page_title="Mini Project Dashboard", page_icon="🌐")

def load_lottie_url(url: str):
    try:
        r = requests.get(url, timeout=6)
        r.raise_for_status()
        return r.json()
    except requests.RequestException:
        return None
    except ValueError:
        return None

lottie_url = "https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json"
lottie_json = load_lottie_url(lottie_url)

st.title("🌐 Mini Project Dashboard")

if lottie_json:
    st_lottie(lottie_json, height=300)
else:
    st.info("Animation unavailable — continuing without it.")

st.markdown("""
    <div style="
        padding: 20px;
        border-radius: 12px;
        background-color: #e8e8ef; 
        border: 1px solid #d0d0d5;
        box-shadow: 0px 2px 6px rgba(0,0,0,0.05);
        margin-top: 20px;
        color: #1a1a1a; 
    ">
        <h3 style="margin-bottom:0; color:#1a1a1a;">👋 Welcome!</h3>
        <p style="margin-top:10px; color:#1a1a1a;">
            This is your multi-page Streamlit application.
            Use the sidebar to explore features like CSV Viewer, Weather App, and Database Manager.
        </p>
    </div>
""", unsafe_allow_html=True)



