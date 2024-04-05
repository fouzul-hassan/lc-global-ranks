# Exhchange Marathon - Data Visualization Dashboard

Welcome to our Exchange Marathon Dashboard! This dashboard allows you to visualize data extracted from EXPA using the EXPA API in real-time. Here's how you can set it up and get started:

This repo contans the The AP Hackathon.

## How it Works

We utilize Google Sheets as a datasource and Streamlit, a Python package, for data visualization.

## Prerequistics
1. EXPA Access token
2. Basic Knowledge in Google Sheets & AppScript
3. Basic Python knowledge. You can easily learn Streamlit.

### Prepare the Datasource

1. Create a Google Sheet.
2. Access Extensions -> Appscript.
3. Create a new file or use an existing one.
4. Paste the code from `App-Script -> data-extraction.gs`.

    4.1 In the code you may change the below sections.

   ```javascript
   // API data
   const baseUrl = 'https://analytics.api.aiesec.org/v2/applications/analyze';
   const accessToken = 'your token';
   ```
    4.2. Instead of the above ideas you may add your LC ids and the name

   ```javascript
   // Entity Lists
   const entitiesList = [
     { id: 1630, name: 'Asia Pacific' },
     { id: 572, name: 'Afghanistan' },
     { id: 1591, name: 'Australia' },
   ];
   ```
   4.3. Change the date duration and Make sure that you have a sheet named 'Final'
   ```javascript
   // CONFIGS
   const startDate = "2024-04-03";
   const endDate = "2024-04-07";
   const sheetName = "Final";
    ```

5. Set up a trigger to extract data in real-time.

5.1 howevr the left bar and choose the alarm/clock icon (trigger) which is in the 4th from top to down
5.2 Click the blue colour +Add Trigger Icon
5.3 You will get a prompt
5.4 Choose ''startProcess'' in ''Choose which function to run''
5.5 Choose ''which deployment should run'' as ''Head''
5.6 ''Choose Select event source'' as ''Time-driven''
5.7 based on your preference choose ''Select type of time based trigger'' and ''Select hour interval''

Now the dataset is ready you can see the data realtime in the Final tab.

Additional, you may use a pivot to analys them or the usual google sheet formaulas and tricks to make a sheet dashboard.

### Publish the data to the web

1. From the Google Sheet -> click File -> Share -> Publish to web
2. Choose the specific tab (Final in my case) and choose the csv option.
3. Then you will get a link. Copy the link and keep it with you safely

### Streamlit Instructions

It's better if you are using Anaconda or conda, but you can create a virtual environment [click here](https://docs.streamlit.io/get-started/installation) for more details about the installation.

### Dashboard changes the you need to do

1. Fork our repo (link of the repo). (link to a doc - how to fork a repo)
2. Clone the repo in your PC
3. You may add your link that you copied when you pucblush the csv to the web in leaderboard.py
```python
sheet_url = 'your link here'
```

### Deploy Streamlit

Then you can commit & push the codes

Then you may deploy your streamlit app easily within a few steps. [Clikc here for the tutorials](link : https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app)


## Team Collaborators

![Fouzul Hassan](https://media.licdn.com/dms/image/C4D03AQH1BIxCvtFTsg/profile-displayphoto-shrink_800_800/0/1658296759194?e=1717632000&v=beta&t=FEAvF66N066k-yO_tqJk6K79wpTHpiz8_7zdg6YjTFI) ![Senuri Bandara](https://media.licdn.com/dms/image/C5603AQF4_cugH3k0Mg/profile-displayphoto-shrink_800_800/0/1640343615995?e=1717632000&v=beta&t=vwP2x7PAuOW9T8F1gKCoD99zIx4ERcW-koUf-z9kJuM) ![Kavindu Senevirathne](https://media.licdn.com/dms/image/D5603AQGNiaKPen9VpA/profile-displayphoto-shrink_800_800/0/1709876478824?e=1717632000&v=beta&t=6rwL0nX7QEq5JfpvziMw8KTzkaAas-mADOkQIGTzJEI) ![Pasindu Bhanuka](https://media.licdn.com/dms/image/D5603AQEadGKGOOJ06Q/profile-displayphoto-shrink_800_800/0/1710271260092?e=1717632000&v=beta&t=3ju1TwM--Y6Mnw6rn4WfF2YrjJSwSQzP3iesWxIQtbw)

1. **Fouzul Hassan** - MCVP IM
   - [LinkedIn](https://www.linkedin.com/in/fouzul-hassan/)
   
2. **Senuri Bandara** - Analytics Lead
   - [LinkedIn](https://www.linkedin.com/in/senuri-bandara/)
   
3. **Kavindu Senevirathne** - Developer Team Leader
   - [LinkedIn](https://www.linkedin.com/in/kavindu-senevirathne/)
   
4. **Pasindu Bhanuka** - Developer
   - [LinkedIn](https://www.linkedin.com/in/pasindu-bhanuka-/)
