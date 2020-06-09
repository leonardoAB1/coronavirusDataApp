import tkinter as tk 
from PIL import ImageTk, Image
#from selenium import webdriver
import requests, json
from tkinter import messagebox as mg
import tkinter.ttk as ttk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


#root commands
root=tk.Tk()
root.title('Coronavirus NOW')
root.iconbitmap('images/coronavirus.ico')
root.geometry('1020x580')
background_image=Image.open("images/background.jpg").resize((1020,580), Image.ANTIALIAS)
background_image=ImageTk.PhotoImage(background_image)
tk.Label(root, image=background_image).place(x=0, y=0, relwidth=1, relheight=1)


#def frames
plot_frame=tk.LabelFrame(root, padx=2, pady=2, relief="groove", bd=10)
left_frame=tk.LabelFrame(root, padx=2,pady=2, relief="groove", bd=10)

#insert frames
plot_frame.grid(row=0, column=1, padx=1, pady=1, sticky="nse")
left_frame.grid(row=0, column=0, padx=1, pady=1, sticky="nsw")

#constants
source_value=tk.StringVar()
source_value.set("A")
selected_country=tk.StringVar()
selected_country_2=tk.StringVar()

checkbox_value=tk.IntVar()
checkbox_value.set(0)
dates=[]

def evaluateSource():
    global countries, country_codes, country_options, country_options_2, selected_country, selected_country_2
    if source_value.get()=="A":
        countries=['Afghanistan', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica',
                        'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas',
                        'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia',
                        'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory',
                        'British Virgin Islands', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon',
                        'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island',
                        'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo (Brazzaville)', 'Congo (Kinshasa)', 'Cook Islands',
                        'Costa Rica', 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', "Côte d'Ivoire", 'Denmark', 'Djibouti', 'Dominica',
                        'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia',
                        'Falkland Islands (Malvinas)', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia',
                        'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland',
                        'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti',
                        'Heard and Mcdonald Islands', 'Holy See (Vatican City State)', 'Honduras', 'Hong Kong, SAR China', 'Hungary',
                        'Iceland', 'India', 'Indonesia', 'Iran, Islamic Republic of', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy',
                        'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea (North)', 'Korea (South)', 'Kuwait',
                        'Kyrgyzstan', 'Lao PDR', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg',
                        'Macao, SAR China', 'Macedonia, Republic of', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands',
                        'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia, Federated States of', 'Moldova', 'Monaco', 'Mongolia',
                        'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'Netherlands Antilles',
                        'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Norway',
                        'Oman', 'Pakistan', 'Palau', 'Palestinian Territory', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn',
                        'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Republic of Kosovo', 'Romania', 'Russian Federation', 'Rwanda', 'Réunion',
                        'Saint Helena', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Pierre and Miquelon', 'Saint Vincent and Grenadines',
                        'Saint-Barthélemy', 'Saint-Martin (French part)', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia',
                        'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia',
                        'South Africa', 'South Georgia and the South Sandwich Islands', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname',
                        'Svalbard and Jan Mayen Islands', 'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic (Syria)', 'Taiwan, Republic of China',
                        'Tajikistan', 'Tanzania, United Republic of', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago',
                        'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'US Minor Outlying Islands', 'Uganda',
                        'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States of America', 'Uruguay', 'Uzbekistan', 'Vanuatu',
                        'Venezuela (Bolivarian Republic)', 'Viet Nam', 'Virgin Islands, US', 'Wallis and Futuna Islands', 'Western Sahara',
                        'Yemen', 'Zambia', 'Zimbabwe']
        country_codes={'Afghanistan': 'afghanistan', 'Albania': 'albania', 'Algeria': 'algeria', 'American Samoa': 'american-samoa',
                        'Andorra': 'andorra', 'Angola': 'angola', 'Anguilla': 'anguilla', 'Antarctica': 'antarctica',
                        'Antigua and Barbuda': 'antigua-and-barbuda', 'Argentina': 'argentina', 'Armenia': 'armenia', 'Aruba': 'aruba',
                        'Australia': 'australia', 'Austria': 'austria', 'Azerbaijan': 'azerbaijan', 'Bahamas': 'bahamas', 'Bahrain': 'bahrain',
                        'Bangladesh': 'bangladesh', 'Barbados': 'barbados', 'Belarus': 'belarus', 'Belgium': 'belgium', 
                        'Belize': 'belize', 'Benin': 'benin', 'Bermuda': 'bermuda', 'Bhutan': 'bhutan', 'Bolivia': 'bolivia',
                        'Bosnia and Herzegovina': 'bosnia-and-herzegovina', 'Botswana': 'botswana', 'Bouvet Island': 'bouvet-island', 
                        'Brazil': 'brazil', 'British Indian Ocean Territory': 'british-indian-ocean-territory', 
                        'British Virgin Islands': 'british-virgin-islands', 'Brunei Darussalam': 'brunei', 
                        'Bulgaria': 'bulgaria', 'Burkina Faso': 'burkina-faso', 'Burundi': 'burundi',
                        'Cambodia': 'cambodia', 'Cameroon': 'cameroon', 'Canada': 'canada', 'Cape Verde': 'cape-verde',
                        'Cayman Islands': 'cayman-islands', 'Central African Republic': 'central-african-republic', 'Chad': 'chad',
                        'Chile': 'chile', 'China': 'china', 'Christmas Island': 'christmas-island',
                        'Cocos (Keeling) Islands': 'cocos-keeling-islands', 'Colombia': 'colombia',
                        'Comoros': 'comoros', 'Congo (Brazzaville)': 'congo-brazzaville', 'Congo (Kinshasa)': 'congo-kinshasa',
                        'Cook Islands': 'cook-islands', 'Costa Rica': 'costa-rica', 'Croatia': 'cote-divoire', 
                        'Cuba': 'croatia', 'Cyprus': 'cuba', 'Czech Republic': 'cyprus', "Côte d'Ivoire": 'czech-republic',
                        'Denmark': 'denmark', 'Djibouti': 'djibouti', 'Dominica': 'dominica', 'Dominican Republic': 'dominican-republic',
                        'Ecuador': 'ecuador', 'Egypt': 'egypt', 'El Salvador': 'el-salvador', 'Equatorial Guinea': 'equatorial-guinea',
                        'Eritrea': 'eritrea', 'Estonia': 'estonia', 'Ethiopia': 'ethiopia', 'Falkland Islands (Malvinas)': 'falkland-islands-malvinas',
                        'Faroe Islands': 'faroe-islands', 'Fiji': 'fiji', 'Finland': 'finland', 'France': 'france', 'French Guiana': 'french-guiana',
                        'French Polynesia': 'french-polynesia', 'French Southern Territories': 'french-southern-territories', 'Gabon': 'gabon',
                        'Gambia': 'gambia', 'Georgia': 'georgia', 'Germany': 'germany', 'Ghana': 'ghana', 'Gibraltar': 'gibraltar',
                        'Greece': 'greece', 'Greenland': 'greenland', 'Grenada': 'grenada', 'Guadeloupe': 'guadeloupe',
                        'Guam': 'guam', 'Guatemala': 'guatemala', 'Guernsey': 'guernsey', 'Guinea': 'guinea',
                        'Guinea-Bissau': 'guinea-bissau', 'Guyana': 'guyana', 'Haiti': 'haiti',
                        'Heard and Mcdonald Islands': 'heard-and-mcdonald-islands', 'Holy See (Vatican City State)': 'holy-see-vatican-city-state',
                        'Honduras': 'honduras', 'Hong Kong, SAR China': 'hong-kong-sar-china', 'Hungary': 'hungary',
                        'Iceland': 'iceland', 'India': 'india', 'Indonesia': 'indonesia', 'Iran, Islamic Republic of': 'iran',
                        'Iraq': 'iraq', 'Ireland': 'ireland', 'Isle of Man': 'isle-of-man', 'Israel': 'israel', 'Italy': 'italy',
                        'Jamaica': 'jamaica', 'Japan': 'japan', 'Jersey': 'jersey', 'Jordan': 'jordan', 'Kazakhstan': 'kazakhstan',
                        'Kenya': 'kenya', 'Kiribati': 'kiribati', 'Korea (North)': 'korea-north', 'Korea (South)': 'korea-south', 
                        'Kuwait': 'kuwait', 'Kyrgyzstan': 'kyrgyzstan', 'Lao PDR': 'lao-pdr', 'Latvia': 'latvia', 'Lebanon': 'lebanon',
                        'Lesotho': 'lesotho', 'Liberia': 'liberia', 'Libya': 'libya', 'Liechtenstein': 'liechtenstein', 'Lithuania': 'lithuania',
                        'Luxembourg': 'luxembourg', 'Macao, SAR China': 'macao-sar-china', 'Macedonia, Republic of': 'macedonia',
                        'Madagascar': 'madagascar', 'Malawi': 'malawi', 'Malaysia': 'malaysia', 'Maldives': 'maldives',
                        'Mali': 'mali', 'Malta': 'malta', 'Marshall Islands': 'marshall-islands', 'Martinique': 'martinique',
                        'Mauritania': 'mauritania', 'Mauritius': 'mauritius', 'Mayotte': 'mayotte', 'Mexico': 'mexico',
                        'Micronesia, Federated States of': 'micronesia', 'Moldova': 'moldova', 'Monaco': 'monaco', 'Mongolia': 'mongolia',
                        'Montenegro': 'montenegro', 'Montserrat': 'montserrat', 'Morocco': 'morocco', 'Mozambique': 'mozambique', 'Myanmar': 'myanmar',
                        'Namibia': 'namibia', 'Nauru': 'nauru', 'Nepal': 'nepal', 'Netherlands': 'netherlands', 'Netherlands Antilles': 'netherlands-antilles',
                        'New Caledonia': 'new-caledonia', 'New Zealand': 'new-zealand', 'Nicaragua': 'nicaragua', 'Niger':'niger' ,
                        'Nigeria': 'nigeria', 'Niue': 'niue', 'Norfolk Island': 'norfolk-island', 'Northern Mariana Islands': 'northern-mariana-islands',
                        'Norway':'norway' , 'Oman': 'oman', 'Pakistan': 'pakistan', 'Palau': 'palau',
                        'Palestinian Territory': 'palestine', 'Panama':'panama' , 'Papua New Guinea': 'papua-new-guinea', 'Paraguay': 'paraguay',
                        'Peru': 'peru', 'Philippines': 'philippines', 'Pitcairn': 'pitcairn', 'Poland': 'poland', 'Portugal': 'portugal',
                        'Puerto Rico': 'puerto-rico', 'Qatar': 'qatar', 'Republic of Kosovo': 'kosovo', 'Romania': 'romania',
                        'Russian Federation': 'russia', 'Rwanda': 'rwanda', 'Réunion': 'réunion', 'Saint Helena': 'saint-helena',
                        'Saint Kitts and Nevis': 'saint-kitts-and-nevis', 'Saint Lucia': 'saint-lucia', 'Saint Pierre and Miquelon': 'saint-pierre-and-miquelon',
                        'Saint Vincent and Grenadines': 'saint-vincent-and-the-grenadines', 'Saint-Barthélemy': 'saint-barthélemy',
                        'Saint-Martin (French part)': 'saint-martin-french-part', 'Samoa': 'samoa', 'San Marino': 'san-marino',
                        'Sao Tome and Principe': 'sao-tome-and-principe', 'Saudi Arabia': 'saudi-arabia', 'Senegal': 'senegal', 'Serbia': 'serbia',
                        'Seychelles': 'seychelles', 'Sierra Leone': 'sierra-leone', 'Singapore': 'singapore', 'Slovakia': 'slovakia',
                        'Slovenia': 'slovenia', 'Solomon Islands': 'solomon-islands', 'Somalia': 'somalia', 'South Africa': 'south-africa',
                        'South Georgia and the South Sandwich Islands': 'south-georgia-and-the-south-sandwich-islands',
                        'South Sudan': 'south-sudan', 'Spain': 'spain', 'Sri Lanka': 'sri-lanka', 'Sudan': 'sudan', 'Suriname': 'suriname',
                        'Svalbard and Jan Mayen Islands': 'svalbard-and-jan-mayen-islands', 'Swaziland': 'swaziland', 'Sweden': 'sweden',
                        'Switzerland': 'switzerland', 'Syrian Arab Republic (Syria)': 'syria', 'Taiwan, Republic of China': 'taiwan', 
                        'Tajikistan': 'tajikistan', 'Tanzania, United Republic of': 'tanzania', 'Thailand': 'thailand', 
                        'Timor-Leste': 'timor-leste', 'Togo': 'togo', 'Tokelau': 'tokelau', 'Tonga': 'tonga', 
                        'Trinidad and Tobago': 'trinidad-and-tobago', 'Tunisia': 'tunisia', 'Turkey': 'turkey', 'Turkmenistan': 'turkmenistan', 
                        'Turks and Caicos Islands': 'turks-and-caicos-islands', 'Tuvalu': 'tuvalu', 'US Minor Outlying Islands': 'us-minor-outlying-islands', 
                        'Uganda': 'uganda', 'Ukraine': 'ukraine', 'United Arab Emirates': 'united-arab-emirates', 
                        'United Kingdom': 'united-kingdom', 'United States of America': 'united-states', 'Uruguay': 'uruguay', 
                        'Uzbekistan': 'uzbekistan', 'Vanuatu': 'vanuatu', 'Venezuela (Bolivarian Republic)': 'venezuela', 'Viet Nam': 'vietnam',
                        'Virgin Islands, US': 'virgin-islands', 'Wallis and Futuna Islands': 'wallis-and-futuna-islands', 
                        'Western Sahara': 'western-sahara', 'Yemen': 'yemen', 'Zambia': 'zambia', 'Zimbabwe': 'zimbabwe'}

    else:
        countries=['Afghanistan', 'Albania', 'Algeria', 'Angola', 'Argentina', 'Armenia', 'Australia', 'Austria',
                        'Azerbaijan', 'Bahamas', 'Bangladesh', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia',
                        'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso',
                        'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Ivory Coast', 'Central African Republic', 'Chad',
                        'Chile', 'China', 'Colombia', 'Congo', 'Democratic Republic of Congo','Costa Rica', 'Croatia',
                        'Cuba', 'Cyprus', 'Czechia', 'Denmark', 'Diamond Princess', 'Djibouti', 'Dominican Republic',
                        'DR Congo', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia',
                        'Falkland Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Southern Territories',
                        'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Greenland', 'Guatemala', 'Guinea',
                        'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras','Hong Kong', 'Hungary', 'Iceland', 'India',
                        'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan',
                        'Kenya', 'Korea', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Lao', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia',
                        'Libya', 'Lithuania', 'Luxembourg', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Mali',
                        'Mauritania', 'Mexico', 'Moldova', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar',
                        'Namibia', 'Nepal','Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria',
                        'North Korea', 'Norway', 'Oman', 'Pakistan', 'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay',
                        'Peru', 'Philippines', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Republic of Kosovo',
                        'Romania', 'Russia', 'Rwanda', 'Saudi Arabia', 'Senegal', 'Serbia', 'Sierra Leone',
                        'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa',
                        'South Korea','South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname',
                        'Svalbard and Jan Mayen','Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic',
                        'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Trinidad and Tobago',
                        'Tunisia', 'Turkey', 'Turkmenistan', 'UAE', 'Uganda', 'United Kingdom', 'Ukraine', 'USA',
                        'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam', 'Western Sahara', 'Yemen',
                        'Zambia', 'Zimbabwe']
        country_codes={'Afghanistan': 'AF', 'Albania': 'AL', 'Algeria': 'DZ', 'Angola': 'AO', 'Argentina': 'AR',
                        'Armenia': 'AM', 'Australia': 'AU', 'Austria': 'AT', 'Azerbaijan': 'AZ', 'Bahamas': 'BS',
                        'Bangladesh': 'BD', 'Belarus': 'BY', 'Belgium': 'BE', 'Belize': 'BZ', 'Benin': 'BJ',
                        'Bhutan': 'BT', 'Bolivia': 'BO', 'Bosnia and Herzegovina': 'BA', 'Botswana': 'BW',
                        'Brazil': 'BR', 'Brunei Darussalam': 'BN', 'Bulgaria': 'BG', 'Burkina Faso': 'BF',
                        'Burundi': 'BI', 'Cambodia': 'KH', 'Cameroon': 'CM', 'Canada': 'CA', 'Ivory Coast': 'CI',
                        'Central African Republic': 'CF', 'Chad': 'TD', 'Chile': 'CL', 'China': 'CN', 'Colombia': 'CO',
                        'Congo': 'CG', 'Democratic Republic of Congo': 'CD', 'Costa Rica': 'CR', 'Croatia': 'HR',
                        'Cuba': 'CU', 'Cyprus': 'CY', 'Czechia': 'CZ', 'Denmark': 'DK', 'Diamond Princess': 'DP',
                        'Djibouti': 'DJ', 'Dominican Republic': 'DO', 'DR Congo': 'CD', 'Ecuador': 'EC', 'Egypt': 'EG',
                        'El Salvador': 'SV', 'Equatorial Guinea': 'GQ', 'Eritrea': 'ER', 'Estonia': 'EE', 'Ethiopia': 'ET',
                        'Falkland Islands': 'FK', 'Fiji': 'FJ', 'Finland': 'FI', 'France': 'FR', 'French Guiana': 'GF',
                        'French Southern Territories': 'TF', 'Gabon': 'GA', 'Gambia': 'GM', 'Georgia': 'GE',
                        'Germany': 'DE', 'Ghana': 'GH', 'Greece': 'GR', 'Greenland': 'GL', 'Guatemala': 'GT',
                        'Guinea': 'GN', 'Guinea-Bissau': 'GW', 'Guyana': 'GY', 'Haiti': 'HT', 'Honduras': 'HN',
                        'Hong Kong': 'HK', 'Hungary': 'HU', 'Iceland': 'IS', 'India': 'IN', 'Indonesia': 'ID',
                        'Iran': 'IR', 'Iraq': 'IQ', 'Ireland': 'IE', 'Israel': 'IL', 'Italy': 'IT', 'Jamaica': 'JM',
                        'Japan': 'JP', 'Jordan': 'JO', 'Kazakhstan': 'KZ', 'Kenya': 'KE', 'Korea': 'KP',
                        'Kosovo': 'XK', 'Kuwait': 'KW', 'Kyrgyzstan': 'KG', 'Lao': 'LA', 'Latvia': 'LV',
                        'Lebanon': 'LB', 'Lesotho': 'LS', 'Liberia': 'LR', 'Libya': 'LY', 'Lithuania': 'LT',
                        'Luxembourg': 'LU', 'Macedonia': 'MK', 'Madagascar': 'MG', 'Malawi': 'MW', 'Malaysia': 'MY', 
                        'Mali': 'ML', 'Mauritania': 'MR', 'Mexico': 'MX', 'Moldova': 'MD', 'Mongolia': 'MN', 'Montenegro': 'ME', 
                        'Morocco': 'MA', 'Mozambique': 'MZ', 'Myanmar': 'MM', 'Namibia': 'NA', 'Nepal': 'NP', 'Netherlands': 'NL', 
                        'New Caledonia': 'NC', 'New Zealand': 'NZ', 'Nicaragua': 'NI', 'Niger': 'NE', 'Nigeria': 'NG', 
                        'North Korea': 'KP', 'Norway': 'NO', 'Oman': 'OM', 'Pakistan': 'PK', 'Palestine': 'PS', 'Panama': 'PA', 
                        'Papua New Guinea': 'PG', 'Paraguay': 'PY', 'Peru': 'PE', 'Philippines': 'PH', 'Poland': 'PL', 'Portugal': 'PT', 
                        'Puerto Rico': 'PR', 'Qatar': 'QA', 'Republic of Kosovo': 'XK', 'Romania': 'RO', 'Russia': 'RU', 'Rwanda': 'RW', 
                        'Saudi Arabia': 'SA', 'Senegal': 'SN', 'Serbia': 'RS', 'Sierra Leone': 'SL', 'Singapore': 'SG', 'Slovakia': 'SK', 
                        'Slovenia': 'SI', 'Solomon Islands': 'SB', 'Somalia': 'SO', 'South Africa': 'ZA', 'South Korea': 'KR', 
                        'South Sudan': 'SS', 'Spain': 'ES', 'Sri Lanka': 'LK', 'Sudan': 'SD', 'Suriname': 'SR',
                        'Svalbard and Jan Mayen': 'SJ', 'Swaziland': 'SZ', 'Sweden': 'SE', 'Switzerland': 'CH',
                        'Syrian Arab Republic': 'SY', 'Taiwan': 'TW', 'Tajikistan': 'TJ', 'Tanzania': 'TZ', 'Thailand': 'TH',
                        'Timor-Leste': 'TL', 'Togo': 'TG', 'Trinidad and Tobago': 'TT', 'Tunisia': 'TN', 'Turkey': 'TR',
                        'Turkmenistan': 'TM', 'UAE': 'AE', 'Uganda': 'UG', 'United Kingdom': 'GB', 'Ukraine': 'UA',
                        'USA': 'US', 'Uruguay': 'UY', 'Uzbekistan': 'UZ', 'Vanuatu': 'VU', 'Venezuela': 'VE', 
                        'Vietnam': 'VN', 'Western Sahara': 'EH', 'Yemen': 'YE', 'Zambia': 'ZM', 'Zimbabwe': 'ZW'}

    if selected_country.get()==None:
        selected_country.set(country_codes["Afghanistan"])
    elif selected_country_2.get()==None:
        selected_country_2.set(country_codes["Afghanistan"])

    #Option Menus
    country_options=ttk.OptionMenu(left_frame, selected_country, *countries)
    country_options_2=ttk.OptionMenu(left_frame, selected_country_2, *countries)
    country_options.grid(row=1, column=0, sticky="we")
    country_options_2.grid(row=10, column=0, sticky="we")
    if checkbox_value.get()==0:
        country_options_2.config(state="disable")
