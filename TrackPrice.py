"""
Amazon Product Price Tracker.

Fetches price of a certain product from the website and saves its price log in a Comma Seperated File having 
the file name with the name of product in a new folder named "Tracked Products" created at the same destination
as that of this file.

In order to change the product, copy the URL of product's amazon page and paste it in the "URL" variable.
"""

from bs4 import BeautifulSoup
import csv
import datetime
import os
import requests

currentDT = datetime.datetime.now()

#Amazon URL goes here
#URL = "https://www.amazon.in/Sony-A6000Y-Digital-16-50mm-55-210mm/dp/B00XOXFB1I/ref=sr_1_3?keywords=sony+a6000&qid=1562674094&s=electronics&sr=1-3"
URL = "https://www.amazon.in/Sony-A6000Y-Digital-16-50mm-55-210mm/dp/B00XOXFB1I/ref=asc_df_B00XOXFB1I/?tag=googleshopdes-21&linkCode=df0&hvadid=396986111700&hvpos=&hvnetw=g&hvrand=8647138198519415733&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007751&hvtargid=pla-352077303119&psc=1&ext_vrnc=hi"

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'}
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

#variables from html elements on the URL
title = soup.find(id = "productTitle").get_text()
filename = title.strip()+".csv"
price = soup.find(id = "priceblock_ourprice").get_text()
price = price[2:]
date = currentDT.strftime("%d/%m/%Y")
time = currentDT.strftime("%H:%M:%S")

row = [date, time, price]

if not os.path.exists("Tracked Products"):
    os.makedirs("Tracked Products")

dest = "Tracked Products\\"+filename

exists = os.path.isfile(dest)

if exists:
	with open(dest, 'a', newline='') as csvFile:
		writer = csv.writer(csvFile)
		writer.writerow(row)
	csvFile.close()
else:
	with open(dest, 'x', newline='') as csvFile:
		csvFile.write("Date, Time, Price (Rs.)\n")
		writer = csv.writer(csvFile)
		writer.writerow(row)
	csvFile.close()