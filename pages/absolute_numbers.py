from Home import *
from constants import *
import streamlit as st
import time
import numpy as np
import numpy as np


st.set_page_config(page_title="Absolute Numbers", page_icon="📈")

st.markdown("# Absolute Numbers")
st.sidebar.header("Absolute Numbers")

#SIDEBAR
selected_entity = st.sidebar.multiselect("Entity", entities, default='Sri Lanka')

all_options = st.sidebar.checkbox("Select all entities")

if all_options:
    selected_entity = entities

selected_status = st.sidebar.selectbox("Status", status_options)
selected_product = st.sidebar.selectbox("Product", product_options)

abs_raw = cooking(DS_ABS,abs_desired_headers)

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

def main():
    st.dataframe(abs_df, use_container_width=True)
    # st.dataframe(abs_df['Rank'])



if __name__ == "__main__":
    main()