evaluateSource()




#def entries
country_entry=tk.Entry(left_frame, width=30)
confirmed_entry=tk.Entry(left_frame, width=30)
deaths_entry=tk.Entry(left_frame, width=30)
recovered_entry=tk.Entry(left_frame, width=30)
active_entry=tk.Entry(left_frame, width=30)
date_entry=tk.Entry(left_frame, width=30)

country_entry_2=tk.Entry(left_frame, width=30)
confirmed_entry_2=tk.Entry(left_frame, width=30)
deaths_entry_2=tk.Entry(left_frame, width=30)
recovered_entry_2=tk.Entry(left_frame, width=30)
active_entry_2=tk.Entry(left_frame, width=30)
date_entry_2=tk.Entry(left_frame, width=30)

#buttons commands
#open, size and add image into plot_frame
def wallpaperCall():
    global wallpaper
    wallpaper=Image.open("images/wallpaper.jpg").resize((640,530), Image.ANTIALIAS)
    wallpaper=ImageTk.PhotoImage(wallpaper)
    tk.Label(plot_frame, image=wallpaper).pack()


#process data for plotting and manage entries
def processData(select_second_country=False, day_number=-1): 
                           
    global country_entry, confirmed_entry, deaths_entry, recovered_entry, active_entry, date_entry
    global country_entry_2, confirmed_entry_2, deaths_entry_2, recovered_entry_2, active_entry_2, date_entry_2

    global dates                          
    data=[]
    fig=Figure(figsize=(6.5,5),dpi=100)
    
      
    try:
        #update source/selected_country error handling
        if not selected_country.get().islower() and source_value.get()=="A":
            selected_country.set(country_codes[selected_country.get()])
        if len(selected_country.get())!=2 and source_value.get()=="B":
            selected_country.set(country_codes[selected_country.get()])
        if not(selected_country_2.get().islower()) and source_value.get()=="A":
            selected_country_2.set(country_codes[selected_country_2.get()])
        if len(selected_country_2.get())!=2 and source_value.get()=="B":
            selected_country_2.set(country_codes[selected_country_2.get()])
    except KeyError:
        mg.showinfo("Error", "Source Error\nTry Updating Source")
    else:
        
        try:
            if source_value.get()=="A":
                #info request/query
                api_requests_day_one=requests.get("https://api.covid19api.com/dayone/country/{}/status/confirmed".format(selected_country.get()))
                api_day_one=json.loads(api_requests_day_one.content)
                
                for dict in api_day_one:                     
                    x_axis=(dict["Date"])
                    dates.append(x_axis)
                    y_axis=(dict["Cases"])
                    data.append((len(dates),y_axis))
                x,y=zip(*data)
                processed_data=(x,y)

            
                if select_second_country==False:
                    clearFrame(plot_frame)
                    #clear entries
                    country_entry.delete(0,'end')
                    confirmed_entry.delete(0,'end')
                    deaths_entry.delete(0,'end')
                    recovered_entry.delete(0,'end')
                    active_entry.delete(0,'end')
                    active_entry.delete(0,'end')
                    date_entry.delete(0,'end')
                    day_number_entry.delete(0,'end')
                    #info request/query
                    status=requests.get("https://api.covid19api.com/live/country/{}/status/confirmed".format(selected_country.get()))
                    status=json.loads(status.content)
                    country_entry.insert(0,status[day_number]["Country"])
                    confirmed_entry.insert(0,status[day_number]["Confirmed"])
                    deaths_entry.insert(0,status[day_number]["Deaths"])
                    recovered_entry.insert(0,status[day_number]["Recovered"])
                    active_entry.insert(0,status[day_number]["Active"])
                    date_entry.insert(0,status[day_number]["Date"][:10])
                    
                    #search dta by date
                    day_number_entry.config(state="normal")
                    day_button.config(state="normal")
                    
                    #add data plot to figure
                    sub=fig.add_subplot(111)
                    sub.plot(processed_data[0],processed_data[1])
                    sub.set_xlabel("Time")
                    sub.set_ylabel("Confirmed Cases")
                    sub.set_title("{}´s Growing Curve".format(country_entry.get()))
                
                else:  
                    
                    clearFrame(plot_frame)
                    #info request/query
                    api_requests_one=requests.get("https://api.covid19api.com/dayone/country/{}/status/confirmed".format(selected_country_2.get()))
                    api_day_one=json.loads(api_requests_one.content)
                    
                    for dict in api_day_one:                     
                        x_axis=(dict["Date"])
                        dates.append(x_axis)
                        y_axis=(dict["Cases"])
                        data.append((len(dates),y_axis))
                    x,y=zip(*data)
                    processed_data_2=(x,y)
                    
                    #clear entries
                    country_entry_2.delete(0,'end')
                    confirmed_entry_2.delete(0,'end')
                    deaths_entry_2.delete(0,'end')
                    recovered_entry_2.delete(0,'end')
                    active_entry_2.delete(0,'end')
                    active_entry_2.delete(0,'end')
                    date_entry_2.delete(0,'end')
                    day_number_entry_2.delete(0,'end')
                    #info request/query
                    status=requests.get("https://api.covid19api.com/live/country/{}/status/confirmed".format(selected_country_2.get()))
                    status=json.loads(status.content)
                    country_entry_2.insert(0,status[day_number]["Country"])
                    confirmed_entry_2.insert(0,status[day_number]["Confirmed"])
                    deaths_entry_2.insert(0,status[day_number]["Deaths"])
                    recovered_entry_2.insert(0,status[day_number]["Recovered"])
                    active_entry_2.insert(0,status[day_number]["Active"])
                    date_entry_2.insert(0,status[day_number]["Date"][:10])
                    
                    #activate search data by date
                    day_number_entry_2.config(state="normal")
                    day_button_2.config(state="normal")
                    
                    #add data plots to figure
                    sub1=fig.add_subplot(211)
                    sub1.plot(processed_data[0],processed_data[1])
                    sub1.set_ylabel("{}".format(country_entry.get()))
                    sub1.set_title("Covid-19 Growing Rate")
                    
                    sub2=fig.add_subplot(212)
                    sub2.plot(processed_data_2[0],processed_data_2[1])
                    sub2.set_ylabel("{}".format(country_entry_2.get()))
                    sub2.set_xlabel("Time")

            
            elif source_value.get()=="B":
                #info request/query
                api_requests_day_one=requests.get("https://api.thevirustracker.com/free-api?countryTimeline={}".format(selected_country.get()))
                api_day_one=json.loads(api_requests_day_one.content)

                dates=([*api_day_one['timelineitems'][0]])
                dates.pop()
                
                index=0
                for i in dates:
                    index+=1
                    x_axis=(index) 
                    y_axis=(api_day_one['timelineitems'][0][i]['total_cases'])
                    data.append((x_axis,y_axis))
                x,y=zip(*data)
                processed_data=(x,y)

            
                if select_second_country==False:
                    clearFrame(plot_frame)
                    #clear entries
                    country_entry.delete(0,'end')
                    confirmed_entry.delete(0,'end')
                    deaths_entry.delete(0,'end')
                    recovered_entry.delete(0,'end')
                    active_entry.delete(0,'end')
                    active_entry.delete(0,'end')
                    date_entry.delete(0,'end')
                    day_number_entry.delete(0,'end')
                    #info request/query
                    status=requests.get("https://api.thevirustracker.com/free-api?countryTimeline={}".format(selected_country.get()))
                    status=json.loads(status.content)
                    country_entry.insert(0, api_day_one['countrytimelinedata'][0]["info"]["title"])
                    confirmed_entry.insert(0, api_day_one['timelineitems'][0][dates[day_number]]["total_cases"])
                    deaths_entry.insert(0, api_day_one['timelineitems'][0][dates[day_number]]["total_deaths"])
                    recovered_entry.insert(0, api_day_one['timelineitems'][0][dates[day_number]]["total_recoveries"])
                    active_entry.insert(0, int(api_day_one['timelineitems'][0][dates[day_number]]["total_cases"])-(int(api_day_one['timelineitems'][0][dates[day_number]]["total_recoveries"])+int(api_day_one['timelineitems'][0][dates[day_number]]["total_deaths"])))
                    date_entry.insert(0,dates[day_number])
                    
                    #search dta by date
                    day_number_entry.config(state="normal")
                    day_button.config(state="normal")
                    
                    #add data plot to figure
                    sub=fig.add_subplot(111)
                    sub.plot(processed_data[0],processed_data[1])
                    sub.set_xlabel("Time")
                    sub.set_ylabel("Confirmed Cases")
                    sub.set_title("{}´s Growing Curve".format(country_entry.get()))
                
                else:  
                    
                    clearFrame(plot_frame)
                    #info request/query
                    api_requests_day_one=requests.get("https://api.thevirustracker.com/free-api?countryTimeline={}".format(selected_country_2.get()))
                    api_day_one=json.loads(api_requests_day_one.content)
                    
                    dates=([*api_day_one['timelineitems'][0]])
                    dates.pop()

                    data=[]
                    index=0
                    for i in dates:
                        index+=1
                        x_axis=(index) 
                        y_axis=(api_day_one['timelineitems'][0][i]['total_cases'])
                        data.append((x_axis,y_axis))
                    x,y=zip(*data)
                    processed_data_2=(x,y)
                    
                    #clear entries
                    country_entry_2.delete(0,'end')
                    confirmed_entry_2.delete(0,'end')
                    deaths_entry_2.delete(0,'end')
                    recovered_entry_2.delete(0,'end')
                    active_entry_2.delete(0,'end')
                    active_entry_2.delete(0,'end')
                    date_entry_2.delete(0,'end')
                    day_number_entry_2.delete(0,'end')
                    #info request/query
                    status=requests.get("https://api.thevirustracker.com/free-api?countryTimeline={}".format(selected_country_2.get()))
                    status=json.loads(status.content)
                    country_entry_2.insert(0, api_day_one['countrytimelinedata'][0]["info"]["title"])
                    confirmed_entry_2.insert(0, api_day_one['timelineitems'][0][dates[day_number]]["total_cases"])
                    deaths_entry_2.insert(0, api_day_one['timelineitems'][0][dates[day_number]]["total_deaths"])
                    recovered_entry_2.insert(0, api_day_one['timelineitems'][0][dates[day_number]]["total_recoveries"])
                    active_entry_2.insert(0, int(api_day_one['timelineitems'][0][dates[day_number]]["total_cases"])-(int(api_day_one['timelineitems'][0][dates[day_number]]["total_recoveries"])+int(api_day_one['timelineitems'][0][dates[day_number]]["total_deaths"])))
                    date_entry_2.insert(0,dates[day_number])
                    
                    #activate search data by date
                    day_number_entry_2.config(state="normal")
                    day_button_2.config(state="normal")
                    
                    #add data plots to figure
                    sub1=fig.add_subplot(211)
                    sub1.plot(processed_data[0],processed_data[1])
                    sub1.set_ylabel("{}".format(country_entry.get()))
                    sub1.set_title("Covid-19 Growing Rate")
                    
                    sub2=fig.add_subplot(212)
                    sub2.plot(processed_data_2[0],processed_data_2[1])
                    sub2.set_ylabel("{}".format(country_entry_2.get()))
                    sub2.set_xlabel("Time")
            
            
    
        except:
            mg.showinfo("Error", "Not Enough Data \nTry another data source\n or check your internet connection.")
            
        
        else:
            #add figure to canvas
            canvas=FigureCanvasTkAgg(fig, master=plot_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
            
            #pack canvas into plot_frame
            toolbar=NavigationToolbar2Tk(canvas, plot_frame)
            toolbar.update()
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
                


        
        
def clearFrame(frame):
    if frame.winfo_children()!=[]:
        for widget in frame.winfo_children():
            widget.destroy()
    else:
        wallpaperCall()
    
    
def displayMap():
    import pandas as pd
    import geopandas as gpd
    try:
        #collect data from web table
        data=pd.read_html(requests.get("https://www.ecdc.europa.eu/en/geographical-distribution-2019-ncov-cases").content)
        data=data[0][["Places reporting cases","Sum of Cases"]]
        
    except ConnectionError:
        mg.showerror("Connection Error", "No internet connection.")
        
    else:        
        #read shp file
        world_data=gpd.read_file("mapData/world_data.shp")

        #--rename countries in shp file to match the ones from web table--
        world_data.replace('Burkina Faso', 'Burkina_Faso', inplace = True)
        world_data.replace('Cape Verde', 'Cape_Verde', inplace = True)
        world_data.replace('CentralAfricanRepublic', 'Central_African_Republic', inplace = True)        
        world_data.replace('Cote d\'Ivoire', 'Cote_dIvoire', inplace = True)
        world_data.replace('Democratic Republic of the Congo', 'Democratic_Republic_of_the_Congo', inplace = True)
        world_data.replace('Equatorial Guinea', 'Equatorial_Guinea', inplace = True)
        world_data.replace('Swaziland', 'Eswatini', inplace = True)
        world_data.replace('Guinea-Bissau', 'Guinea_Bissau', inplace = True)
        world_data.replace('Libyan Arab Jamahiriya', 'Libya', inplace = True)
        world_data.replace('Sao Tome and Principe', 'Sao_Tome_and_Principe', inplace = True)
        world_data.replace('Sierra Leone', 'Sierra_Leone', inplace = True)
        world_data.replace('South Africa', 'South_Africa', inplace = True)
        #world_data.replace('Sudan', 'South_Sudan', inplace = True)
        world_data.replace('United Republic of Tanzania', 'United_Republic_of_Tanzania', inplace = True)
        world_data.replace('Western Sahara', 'Western_Sahara', inplace = True)
        world_data.replace('Antigua and Barbuda', 'Antigua_and_Barbuda', inplace = True)
        world_data.replace('Netherlands Antilles', 'Bonaire, Saint Eustatius and Saba', inplace = True)
        world_data.replace('British Virgin Islands', 'British_Virgin_Islands', inplace = True)
        world_data.replace('Cayman Islands', 'Cayman_Islands', inplace = True)
        world_data.replace('Costa Rica', 'Costa_Rica', inplace = True)
        #world_data.replace('Netherlands Antilles', 'Curaçao', inplace = True)
        world_data.replace('Dominican Republic', 'Dominican_Republic', inplace = True)
        world_data.replace('El Salvador', 'El_Salvador', inplace = True)
        world_data.replace('Falkland Islands (Malvinas)', 'Falkland_Islands_(Malvinas)', inplace = True)
        world_data.replace('Puerto Rico', 'Puerto_Rico', inplace = True)
        world_data.replace('Saint Kitts and Nevis', 'Saint_Kitts_and_Nevis', inplace = True)
        world_data.replace('Saint Lucia', 'Saint_Lucia', inplace = True)
        world_data.replace('Saint Vincent and the Grenadines', 'Saint_Vincent_and_the_Grenadines', inplace = True)
        world_data.replace('Saint Martin', 'Sint_Maarten', inplace = True)
        world_data.replace('Trinidad and Tobago', 'Trinidad_and_Tobago', inplace = True)
        world_data.replace('Turks and Caicos Islands', 'Turks_and_Caicos_islands', inplace = True)
        world_data.replace('United States', 'United_States_of_America', inplace = True)
        world_data.replace('United States Virgin Islands', 'United_States_Virgin_Islands', inplace = True)
        world_data.replace('Brunei Darussalam', 'Brunei_Darussalam', inplace = True)
        world_data.replace('Iran (Islamic Republic of)', 'Iran', inplace = True)
        world_data.replace('Lao People\'s Democratic Republic', 'Laos', inplace = True)
        world_data.replace('Burma', 'Myanmar', inplace = True)
        world_data.replace('Saudi Arabia', 'Saudi_Arabia', inplace = True)
        world_data.replace('Korea, Republic of', 'South_Korea', inplace = True)
        world_data.replace('Sri Lanka', 'Sri_Lanka', inplace = True)
        world_data.replace('Syrian Arab Republic', 'Syria', inplace = True)
        world_data.replace('Timor-Leste', 'Timor_Leste', inplace = True)
        world_data.replace('United Arab Emirates', 'United_Arab_Emirates', inplace = True)
        world_data.replace('Viet Nam', 'Vietnam', inplace = True)
        world_data.replace('Bosnia and Herzegovina', 'Bosnia_and_Herzegovina', inplace = True)
        world_data.replace('Czech Republic', 'Czechia', inplace = True)
        world_data.replace('Faroe Islands', 'Faroe_Islands', inplace = True)
        world_data.replace('Holy See(Vatican City)', 'Holy_See', inplace = True)
        world_data.replace('Isle of Man', 'Isle_of_Man', inplace = True)
        world_data.replace('Serbia', 'Kosovo', inplace = True)
        world_data.replace('Republic of Moldova', 'Moldova', inplace = True)
        world_data.replace('The former Yugoslav Republic of Macedonia', 'North_Macedonia', inplace = True)
        world_data.replace('San Marino', 'San_Marino', inplace = True)
        world_data.replace('United Kingdom', 'United_Kingdom', inplace = True)
        world_data.replace('French Polynesia', 'French_Polynesia', inplace = True)
        world_data.replace('New Caledonia', 'New_Caledonia', inplace = True)
        world_data.replace('New Zealand', 'New_Zealand', inplace = True)
        world_data.replace('Northern Mariana Islands', 'Northern_Mariana_Islands', inplace = True)
        world_data.replace('Papua New Guinea', 'Papua_New_Guinea', inplace = True)
        #world_data.replace('', 'Cases_on_an_international_conveyance_Japan', inplace = True)

        #replace column name
        data.rename(columns={"Places reporting cases":"NAME"},inplace=True)

        #combine dataframes
        combined_data=world_data.merge(data, on="NAME")
        
        #plot data
        combined_data.plot(
            column="Sum of Cases",
            cmap="YlOrRd",
            #legend=True,
            figsize=(15, 10),
            scheme='userdefined',
            classification_kwds={'bins':[10,100,500,1000,5000,10000,15000,100000,150000,1000000,1500000,2000000]}).set_title("COVID-19 MAP", loc='center')

        plt.show()


    
#error handling @day buttons command   
def get_number(str_):
    try:
        if type(str_)==str:
            return int(str_)
    except:
        return 0



#plot_wallpaper
if plot_frame.winfo_children()==[]:
    wallpaperCall()

#add  menu
menubar = tk.Menu(root)
#menu commands
# create a pulldown menu, and add it to the menu bar
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=root.quit)
filemenu.add_command(label="Source A", command=lambda:source_value.set("A"))
filemenu.add_command(label="Source B", command=lambda:source_value.set("B"))
menubar.add_cascade(label="File", menu=filemenu)
menubar.add_command(label="Update Source", command=evaluateSource)
#display menu
root.config(menu=menubar)

