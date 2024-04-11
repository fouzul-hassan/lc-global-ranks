# from streamlit_autorefresh import st_autorefresh

import streamlit as st
import pandas as pd

icon_path = 'https://aiesec.lk/data/dist/images/favicon.png'
st.set_page_config(
    layout="centered",
    page_title="LC Global Rank - Dashboard",
    page_icon= icon_path,
)

st.title('LC Global Rank - Dashboard')

# Load data outside of Streamlit app initialization
@st.cache_data(ttl=1800) 
def load_data(data_url):
    try:
        data = pd.read_csv(data_url)

        # Check if 'month_name' column exists
        if 'month_name' not in data.columns:
            st.error("Error: 'month_name' column not found in the CSV file.")
            return None

        data['month_name'] = pd.to_datetime(data['month_name'], format='%Y %B', errors='coerce').dt.strftime('%B %Y')
        return data
    except Exception as e:
        st.error(f"An error occurred while loading data: {e}")
        return None

def something():
    st.write('something')

def main():
    something()


if __name__ == "__main__":
    main()