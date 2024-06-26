

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

cr_apd_desired_headers = [('Entity',''), ('LC',''),
                       ('APPROVED TO REALIZED', 'Total'), ('APPROVED TO REALIZED', 'iGV'),
                       ('APPROVED TO REALIZED', 'iGTa'), ('APPROVED TO REALIZED', 'iGTe'),
                       ('APPROVED TO REALIZED', 'oGV'), ('APPROVED TO REALIZED', 'oGTa'),
                       ('APPROVED TO REALIZED', 'oGTe'), 
                       
                       ('APPROVED TO FINISHED', 'Total'),
                       ('APPROVED TO FINISHED', 'iGV'), ('APPROVED TO FINISHED', 'iGTa'),
                       ('APPROVED TO FINISHED', 'iGTe'), ('APPROVED TO FINISHED', 'oGV'),
                       ('APPROVED TO FINISHED', 'oGTa'), ('APPROVED TO FINISHED', 'oGTe'),

                       ('APPROVED TO COMPLETED', 'Total'), ('APPROVED TO COMPLETED', 'iGV'), ('APPROVED TO COMPLETED', 'iGTa'),
                       ('APPROVED TO COMPLETED', 'iGTe'), ('APPROVED TO COMPLETED', 'oGV'), ('APPROVED TO COMPLETED', 'oGTa'),
                       ('APPROVED TO COMPLETED', 'oGTe')
                       ]

cr_fi_desired_headers = [('Entity',''), ('LC',''),
                       ('FINISHED TO COMPLETED', 'Total'), ('FINISHED TO COMPLETED', 'iGV'),
                       ('FINISHED TO COMPLETED', 'iGTa'), ('FINISHED TO COMPLETED', 'iGTe'),
                       ('FINISHED TO COMPLETED', 'oGV'), ('FINISHED TO COMPLETED', 'oGTa'),
                       ('FINISHED TO COMPLETED', 'oGTe')
                       ]

global_od_index =    [(               'Entity',      ''),
            (                   'LC',      ''),
            (             'APPROVED', 'Total'),
            (             'APPROVED',   'iGV'),
            (             'APPROVED',  'iGTa'),
            (             'APPROVED',  'iGTe'),
            (             'APPROVED',   'oGV'),
            (             'APPROVED',  'oGTa'),
            (             'APPROVED',  'oGTe'),
            (             'REALIZED', 'Total'),
            (             'REALIZED',   'iGV'),
            (             'REALIZED',  'iGTa'),
            (             'REALIZED',  'iGTe'),
            (             'REALIZED',   'oGV'),
            (             'REALIZED',  'oGTa'),
            (             'REALIZED',  'oGTe'),
            ( 'APPROVED TO REALIZED', 'Total'),
            ( 'APPROVED TO REALIZED',   'iGV'),
            ( 'APPROVED TO REALIZED',  'iGTa'),
            ( 'APPROVED TO REALIZED',  'iGTe'),
            ( 'APPROVED TO REALIZED',   'oGV'),
            ( 'APPROVED TO REALIZED',  'oGTa'),
            ( 'APPROVED TO REALIZED',  'oGTe'),
            ('FINISHED TO COMPLETED', 'Total'),
            ('FINISHED TO COMPLETED',   'iGV'),
            ('FINISHED TO COMPLETED',  'iGTa'),
            ('FINISHED TO COMPLETED',  'iGTe'),
            ('FINISHED TO COMPLETED',   'oGV'),
            ('FINISHED TO COMPLETED',  'oGTa'),
            ('FINISHED TO COMPLETED',  'oGTe')]

caps_for_od =    [
            (             'APPROVED', 'Total'),
            (             'APPROVED',   'iGV'),
            (             'APPROVED',  'iGTa'),
            (             'APPROVED',  'iGTe'),
            (             'APPROVED',   'oGV'),
            (             'APPROVED',  'oGTa'),
            (             'APPROVED',  'oGTe'),
            (             'REALIZED', 'Total'),
            (             'REALIZED',   'iGV'),
            (             'REALIZED',  'iGTa'),
            (             'REALIZED',  'iGTe'),
            (             'REALIZED',   'oGV'),
            (             'REALIZED',  'oGTa'),
            (             'REALIZED',  'oGTe'),
            ( 'APPROVED TO REALIZED', 'Total'),
            ( 'APPROVED TO REALIZED',   'iGV'),
            ( 'APPROVED TO REALIZED',  'iGTa'),
            ( 'APPROVED TO REALIZED',  'iGTe'),
            ( 'APPROVED TO REALIZED',   'oGV'),
            ( 'APPROVED TO REALIZED',  'oGTa'),
            ( 'APPROVED TO REALIZED',  'oGTe'),
            ('FINISHED TO COMPLETED', 'Total'),
            ('FINISHED TO COMPLETED',   'iGV'),
            ('FINISHED TO COMPLETED',  'iGTa'),
            ('FINISHED TO COMPLETED',  'iGTe'),
            ('FINISHED TO COMPLETED',   'oGV'),
            ('FINISHED TO COMPLETED',  'oGTa'),
            ('FINISHED TO COMPLETED',  'oGTe')]
           