#left frame
#def widget
clear_screen_button=tk.Button(left_frame, text="Clear screen", relief="groove", command=lambda:clearFrame(plot_frame))
display_map_button=tk.Button(left_frame, text="Display Choropleth Map", relief="groove", command=displayMap)

#country_options defined inside evaluateSource
country_button=tk.Button(left_frame,text="LookUp Country", padx=1, pady=1, relief="groove", command=processData)
day_number_entry=tk.Entry(left_frame, state="disable", width=30)
day_button=tk.Button(left_frame, text="Insert DayN°", state="disable", padx=1, pady=1, relief="groove",
                      command=lambda:processData(day_number=(get_number(day_number_entry.get())-1)))

country_label=tk.Label(left_frame, text="Country:",padx=5, pady=2)
confirmed_label=tk.Label(left_frame, text="Confirmed:",padx=5, pady=2)
deaths_label=tk.Label(left_frame, text="Deaths:",padx=5, pady=2)
recovered_label=tk.Label(left_frame, text="Recovered:",padx=5, pady=2)
active_label=tk.Label(left_frame, text="Active:",padx=5, pady=2)
date_label=tk.Label(left_frame, text="Date:",padx=5, pady=2)


#Second Country
#country_options_2 defined inside evaluateSource
country_options_2.config( state="disable")
country_button_2=tk.Button(left_frame,text="Compare Country", padx=1, pady=1, relief="groove", state="disable",
                            command=lambda:processData(select_second_country=True))
