from Home import *
from constants import *
import streamlit as st
import time
import numpy as np


st.set_page_config(page_title="Global OD Rank", page_icon="📈")

st.markdown("# Global OD Rank")
st.sidebar.header("Global OD Rank")
st.write("This is Demo of the Global OD Dashboard, where we could use for LCs as well")

selected_entity = st.sidebar.multiselect("Entity", entities, default='Sri Lanka')

all_options = st.sidebar.checkbox("Select all entities")

if all_options:
    selected_entity = entities

selected_criteria = st.sidebar.selectbox("Criteria", criteria_options)
selected_product = st.sidebar.selectbox("Product", product_options)

# abs_raw = cooking(DS_ABS,abs_desired_headers)
# cr_apd_raw = cooking(DS_CR_APD,cr_apd_desired_headers)
# cr_fi_raw = cooking(DS_CR_FI,cr_fi_desired_headers)

merge_od = pd.merge(abs_raw,cr_apd_raw, on=[('Entity',''), ('LC','')])
merge_od = pd.merge(merge_od, cr_fi_raw, on=[('Entity',''), ('LC','')])
od_df = merge_od[global_od_index]


od_df_transposed = od_df.transpose()
criteria_only = od_df_transposed.loc[(selected_criteria, selected_product), :]
entity_only = od_df_transposed.loc[('Entity', ''), :]
lc_only = od_df_transposed.loc[('LC', ''), :]

od_df2 = pd.merge(lc_only, entity_only, left_index=True, right_index=True)
od_df2 = pd.merge(od_df2, criteria_only, left_index=True, right_index=True)
od_df2.columns = od_df2.columns.droplevel(level=1)


st.dataframe(od_df2, use_container_width=True)