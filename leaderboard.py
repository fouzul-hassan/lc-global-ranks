import streamlit as st
import pandas as pd
import requests
import plotly.express as px
import json  # Import the json module
import plotly.express as px
from streamlit_autorefresh import st_autorefresh

# Loading Data
@st.cache_data(ttl=5)  # 300 seconds = 5 minutes #1800
def load_data(sheet_url):
    try:
        data = pd.read_csv(sheet_url)
        return data
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return None

def generate_grouped_bar_chart(data, entity):
    # Define color map for each entity
    
    filtered_df = data[data['Entity'] == entity]
    fig = px.bar(filtered_df, x='Function', y=['Applied', 'Approved', 'Unique_LCs'],
                 title=f'Grouped Bar Chart for {entity}',
                 labels={'value': 'Count', 'Function': 'Function'},
                 barmode='group',
                 )
    
    
    
    return fig


# Function to create a bar chart based on the specified metric
def create_bar_chart_seperate(df, entity, metric, title):
    filtered_df = df[df['Entity'] == entity]
    fig = px.bar(filtered_df, x='Function', y=metric, title=title, labels={'Function': 'Function', 'Entity': 'Entity', metric: metric}, color='Function')
    return fig

# Function to create a bar chart based on the total points of each entity
def create_bar_chart(entity_sum):
    # Convert entity sum dictionary to DataFrame
    df_entity_sum = pd.DataFrame.from_dict(entity_sum, orient='index')
    
    # Reset index to make entity a column instead of index
    df_entity_sum.reset_index(inplace=True)
    df_entity_sum.rename(columns={'index': 'Entity'}, inplace=True)
    
    # Create a bar chart using Plotly Express
    fig = px.bar(df_entity_sum, x='Entity', y='Total', title='Total Score', labels={'Entity': 'Entity', 'Total': 'Total Points'}, color='Entity')

            # Hide the legend
    fig.update_layout(showlegend=False)
    
    return fig

# Function to calculate the total 'Applied' related to each entity
def calculate_total_applied(df):
    entity_applied_total = {}
    for index, row in df.iterrows():
        entity = row['Entity']
        applied = row['Applied']
        if entity not in entity_applied_total:
            entity_applied_total[entity] = applied
        else:
            entity_applied_total[entity] += applied
    return entity_applied_total

# Function to calculate the total 'Approved' related to each entity
def calculate_total_approved(df):
    entity_approved_total = {}
    for index, row in df.iterrows():
        entity = row['Entity']
        approved = row['Approved']
        if entity not in entity_approved_total:
            entity_approved_total[entity] = approved
        else:
            entity_approved_total[entity] += approved
    return entity_approved_total

# Function to calculate the count of 'Applied' related to each entity based on the selected function
def count_applied_by_entity(df, selected_function):
    filtered_df = df[df['Function'] == selected_function]
    applied_counts = filtered_df.groupby('Entity')['Applied'].sum().reset_index()
    applied_counts.rename(columns={'Applied': 'Count_Applied'}, inplace=True)
    return applied_counts

# Function to calculate the count of 'Approved' related to each entity based on the selected function
def count_approved_by_entity(df, selected_function):
    filtered_df = df[df['Function'] == selected_function]
    approved_counts = filtered_df.groupby('Entity')['Approved'].sum().reset_index()
    approved_counts.rename(columns={'Approved': 'Count_Approved'}, inplace=True)
    return approved_counts


icon_path = 'https://aiesec.lk/data/dist/images/favicon.png'

entity_colors={
                'CC': '#ffdabc',
                'CN': '#cfbaf0',
                'CS': '#90dbf4',
                'USJ': '#efeaa9',
                'Kandy': '#a3c4f3',
                'Ruhuna': '#a6f2ae',
                'SLIIT': '#f1c0e8',
                'NSBM': '#8eecf5',
                'NIBM': '#98f5e1',
                'Rajarata': '#ffcfd2'
            }