day_number_entry_2=tk.Entry(left_frame, state="disable", width=30)
day_button_2=tk.Button(left_frame, text="Insert DayN°", padx=1, pady=1, state="disable", relief="groove",
                        command=lambda:processData(day_number=(get_number(day_number_entry_2.get())-1), select_second_country=True))

country_label_2=tk.Label(left_frame, text="Country:", state="disable",padx=5, pady=2)
confirmed_label_2=tk.Label(left_frame, text="Confirmed:", state="disable",padx=5, pady=2)
deaths_label_2=tk.Label(left_frame, text="Deaths:", state="disable",padx=5, pady=2)
recovered_label_2=tk.Label(left_frame, text="Recovered:", state="disable",padx=5, pady=2)
active_label_2=tk.Label(left_frame, text="Active:", state="disable",padx=5, pady=2)
date_label_2=tk.Label(left_frame, text="Date:", state="disable",padx=5, pady=2)


#insert/grid widget
clear_screen_button.grid(row=0,column=1, sticky="we")
display_map_button.grid(row=0, column=0, sticky="we")

#country_options inserted in evaluateSource()
country_button.grid(row=1, column=1, sticky="we")
day_number_entry.grid(row=8, column=1, sticky="we")
day_button.grid(row=8, column=0, sticky="we")

