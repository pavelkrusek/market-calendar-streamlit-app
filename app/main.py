from datetime import datetime, timedelta

import streamlit as st
from market_calendar_tool import Site, clean_data, scrape_calendar

st.set_page_config(page_title="Market Calendar Tool", layout="wide")
st.title("Market Calendar Tool")
st.markdown(
    "<h4 style='color:red;'>This is just preliminary testing - the application is not yet finalized!</h4>",
    unsafe_allow_html=True,
)
st.sidebar.header("Options")

site_options = {
    "Forex": Site.FOREXFACTORY,
    "Metals": Site.METALSMINE,
    "Energy": Site.ENERGYEXCH,
    "Crypto": Site.CRYPTOCRAFT,
}

site_name = st.sidebar.selectbox("Select Calendar", list(site_options.keys()))
selected_site = site_options[site_name]

# st.sidebar.subheader("Date Range")

default_date_from = datetime.today()
default_date_to = datetime.today() + timedelta(days=7)

date_from = st.sidebar.date_input("From Date", value=default_date_from)
date_to = st.sidebar.date_input("To Date", value=default_date_to)

date_from_str = date_from.strftime("%Y-%m-%d")
date_to_str = date_to.strftime("%Y-%m-%d")

if st.sidebar.button("Scrape Calendar"):
    with st.spinner("Scraping data..."):
        try:
            raw_data = scrape_calendar(
                site=selected_site,
                date_from=date_from_str,
                date_to=date_to_str,
                extended=False,
            )
            cleaned_data = clean_data(raw_data)
            st.success("Data scraped and cleaned successfully!")

            st.subheader("Cleaned Data")
            st.dataframe(cleaned_data.base)
        except Exception as e:
            st.error(f"An error occurred: {e}")
else:
    st.info("Configure options and click 'Scrape Calendar' to view data.")