def show_guide():

    st.write("1. Overall Walkthrough")
    overall_gif = open("overall.gif", "rb").read()
    st.image(overall_gif)

    st.write("2. Wide Mode")
    wide_gif = open("wide.gif", "rb").read()
    st.image(wide_gif)

    st.write("3. Change the Theme")
    dark_gif = open("dark.gif", "rb").read()
    st.image(dark_gif)


# Main Streamlit app
def main():
    st.set_page_config(
    layout="wide",
    page_title="AP Hackathon - Dashboard",
    page_icon= icon_path,
    )   

    st.title("AP Hackathon - Dashboard")

    # with st.expander("**Dashboard Guide**"):
    #     show_guide()
    #     st.write("Click the **\"Dashboard Guide\"** again to hide the guide")

    st_autorefresh(interval=5 * 60 * 1000, key="data_refresh")  # Set interval to 5 minutes
    # URL to your Google Sheets data
    sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRQ0DK7DqYpQQwLsb93-fbhDN1NhHLO9P7GNhyceIwWdj5EOFInWSflTbvDYrakkuEJlDHgDV25kP9w/pub?gid=1562137798&single=true&output=csv"

    # Load data using the cached function
    data = load_data(sheet_url)
    # st_autorefresh(interval=5 * 60 * 1000, key="data_refresh") 

    if data is not None:
        #st.write("Data loaded successfully:")
        #st.write(data)

        # Check if the 'Entity' column exists in the DataFrame
        if 'Entity' in data.columns:

            # Create a sidebar with a selector to choose the 'Function'
            #selected_function = st.sidebar.selectbox('Select Function', data['Function'].unique())

            
            # Calculate entity sum
            # entity_sum = calculate_entity_sum(data)

            # Convert entity sum to JSON object
            # entity_sum_json = json.dumps(entity_sum)

            # # Create the bar chart
            # bar_chart = create_bar_chart(entity_sum)

            # Display the bar chart using Plotly Chart
            # st.plotly_chart(bar_chart, use_container_width=True)


            # Barchart 1 : APP
            # Calculate total 'Applied' related to each entity
            entity_applied_total = calculate_total_applied(data)

            # Convert dictionary to DataFrame
            df_entity_applied_total = pd.DataFrame.from_dict(entity_applied_total, orient='index', columns=['Total_Applied'])
            df_entity_applied_total.reset_index(inplace=True)
            df_entity_applied_total.rename(columns={'index': 'Entity'}, inplace=True)

            # Create a colored bar chart using Plotly Express
            fig = px.bar(df_entity_applied_total, x='Entity', y='Total_Applied', title='Total Applications by Entity', labels={'Entity': 'Entity', 'Total_Applied': 'Applications'}, color='Entity', color_discrete_map=entity_colors)

            # Hide the legend
            fig.update_layout(showlegend=False)


            # Barchart 2: APD
            # Calculate total 'Approved' related to each entity
            entity_approved_total = calculate_total_approved(data)

            # Convert dictionary to DataFrame
            df_entity_approved_total = pd.DataFrame.from_dict(entity_approved_total, orient='index', columns=['Total_Approved'])
            df_entity_approved_total.reset_index(inplace=True)
            df_entity_approved_total.rename(columns={'index': 'Entity'}, inplace=True)

            # Create a colored bar chart using Plotly Express
            fig_approved = px.bar(df_entity_approved_total, x='Entity', y='Total_Approved', title='Total Approvals by Entity', labels={'Entity': 'Entity', 'Total_Approved': 'Approvals'},color='Entity', color_discrete_map=entity_colors)

            # Hide the legend
            fig_approved.update_layout(showlegend=False)

            # Barchart 3: Unique LCs
            # Calculate total 'Unique_LCs' related to each entity
            # entity_unique_lcs_total = calculate_total_unique_lcs(data)

            # # Convert dictionary to DataFrame
            # df_entity_unique_lcs_total = pd.DataFrame.from_dict(entity_unique_lcs_total, orient='index', columns=['Total_Unique_LCs'])
            # df_entity_unique_lcs_total.reset_index(inplace=True)
            # df_entity_unique_lcs_total.rename(columns={'index': 'Entity'}, inplace=True)

            # # Create a colored bar chart using Plotly Express
            # fig_unique_lcs = px.bar(df_entity_unique_lcs_total, x='Entity', y='Total_Unique_LCs', title='Total Unique LCs by Entity', labels={'Entity': 'Entity', 'Total_Unique_LCs': 'Unique LCs'},color='Entity', color_discrete_map=entity_colors)

            # # Hide the legend
            # fig_unique_lcs.update_layout(showlegend=False)

            # Display the bar charts using Plotly Chart
            # col1, col2, col3 = st.columns(3)
            # col1, col2 = st.columns(2)

            # with col1:
            #     # Render the bar chart using Streamlit
            #     st.plotly_chart(fig, use_container_width=True)

            # with col2:
            #     # Render the bar chart using Streamlit
            #     st.plotly_chart(fig_approved, use_container_width=True)

            # with col3:
            #     # Render the bar chart using Streamlit
            #     st.plotly_chart(fig_unique_lcs, use_container_width=True)
            st.plotly_chart(fig_approved, use_container_width=True)
            st.plotly_chart(fig, use_container_width=True)
            

            st.subheader('Functional Analysis')

            # Generate and display grouped bar chart
            #st.plotly_chart(generate_grouped_bar_chart(data, selected_entity))
            # Create a select box to choose the 'Function'
            selected_function = st.selectbox('Select Function', data['Function'].unique())
            

            # Barchart 4: APP by Function
            # Get the count of 'Applied' related to each entity based on the selected function
            applied_counts = count_applied_by_entity(data, selected_function)

            # Create a bar chart using Plotly Express
            fig_1 = px.bar(applied_counts, x='Entity', y='Count_Applied', title=f'Applications by Entity for {selected_function} Function',labels={'Entity': 'Entity', 'Count_Applied': 'Applications'}, color='Entity', color_discrete_map=entity_colors)
            fig_1.update_layout(showlegend=False)
            # Barchart 5: APD by Function
            # Get the count of 'Approved' related to each entity based on the selected function
            approved_counts = count_approved_by_entity(data, selected_function)

            # Create a bar chart using Plotly Express
            fig_2 = px.bar(approved_counts, x='Entity', y='Count_Approved', title=f'Approvals by Entity for {selected_function} Function',labels={'Entity': 'Entity', 'Count_Approved': 'Approvals'}, color='Entity', color_discrete_map=entity_colors)
            fig_2.update_layout(showlegend=False)
            # Barchart 6: Unique_LCs by Function
            # Get the count of 'Unique_LCs' related to each entity based on the selected function
            # unique_lcs_counts = count_unique_lcs_by_entity(data, selected_function)

            # # Create a bar chart using Plotly Express
            # fig_3 = px.bar(unique_lcs_counts, x='Entity', y='Count_Unique_LCs', title=f'No of Unique_LCs by Entity for {selected_function} Function',labels={'Entity': 'Entity', 'Count_Unique_LCs': 'Unique LCs'}, color='Entity', color_discrete_map=entity_colors)
            # fig_3.update_layout(showlegend=False)
            

            # Display the bar charts using Plotly Chart
            # col1, col2, col3 = st.columns(3)
            # col1, col2 = st.columns(2)

            # with col1:
            #     # Render the bar chart using Streamlit
            #     st.plotly_chart(fig_1, use_container_width=True)

            # with col2:
            #     # Render the bar chart using Streamlit
            #     st.plotly_chart(fig_2, use_container_width=True)
            st.plotly_chart(fig_2, use_container_width=True)
            st.plotly_chart(fig_1, use_container_width=True)
            
            # with col3:
            #     # Render the bar chart using Streamlit
            #     st.plotly_chart(fig_3, use_container_width=True)

            st.write("<br><br>", unsafe_allow_html=True)
            #Footer
            st.write("<p style='text-align: center;'>Made with ❤️ by &lt;/Dev.Team&gt; of AIESEC in Sri Lanka</p>", unsafe_allow_html=True)


        else:
            st.error("The 'Entity' column does not exist in the loaded data.")
    else:
        st.error("Failed to load data.")

if __name__ == "__main__":
    main()