country_label.grid(row=2, column=0, sticky="e")
confirmed_label.grid(row=3, column=0, sticky="e")
deaths_label.grid(row=4, column=0, sticky="e")
recovered_label.grid(row=5, column=0, sticky="e")
active_label.grid(row=6, column=0, sticky="e")
date_label.grid(row=7, column=0, sticky="e")

country_entry.grid(row=2, column=1, columnspan=1)
confirmed_entry.grid(row=3, column=1, columnspan=1)
deaths_entry.grid(row=4, column=1, columnspan=1)
recovered_entry.grid(row=5, column=1, columnspan=1)
active_entry.grid(row=6, column=1, columnspan=1)
date_entry.grid(row=7, column=1, columnspan=1)


#second country
#country_options_2 inserted in evaluateSource()
country_button_2.grid(row=10, column=1, sticky="we")
day_number_entry_2.grid(row=17, column=1, sticky="we")
day_button_2.grid(row=17, column=0, sticky="we")

country_label_2.grid(row=11, column=0, sticky="e")
confirmed_label_2.grid(row=12, column=0, sticky="e")
deaths_label_2.grid(row=13, column=0, sticky="e")
recovered_label_2.grid(row=14, column=0, sticky="e")
active_label_2.grid(row=15, column=0, sticky="e")
date_label_2.grid(row=16, column=0, sticky="e")

