# import dependancies
import requests
import urllib
from bs4 import BeautifulSoup as bs
from splinter import Browser
from selenium import webdriver
import time
import pandas as pd

def scrape(browser):
    # Set up SOUP object
    html = browser.html
    soup = bs(html, "html.parser")

    # Find all island by loopiing through grid object in soup
    names = []
    acres = []
    countrys = []
    links = []
    lats = []
    lngs = []
    all_spans = []

    attributes_dict = {}

    # Get the link to island
    for grid in soup.find_all(attrs={'class': 'grid-content island-content'}):

        #Get the link
        isle_link = grid.find('a')['href']
        links.append(isle_link)

        # Get the name
        name = grid.find(attrs={'class': 'name'}).text.strip()
        name = name.replace(".", "")
        
        if name in names:
            name = ("x" + name + "x")
            names.append(name)
        else:
            names.append(name)

        # Get the acreage
        try:
            acre = grid.find(attrs={'class': 'num'}).text.strip()
            acres.append(int(acre))
        except Exception:
            acres.append(0)

        # get the location
        for thing in grid.find_all(attrs={'class': 'list-name'}):
            try:
                location = thing.find_all('a')
                region = location[-1].text
                country = location[-2].text
                if region == "United States":
                    country = "United States of America"
                elif region == "Canada":
                    country = "Canada"
                elif country == "US Virgin Islands":
                    country = "United States of America"
                elif country == "French Polynesia":
                    country = "France"
                elif country == "British Virgin Islands":
                    country = "United Kingdom"
                else:
                    country = location[-2].text
                countrys.append(country)
            except Exception:
                countrys.append("NA")
        
        y = 0
        current_spans = []
        attributes_dict[name] = ['hey']
        for span in grid.find_all('span'):
            if y > 3:
                stuff = span.text.strip()
                all_spans.append(stuff)
                current_spans.append(stuff)
            y = y+1

        if len(current_spans) == 0:
            attributes_dict[name] = ["NA"]
        else:
            attributes_dict[name] = current_spans
            

    for link in links:
        browser.visit(link)

        html = browser.html
        soup = bs(html, "html.parser")

        tags = soup.find_all('div', {'class': 'hide'})
        y = 0
        for tag in tags:
            try:
                lat = tag['data-lat']
                lng = tag['data-lon']
                lats.append(lat)
                lngs.append(lng)
                y = y+1
                break
            except Exception:
                pass

    all_unique_attributes = list(dict.fromkeys(all_spans))

    island_attributes_dict = {
        "Island_Name": names,
        "Acreage": acres,
        "Country": countrys,
        "latitude": lats,
        "longitude": lngs}

    for item in all_unique_attributes:
        has_attribute_list = []
        y = 0
        for key in attributes_dict:
            if item in attributes_dict[key]:
                has_attribute_list.append("yes")
                #print(key + " has attribute " + item)
            else:
                has_attribute_list.append("no")
                #print(key + " does not have attribute " + item)
            y = y+1

        island_attributes_dict[item] = has_attribute_list

    #Create a dataframe
    df = pd.DataFrame(island_attributes_dict)

    return df