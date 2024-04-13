from Home import *
from constants import *
import streamlit as st
import time
import numpy as np

st.set_page_config(page_title="Approval Converstion Rate - Approvals", page_icon="📈")

st.markdown("# Converstion Rate - Approval")
st.sidebar.header("Converstion Rate - Approval ")

# cr_apd_raw = cooking(DS_CR_APD,cr_apd_desired_headers)

#SIDEBAR
selected_entity = st.sidebar.multiselect("Entity", entities, default='Sri Lanka')

all_options = st.sidebar.checkbox("Select all entities")

if all_options:
    selected_entity = entities

selected_status = st.sidebar.selectbox("Status", cr_apd_status_options)
selected_product = st.sidebar.selectbox("Product", product_options)

tranposed_cr_apd_df = cr_apd_raw.transpose()
cr_apd_status_only = tranposed_cr_apd_df.loc[(selected_status, selected_product), :]
entity_only = tranposed_cr_apd_df.loc[('Entity', ''), :]
lc_only = tranposed_cr_apd_df.loc[('LC', ''), :]

cr_apd_df = pd.merge(lc_only, entity_only, left_index=True, right_index=True)
# st.dataframe(cr_apd_df)
cr_apd_df = pd.merge(cr_apd_df, cr_apd_status_only, left_index=True, right_index=True)
cr_apd_df.columns = cr_apd_df.columns.droplevel(level=1)

cr_apd_df['Rank'] = cr_apd_df[selected_status].rank(ascending=False)
cr_apd_df['Rank'] = cr_apd_df['Rank'].astype(int)
cr_apd_df = cr_apd_df.sort_values(by='Rank')
cr_apd_df['LC'] = cr_apd_df.apply(lambda row: 
                                                   f"🥇 {row['LC']}" if row['Rank'] == 1 else 
                                                   f"🥈 {row['LC']}" if row['Rank'] == 2 else 
                                                   f"🥉 {row['LC']}" if row['Rank'] == 3 else 
                                                   row['LC'], axis=1)
cr_apd_df.set_index('Rank', inplace=True)
cr_apd_df = cr_apd_df[cr_apd_df['Entity'].isin(selected_entity)]

def main():
    st.dataframe(cr_apd_df, use_container_width=True)




if __name__ == "__main__":
    main()