country_entry_2.grid(row=11, column=1, columnspan=1)
confirmed_entry_2.grid(row=12, column=1, columnspan=1)
deaths_entry_2.grid(row=13, column=1, columnspan=1)
recovered_entry_2.grid(row=14, column=1, columnspan=1)
active_entry_2.grid(row=15, column=1, columnspan=1)
date_entry_2.grid(row=16, column=1, columnspan=1)
    

def activateSecondCountry():
    if checkbox_value.get() == 1:
        country_options_2.config(state="normal")
        country_button_2.config(state="normal")

        country_label_2.config(state="normal")
        confirmed_label_2.config(state="normal")
        deaths_label_2.config(state="normal")
        recovered_label_2.config(state="normal")
        active_label_2.config(state="normal")
        date_label_2.config(state="normal")

        country_entry_2.config(state="normal")
        confirmed_entry_2.config(state="normal")
        deaths_entry_2.config(state="normal")
        recovered_entry_2.config(state="normal")
        active_entry_2.config(state="normal")
        date_entry_2.config(state="normal")
        
    elif checkbox_value.get() == 0:
        country_options_2.config(state="disable")
        country_button_2.config(state="disable")
        day_number_entry_2.config(state="disable")
        day_button_2.config(state="disable")

        country_label_2.config(state="disable")
        confirmed_label_2.config(state="disable")
        deaths_label_2.config(state="disable")
        recovered_label_2.config(state="disable")
        active_label_2.config(state="disable")
        date_label_2.config(state="disable")

        country_entry_2.config(state="disable")
        confirmed_entry_2.config(state="disable")
        deaths_entry_2.config(state="disable")
        recovered_entry_2.config(state="disable")
        active_entry_2.config(state="disable")
        date_entry_2.config(state="disable")
second_country_checkbox=tk.Checkbutton(left_frame, text="Second Country", variable=checkbox_value,
                                        command=activateSecondCountry, onvalue=1, offvalue=0, pady=10)
second_country_checkbox.grid(row=9, column=0, columnspan=2, sticky="we")



root.mainloop()
