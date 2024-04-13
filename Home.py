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
@st.cache_data(ttl=None, show_spinner=True)
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

#CR
abs_raw = cooking(DS_ABS,abs_desired_headers)
cr_apd_raw = cooking(DS_CR_APD,cr_apd_desired_headers)
cr_fi_raw = cooking(DS_CR_FI,cr_fi_desired_headers)

def main():

    st.markdown(
        """
        You are at the right place to see where do you stand Globally !!
        **👈 Select the options in the sidebar** to see
        the RANKs of your LCs!
        ### Ranks based on Absoloute Numbers
        - Check out [👈 Absoloute Numbers](https://global-lc-ranks.streamlit.app/absolute_numbers)
        ### Ranks based on Converstion Rates
        - Check out [👈 Converstion Rate Based on Approvals](https://global-lc-ranks.streamlit.app/APD_Conversion_Rate)
        - Check out [👈 Converstion Rate Based on Finished ](https://global-lc-ranks.streamlit.app/FI_Conversion_Rate)

        ### Ranks based on the Global OD Index (Not Fully Done)
         - Check out  [👈 Global OD Index (Pre-realse version)](https://global-lc-ranks.streamlit.app/Global_OD_Index)

        ### Upcoming Features
         - Global OD Index based on LCs
         - All Converstion Rates
         - Process Time
         - Goal Recommendation for LCs
    """
    )



if __name__ == "__main__":
    main()