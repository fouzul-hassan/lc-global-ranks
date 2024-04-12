from Home import *
from constants import *
import streamlit as st
import time
import numpy as np

st.set_page_config(page_title="Global OD Rank", page_icon="📈")

st.markdown("# Global OD Rank")
st.sidebar.header("Global OD Rank")
st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)

selected_entity = st.sidebar.multiselect("Entity", entities, default='Sri Lanka')

all_options = st.sidebar.checkbox("Select all entities")

if all_options:
    selected_entity = entities

selected_criteria = st.sidebar.selectbox("Criteria", criteria_options)
selected_product = st.sidebar.selectbox("Product", product_options)

abs_raw = cooking(DS_ABS,abs_desired_headers)
cr_apd_raw = cooking(DS_CR_APD,cr_apd_desired_headers)
cr_fi_raw = cooking(DS_CR_FI,cr_fi_desired_headers)

merge_od = pd.merge(abs_raw,cr_apd_raw, on=[('Entity',''), ('LC','')])
merge_od = pd.merge(merge_od, cr_fi_raw, on=[('Entity',''), ('LC','')])
od_df = merge_od[global_od_index]


od_caps = pd.read_csv(OD_CAPS)

st.dataframe(od_df)
print(od_df.columns)
st.dataframe(od_caps)
print(od_caps.columns)
od_df_transposed = od_df.transpose()
# # Resetting index to ensure correct DataFrame structure
od_df_transposed.reset_index(drop=True, inplace=True)

od_caps_data = {
    'Cap_Values': ['APPROVED', 'REALIZED', 'FINISHED TO COMPLETED', 'APPROVED TO REALIZED'],
    'iGV': [154, 111, 75, 71.99],
    'iGTa': [31, 30, 49.83, 94.73],
    'iGTe': [15, 12, 50.41, 81.06],
    'oGV': [100, 72, 75, 71.99],
    'oGTa': [26, 25, 49.97, 94.79],
    'oGTe': [22, 17, 50.41, 81.06]
}
od_caps = pd.DataFrame(od_caps_data)

# Function to calculate OD index
def calculate_od_index(df, func, product):
    cap_value = od_caps.loc[od_caps['Cap_Values'] == func, product].iloc[0]
    return df[(func, product)] / cap_value * 10

# Calculate OD index for APPROVED and REALIZED
for func in ['APPROVED', 'REALIZED']:
    for product in ['iGV', 'iGTa', 'iGTe', 'oGV', 'oGTa', 'oGTe']:
        od_df[(func + '_Index', product)] = calculate_od_index(od_df, func, product)

# Calculate OD index for APPROVED TO REALIZED and FINISHED TO COMPLETED
for func in ['APPROVED TO REALIZED', 'FINISHED TO COMPLETED']:
    for product in ['iGV', 'iGTa', 'iGTe', 'oGV', 'oGTa', 'oGTe']:
        cap_value = od_caps.loc[od_caps['Cap_Values'] == func, product].iloc[0]
        od_df[(func + '_Index', product)] = od_df[(func, product)].apply(lambda x: min(x / cap_value * 10, 10))

# Select only the required columns for the final DataFrame
columns_to_keep = ['Entity', 'LC'] + [('APPROVED_Index', product) for product in ['iGV', 'iGTa', 'iGTe', 'oGV', 'oGTa', 'oGTe']] + [('REALIZED_Index', product) for product in ['iGV', 'iGTa', 'iGTe', 'oGV', 'oGTa', 'oGTe']] + [('APPROVED TO REALIZED_Index', product) for product in ['iGV', 'iGTa', 'iGTe', 'oGV', 'oGTa', 'oGTe']] + [('FINISHED TO COMPLETED_Index', product) for product in ['iGV', 'iGTa', 'iGTe', 'oGV', 'oGTa', 'oGTe']]
od_index_df = od_df[columns_to_keep]

st.dataframe(od_index_df)
