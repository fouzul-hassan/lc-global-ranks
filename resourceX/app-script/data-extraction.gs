// API data
const baseUrl = 'https://analytics.api.aiesec.org/v2/applications/analyze';
const accessToken = 'your token'; // Add your token here

// Entity Lists
const entitiesList = [
    // { id: 1630, name: 'Asia Pacific' },
    // { id: 572, name: 'Afghanistan' },
    { id: 1591, name: 'Australia' },
    { id: 2010, name: 'Bangladesh' },
    // { id: 2104, name: 'Bhutan' },
    { id: 305, name: 'Cambodia' },
    // { id: 2240, name: 'Fiji' },
    { id: 1594, name: 'Hong Kong' },
    { id: 1585, name: 'India' },
    { id: 1539, name: 'Indonesia' },
    // { id: 495, name: 'Iran' },
    { id: 1615, name: 'Japan' },
    { id: 1562, name: 'Korea' },
    // { id: 55, name: 'Laos' },
    { id: 1613, name: 'Mainland of China' },
    { id: 1611, name: 'Malaysia' },
    // { id: 2105, name: 'Maldives' },
    { id: 409, name: 'Mongolia' },
    { id: 4, name: 'Myanmar' },
    { id: 112, name: 'Nepal' },
    { id: 1616, name: 'New Zealand' },
    { id: 1603, name: 'Pakistan' },
    { id: 1604, name: 'Philippines' },
    { id: 1575, name: 'Singapore' },
    { id: 1623, name: 'Sri Lanka' },
    { id: 1561, name: 'Taiwan' },
    { id: 1607, name: 'Thailand' },
    { id: 504, name: 'Vietnam' }
];


// Functional Parsing
const regexList = [
  // {name: "Total", pattern: /^.*_total$/},
  {name: "oGV", pattern: /^o_.*_[7]$/},
  {name: "oGTa", pattern: /^o_.*_[8]$/},
  {name: "oGTe", pattern: /^o_.*_[9]$/},

  {name: "iGV", pattern: /^i_.*_[7]$/},
  {name: "iGTa", pattern: /^i_.*_[8]$/},
  {name: "iGTe", pattern: /^i_.*_[9]$/}
];

// CONFIGS
const startDate = "2024-04-03"; //change the date as you want
const endDate = "2024-04-07"; //change the date as you want
const sheetName = "Final" //change the sheet name as you want

// Exchange Phases //Uncomment if the phase is required
const keysList = [
  // "matched",
  "applied",
  // "an_accepted",
  "approved",
  // "realized",
  // "remote_realized",
  // "finished",
  // "completed"
]

// HEADERS // Exchange Phases //Uncomment if the phase is required
const headersList = [
  "Entity",
  "Function",
  // "Matched",
  "Applied",
  // "An-Accepted",
  "Approved",
  // "Realized",
  // "Remote Realized",
  // "Finished",
  // "Completed",
]

// Helper functions
function fetchDataByLC(startDate, endDate, lcId) {
  const url = `${baseUrl}?access_token=${accessToken}&start_date=${startDate}&end_date=${endDate}&performance_v3[office_id]=${lcId}`;
  const json = UrlFetchApp.fetch(url).getContentText();
  const data = JSON.parse(json);
  return data;
}

function extractData(apiOutput) {
  let extractedData = {}

  regexList.forEach((regex) => {
    let obj = {}

    const regexMatches = Object.entries(apiOutput).filter(([key, value]) => regex.pattern.test(key));

    regexMatches.forEach((match)=> {
      keysList.forEach((key) => {
        if(match[0].includes(key)){
          obj[key] = obj[key] ? obj[key] : 0 + (match[1]?.applicants?.value || 0)
        };
      });
    })

    extractedData[regex.name] = obj
  })

  return extractedData;
}

function prepareSheet() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(sheetName);

  if (!sheet) {
    throw new Error($`Sheet with name ${sheetName} does not exist.`);
  }
  sheet.getRange(1, 1, 1 , headersList.length).setValues([headersList]); 
}

function writeRowToSheet(rowIndex, rowData){
    const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(sheetName);

    sheet.getRange(1 + rowIndex, 1, 1 , rowData.length).setValues([rowData]); 
}

// =================

function startProcess(){
  console.log("Starting process...");
  prepareSheet();

  let finalOutput = {}

  console.log("Fetching data...")
  entitiesList.forEach((entity) => {
    const apiOutput = fetchDataByLC(startDate, endDate, entity.id);
    const extractedData = extractData(apiOutput);

    finalOutput[entity.name] = extractedData;
  });

  console.log(finalOutput);
  console.log("Writing to sheet edited...");

  entitiesList.forEach((entity, index1) => {
    regexList.forEach((regex, index2)=> {
      const dynamicColumns = keysList.map((key) => finalOutput[entity.name][regex.name][key]);

        const rowData = [
        entity.name,
        regex.name,
        ...dynamicColumns
      ];

    writeRowToSheet((index1 * regexList.length)+(index2+1), rowData);
    });
  });

  console.log("Done writing to sheet :)");
}