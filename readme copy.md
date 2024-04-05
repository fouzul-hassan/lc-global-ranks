
Introduction.

We do have a Google Sheet for the datasource, we extract the data from EXPA using EXPA API (analytics.api.aiesec.org). Publish the data as a CSV realtime to get a link.

Sample Sheet for your referance ()

Streamlit which is python package for visulaise the data.
You can use the created function and replicate them or you can reuse the functions.


How it works.

The Google AppScript(link for the file) extracts the data from EXPA to the sheets in the format for easy data visualisation.
Prerequistics
1. EXPA Access token
2. Basic Knowledge in Google Sheets & AppScript
3. Basic Python knowledge. You can easily learn Streamlit.

Steps.

Section 1 Prepare the datasource
1. Create a Google Sheet
2. Click Extentiosns -> Appscript
3. Create a File or use the default file. (You may create another file)
4. Paste the code from App-Script -> data-extraction.gs
(markdown to past the data)
    
    ``````
// // API data
   const baseUrl = 'https://analytics.api.aiesec.org/v2/applications/analyze';
   const accessToken = 'your token';
    ```
    4.1 Add your access token (at line 3)

    4.2 Add your enitity list
    ```
    // // Entity Lists
const entitiesList = [
 { id: 1630, name: 'Asia Pacific' },
 { id: 572, name: 'Afghanistan' },
{ id: 1591, name: 'Australia' },
    ```
    Instead of the above ideas you may add your LC ids and the name
    // // CONFIGS
    const startDate = "2024-04-03"; //change the date as you want
    onst endDate = "2024-04-07"; //change the date as you want
    const sheetName = "Final" //change the sheet name as you want
    ```
    4.2 Change the date duration (at line )
    4.3 Make sure that you have a sheet named 'Final'

5. Now add a trigger from the Appscript to extract the data realtime 
    5.1 howevr the left bar and choose the alram/clock icon (trigger) which is in the 4th from top to down
    5.2 Click the blue colour +Add Trigger Icon
    5.3 You will get a prompt
    5.4 Choose 'startProcess' in Choose which function to run
    5.5 Choose which deployment should run is Head
    5.6 Choose Select event source as Time-driven
    5.7 based on your preference choose 'Select type of time based trigger' and 'Select hour interval'

Now the dataset is ready you can see the data realtime in the final tab.

Additional, you may use a pivot to analys them or the usual google sheet formaulas and tricks to make a sheet dashboard.

Prepare the Codes & Data

From the Google Sheet -> click File -> Share -> Publish to web
Choose the speciifc tab (Final in my case) and choose csv

Then you will get a link. Copy the link and keep it with you safely

Streamlit Instructions

Better if you are using Anaconda or conda, but anyways you can create a virtual env (https://docs.streamlit.io/get-started/installation) for more deatils about the installation.

Dashboard Sourcedes

Fork our repo (link of the repo). (link to a doc - how to fork a repo)
Clone the repo in your PC

You may add your link that you copied when you pucblush the csv to the web in leaderboard.py line 28
```
sheet_url = 'your link here'
```

Then you can commit & push the codes

Then you may deploy your streamlit app easity (link : https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app)


About us.

It would be great if you could give us a recongtion if you are using this, fork our repo and give us a star if you like it

Team (Collobrators)

Photo
Name
Position
Email
Linkedin url

(i need to add 4 people's data)