import streamlit as st
import requests
import urllib.parse
from streamlit_lottie import st_lottie

st.title("🌤 Weather App (Free API)")

def load_lottie_url(url: str):
    try:
        r = requests.get(url, timeout=6)
        r.raise_for_status()
        return r.json()
    except requests.RequestException:
        return None
    except ValueError:
        return None

lottie_url = "https://lottie.host/0fcd0d5a-864f-49a5-b11b-3c849f961edc/SW5kZcLYJY.json"
lottie_json = load_lottie_url(lottie_url)

if lottie_json:
    st_lottie(lottie_json, height=300)
else:
    st.info("Animation unavailable — continuing without it.")
city = st.text_input("Enter city name:")

def get_coordinates(city):
    if not city or not city.strip():
        return None, None
    q = urllib.parse.quote_plus(city.strip())
    url = f"https://nominatim.openstreetmap.org/search?format=json&q={q}"
    headers = {"User-Agent": "streamlit-mini-project/1.0"}
    try:
        resp = requests.get(url, headers=headers, timeout=10)
        resp.raise_for_status()
        data = resp.json()
    except requests.RequestException:
        return None, None
    if not data:
        return None, None
    return float(data[0]["lat"]), float(data[0]["lon"])

def get_weather(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()
    except requests.RequestException:
        return None
    return data.get("current_weather")

if st.button("Get Weather"):
    lat, lon = get_coordinates(city)
    if lat is None:
        st.error("City not found.")
    else:
        weather = get_weather(lat, lon)
        if not weather:
            st.error("Weather not available.")
        else:
            st.subheader(f"Weather in {city.title()}")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("🌡 Temperature (°C)", weather.get("temperature"))
            with col2:
                st.metric("💨 Wind Speed", f"{weather.get('windspeed')} km/h")
            with col3:
                st.metric("📈 Wind Direction", f"{weather.get('winddirection')}°")
