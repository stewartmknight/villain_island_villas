# import dependancies
import requests
import urllib
from bs4 import BeautifulSoup as bs
from splinter import Browser
from selenium import webdriver
import time
import scrape
import pandas as pd


# Initiate Browser instance
executable_path = {"executable_path":"chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless=False)

# Visit the URL
url = "https://www.privateislandsonline.com/search?availability=sale"
browser.visit(url)

y = 0
# This is where the scrolling magic happens
while y > -1:
    # Do an incremental scroll
    y = y + 100
    browser.execute_script("window.scrollTo(0, " + str(y) + ")")
    time.sleep(.4)

    # Check current location and maximum scroll length
    max_height = browser.execute_script("return document.body.scrollHeight")
    current_height = browser.execute_script("return window.pageYOffset;")

    # Check to see if you have gotten to the bottom of the page
    difference = max_height-current_height
    if difference < 700:
        break

# Call the scrape function to get the info
df = scrape.scrape(browser)

# Send the info to a dataframe
df.to_csv("Output/island_info.csv", index=False)