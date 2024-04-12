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

#ABS
abs_data = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS43L7E1wBBLFkrhteENsUvYm7WSXN7NGbRChxL4vXFDKd4hnnsIYLkqzuhv7iJFP0MXxV3X7eZjA4M/pub?gid=1093091800&single=true&output=csv"

# Desired headers
abs_desired_headers = [('Entity',''), ('LC',''), ('SIGN UPs', 'OGX'), ('SIGN UPs', 'oGV'),
                       ('SIGN UPs', 'oGTa'), ('SIGN UPs', 'oGTe'),
                       ('APPLICANTS', 'Total'), ('APPLICANTS', 'iGV'),
                       ('APPLICANTS', 'iGTa'), ('APPLICANTS', 'iGTe'),
                       ('APPLICANTS', 'oGV'), ('APPLICANTS', 'oGTa'),
                       ('APPLICANTS', 'oGTe'), ('ACCEPTED APPLICANTS', 'Total'),
                       ('ACCEPTED APPLICANTS', 'iGV'), ('ACCEPTED APPLICANTS', 'iGTa'),
                       ('ACCEPTED APPLICANTS', 'iGTe'), ('ACCEPTED APPLICANTS', 'oGV'),
                       ('ACCEPTED APPLICANTS', 'oGTa'), ('ACCEPTED APPLICANTS', 'oGTe'),
                       ('APPROVED', 'Total'), ('APPROVED', 'iGV'), ('APPROVED', 'iGTa'),
                       ('APPROVED', 'iGTe'), ('APPROVED', 'oGV'), ('APPROVED', 'oGTa'),
                       ('APPROVED', 'oGTe'), ('REALIZED', 'Total'), ('REALIZED', 'iGV'),
                       ('REALIZED', 'iGTa'), ('REALIZED', 'iGTe'), ('REALIZED', 'oGV'),
                       ('REALIZED', 'oGTa'), ('REALIZED', 'oGTe'), ('FINISHED', 'Total'),
                       ('FINISHED', 'iGV'), ('FINISHED', 'iGTa'), ('FINISHED', 'iGTe'),
                       ('FINISHED', 'oGV'), ('FINISHED', 'oGTa'), ('FINISHED', 'oGTe'),
                       ('COMPLETED', 'Total'), ('COMPLETED', 'iGV'),
                       ('COMPLETED', 'iGTa'), ('COMPLETED', 'iGTe'), ('COMPLETED', 'oGV'),
                       ('COMPLETED', 'oGTa'), ('COMPLETED', 'oGTe')]

abs_df = cooking(abs_data,abs_desired_headers)

# List of entities
entities = [
    "All",  "Sri Lanka", "Afghanistan", "Albania", "Algeria", "Andorra", "Argentina", "Australia", "Bangladesh",
    "Bahrain", "Belgium", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica",
    "Croatia", "Denmark", "Dominican Republic", "Ecuador", "El Salvador", "Ethiopia", "Finland",
    "France", "Georgia", "Germany", "Greece", "Guatemala", "Hong Kong", "India", "Indonesia",
    "Italy", "Japan", "Kenya", "Lebanon", "Malaysia", "Mexico", "Morocco", "Nepal", "New Zealand",
    "Nigeria", "Pakistan", "Panama", "Paraguay", "Peru", "Philippines", "Portugal", "Russia",
    "Rwanda", "Singapore", "South Africa", "South Korea", "Spain", "Sweden",
    "Switzerland", "Taiwan", "Tanzania", "Thailand", "Turkey", "Uganda", "Ukraine",
    "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Uzbekistan",
    "Venezuela", "Vietnam", "Zambia", "Zimbabwe"
]

# Status and Product options (You need to replace these with your actual DataFrame)
status_options = ['APPLICANTS', 'ACCEPTED APPLICANTS', 'APPROVED', 'REALIZED', 'FINISHED', 'COMPLETED']  # Replace with actual status column names
product_options = ['Total', 'iGV', 'iGTa', 'iGTe', 'oGV', 'oGTa', 'oGTe']  # Replace with actual product options

# Sidebar dropdowns
# options = st.multiselect(
#     'What are your favorite colors',
#     ['Green', 'Yellow', 'Red', 'Blue'],
#     ['Yellow', 'Red'])

selected_entity = st.sidebar.multiselect("Entity", entities, default='Sri Lanka')

all_options = st.sidebar.checkbox("Select all entities")

if all_options:
    selected_entity = entities


selected_status = st.sidebar.selectbox("Status", status_options)
selected_product = st.sidebar.selectbox("Product", product_options)

# Display selected options
st.button(f"Selected Status: {selected_status}")
st.button(f"Selected Product: {selected_product}")

if (selected_entity == 'All'):
    filtered_data = abs_df
else:
    filtered_data = abs_df[abs_df['Entity'].isin(selected_entity)]
tranposed_abs_df = filtered_data.transpose()

status_only = tranposed_abs_df.loc[(selected_status, selected_product), :]
entity_only = tranposed_abs_df.loc[('Entity', ''), :]
lc_only = tranposed_abs_df.loc[('LC', ''), :]

abs_df = pd.merge(lc_only, entity_only, left_index=True, right_index=True)
abs_df = pd.merge(abs_df, status_only, left_index=True, right_index=True)
abs_df.columns = abs_df.columns.droplevel(level=1)

abs_df['Rank'] = abs_df[selected_status].rank(ascending=False)
abs_df['Rank'] = abs_df['Rank'].astype(int)
abs_df = abs_df.sort_values(by='Rank')
abs_df.set_index('Rank', inplace=True)

def main():
    st.dataframe(abs_df, use_container_width=True)
    # st.dataframe(abs_df['Rank'])



if __name__ == "__main__":
    main()