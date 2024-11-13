import streamlit as st
from market_calendar_tool import Site, clean_data, scrape_calendar

st.set_page_config(page_title="Market Calendar Viewer", layout="wide")
st.title("Market Calendar Viewer")
st.sidebar.header("Configuration")

site_options = {
    "Forex": Site.FOREXFACTORY,
    "Metals": Site.METALSMINE,
    "Energy": Site.ENERGYEXCH,
    "Crypto": Site.CRYPTOCRAFT,
}

site_name = st.sidebar.selectbox("Select Calendar", list(site_options.keys()))
selected_site = site_options[site_name]
