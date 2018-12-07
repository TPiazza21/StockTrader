# SEBASTIAN REVEL

import urllib2
import csv
import codecs
import math
import urllib2
from bs4 import BeautifulSoup
from datetime import datetime
import numpy

def stockScraper(name):

    dataList = []
    stockDict = {name:[]}
    # LOOKS UP STOCK PAGE
    quote_page = "https://www.nasdaq.com/symbol/" + name + "/real-time"
    page = urllib2.urlopen(quote_page)
    soup = BeautifulSoup(page, "html.parser")

    #FINDS PRICE
    priceHTML = soup.find("div", attrs={'class': "qwidget-dollar"})
    price = extractPrice(priceHTML)
    
    #FINDS PERCENT CHANGE
    percentHTML = soup.find("span", attrs={'id': "quotes_content_left__PctChange"})
    percent = extractPercent(percentHTML)
    
    #FINDS VOLUME 
    volumeHTML = soup.find("span", attrs={'id': "quotes_content_left__Volume"})
    volume = extractVolume(volumeHTML)
    volume = volume.replace(",", "")



    dataList.append(price)
    dataList.append(percent)
    dataList.append(volume)

    stockDict[name] = dataList
    print stockDict
    return stockDict

# HELPER FUNCTION TO GET PRICE 
def extractPrice(text):
    code = str(text)
    price = ""
    foundDollar = False
    for i in range(len(code)):
        if foundDollar:
            if code[i] == "<":
                return price
            price += code[i]
        if code[i] == "$":
            foundDollar = True

# HELPER FUNCTION TO GET VOLUME
def extractVolume(text):
    code = str(text)
    vol = ""
    foundVolume = False
    for i in range(len(code)):
        if foundVolume:
            if code[i] == "<":
                return vol
            vol += code[i]
        if code[i] == ">":
            foundVolume = True

# HELPER FUNCTION TO GET PERCENTCHANGE
def extractPercent(text):
    code = str(text)
    name = ""
    count = 0
    for i in range(len(code)):
        if code[i] == ">":
            count += 1
        if count == 1:
            j = 0
            while(True):
                j += 1
                if code[i+j] == "%":
                    return str(float(name)/100.0)
                else:
                    name = name + code[i+j]