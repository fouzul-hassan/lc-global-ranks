# from streamlit_autorefresh import st_autorefresh

import streamlit as st
import pandas as pd
from constants import *
import time

icon_path = 'https://aiesec.lk/data/dist/images/favicon.png'
st.title('LC Global Rank - Dashboard')

#ETL
st.toast('If this is your first time, the app might take more time to load the data!!!')

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
progress_text = "Loading the data. Please wait.. !"
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    
    abs_raw = cooking(DS_ABS,abs_desired_headers)
    cr_apd_raw = cooking(DS_CR_APD,cr_apd_desired_headers)
    cr_fi_raw = cooking(DS_CR_FI,cr_fi_desired_headers)
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1, text=progress_text)
time.sleep(1)
my_bar.empty()

st.button("Reload")


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