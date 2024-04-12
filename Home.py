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
def hyperRanking(abs_raw,status_options):
    selected_entity = st.sidebar.multiselect("Entity", entities, default='Sri Lanka')

    all_options = st.sidebar.checkbox("Select all entities")

    if all_options:
        selected_entity = entities

    selected_status = st.sidebar.selectbox("Status", status_options)
    selected_product = st.sidebar.selectbox("Product", product_options)


    # print(abs_raw.columns.tolist())
    tranposed_abs_df = abs_raw.transpose()
    status_only = tranposed_abs_df.loc[(selected_status, selected_product), :]
    entity_only = tranposed_abs_df.loc[('Entity', ''), :]
    lc_only = tranposed_abs_df.loc[('LC', ''), :]

    abs_df = pd.merge(lc_only, entity_only, left_index=True, right_index=True)
    # st.dataframe(abs_df)
    abs_df = pd.merge(abs_df, status_only, left_index=True, right_index=True)
    abs_df.columns = abs_df.columns.droplevel(level=1)

    abs_df['Rank'] = abs_df[selected_status].rank(ascending=False)
    abs_df['Rank'] = abs_df['Rank'].astype(int)
    abs_df = abs_df.sort_values(by='Rank')
    abs_df['LC'] = abs_df.apply(lambda row: 
                                                    f"🥇 {row['LC']}" if row['Rank'] == 1 else 
                                                    f"🥈 {row['LC']}" if row['Rank'] == 2 else 
                                                    f"🥉 {row['LC']}" if row['Rank'] == 3 else 
                                                    row['LC'], axis=1)
    abs_df.set_index('Rank', inplace=True)
    abs_df = abs_df[abs_df['Entity'].isin(selected_entity)]

    st.dataframe(abs_df, use_container_width=True)


#CR

def main():
    st.write("Hello")



if __name__ == "__main__":
    main()