#DATASOURCES
#ABSOLOUTE DATA
DS_ABS = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTtYp1uQypeAWtw1wvihQbfv7s1Nhsh_F3E_UAPp_BbiyBGp8stzBvZyr95MRh2k_OtS3XBSwIRceK2/pub?gid=1093091800&single=true&output=csv"

DS_CR_APD = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSItRnn06ZOIJNe0w2bI3JzhOsMfpv0fTKw3hIuUttZT5THMX8Kh-6uJqO527Atjymrznh2zb_F0UQ2/pub?gid=494749078&single=true&output=csv"

DS_CR_FI = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRLWqm66H8ChjimA7wmGirTHxEpSd9v9Sz2mcNN7fdBfhWDmERbU2ig4XdXH35xE8CtFqnv2VDm_pY5/pub?gid=494749078&single=true&output=csv"

OD_CAPS = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRPwQNthVD5A-wLT1QGPsnWvbG5Z-aNZIYn4502fve7oWYxnaxV6weUpWrNcUz6F_DtO0boOe-eVWl0/pub?gid=1669770517&single=true&output=csv"

### DROP DOWN SETTINGS ###

# Absoloute Data
status_options = ['APPLICANTS', 'ACCEPTED APPLICANTS', 'APPROVED', 'REALIZED', 'FINISHED', 'COMPLETED']  # Replace with actual status column names

# Converstion Rate from APD
cr_apd_status_options = ['APPROVED TO REALIZED', 'APPROVED TO FINISHED', 'APPROVED TO COMPLETED']  # Replace with actual status column names

cr_fi_status_options = ['FINISHED TO COMPLETED']

#General
product_options = ['Total', 'iGV', 'iGTa', 'iGTe', 'oGV', 'oGTa', 'oGTe']

criteria_options = ['APPROVED','REALIZED','FINISHED TO COMPLETED','APPROVED TO REALIZED']

# List of entities
entities = [
    "Sri Lanka",
    "Argentina",
    "Bolivia",
    "Brazil",
    "Canada",
    "Chile",
    "Colombia",
    "Costa Rica",
    "Dominican Republic",
    "Ecuador",
    "El Salvador",
    "Guatemala",
    "Mexico",
    "Nicaragua",
    "Panama",
    "Paraguay",
    "Peru",
    "United States",
    "Venezuela",
    "Australia",
    "Bangladesh",
    "Cambodia",
    "Mainland of China",
    "Hong Kong",
    "India",
    "Indonesia",
    "Japan",
    "Malaysia",
    "Mongolia",
    "Myanmar",
    "Nepal",
    "New Zealand",
    "Pakistan",
    "Philippines",
    "Singapore",
    "South Korea",
    "Taiwan",
    "Thailand",
    "Vietnam",
    "Albania",
    "Armenia",
    "Austria",
    "Azerbaijan",
    "Belgium",
    "Bosnia and Herzegovina",
    "Bulgaria",
    "Croatia",
    "Czech Republic",
    "Denmark",
    "Estonia",
    "Finland",
    "France",
    "Georgia",
    "Germany",
    "Greece",
    "Hungary",
    "Iceland",
    "Italy",
    "Kazakhstan",
    "Kyrgyzstan",
    "Latvia",
    "Lithuania",
    "Macedonia",
    "Moldova",
    "Montenegro",
    "Norway",
    "Poland",
    "Portugal",
    "Romania",
    "Russia",
    "Serbia",
    "Slovakia",
    "Spain",
    "Sweden",
    "Switzerland",
    "The Netherlands",
    "Turkey",
    "Ukraine",
    "United Kingdom",
    "Algeria",
    "Bahrain",
    "Benin",
    "Burkina Faso",
    "Cameroon",
    "Cote D'Ivoire",
    "Egypt",
    "Ethiopia",
    "Ghana",
    "Jordan",
    "Kenya",
    "Kuwait",
    "Lebanon",
    "Liberia",
    "Malawi",
    "Morocco",
    "Mozambique",
    "Namibia",
    "Nigeria",
    "Rwanda",
    "Senegal",
    "South Africa",
    "Tanzania",
    "Togo",
    "Tunisia",
    "Uganda",
    "United Arab Emirates",
    ]

