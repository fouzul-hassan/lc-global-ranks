# from streamlit_autorefresh import st_autorefresh

import streamlit as st
import pandas as pd
from constants import *

icon_path = 'https://aiesec.lk/data/dist/images/favicon.png'
st.set_page_config(
    layout="centered",
    page_title="LC Global Rank - Dashboard",
    page_icon= icon_path,
)

st.title('LC Global Rank - Dashboard')

#ETL
@st.cache_data
def cooking(dara_url, desired_headers):
    # Create DataFrame from current headers
    df_origin = pd.read_csv(dara_url, header=[0,1])

    # Replace headers
    df_origin.columns = pd.MultiIndex.from_tuples(desired_headers)

    # Remove rows with NaN values
    df_cleaned = df_origin.dropna()
    # drop all the CLOSED LCs
    filtered_data = df_cleaned[~df_cleaned.iloc[:, 1].str.contains('closed', case=False)]
    
    return filtered_data

# Data Imports
abs_raw = cooking(DS_ABS,abs_desired_headers)
cr_apd_raw = cooking(DS_CR_APD,cr_apd_desired_headers)
cr_fi_raw = cooking(DS_CR_FI,cr_fi_desired_headers)

#ABSOLOUTE NUMBERS



#CR

def main():
    st.write("Hello")



if __name__ == "__main__":
    main()