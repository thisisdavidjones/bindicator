import urllib.request
from dateutil.parser import parse

def getPage():
    response = urllib.request.urlopen()
    page = response.read()
    return(page)

def extractDate(keyString, page):
    endString = '</strong></li>'
    startpos = page.find(keyString)
    endpos = page.find(endString, startpos)
    collectionExtract = page[startpos:endpos]
    startSecondStrongPos = collectionExtract.find("on <strong>")
    dateExtract = collectionExtract[startSecondStrongPos + len("on <strong>"):999]
    return dateExtract

def parsePage(page):
    keyStrings = {
        "Domestic": '<li>Your next <strong>Domestic Waste',
        "Garden" : "<li>Your next <strong>Garden Waste",
        "Recycling": '<li>Your next <strong>Recycling'
    }

    for key, value in keyStrings.items():
        collectionDateString = extractDate(value, page)
        collectionDate = parse(collectionDateString)
        print(key, collectionDate.strftime("%A, %d %B"))





page = getPage()
parsePage(str(page))
