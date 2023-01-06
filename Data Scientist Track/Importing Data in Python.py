from sqlalchemy import create_engine
import pandas as pd

# Using sqlalchemy
engine = create_engine('sqlite:///_____')
con = engine.connect()
rs = con.execute("SELECT * FROM _____")
df = pd.DataFrame(rs.fetchall())
df.columns = rs.keys()
con.close()

# Using the context manager
engine = create_engine('sqlite:///_____')

with engine.connect() as con:
    rs = con.execute('SELECT ____, ____, ____')
    df = pd.DataFrame(rs.fetchmany(size=5))
    df.columns = rs.keys()

# Few line query
engine = create_engine('sqlite:///____')
df = pd.read_sql_query('', engine)

# INNER JOIN in Python(pandas)
"SELECT Column1, ColumnA FROM Table1 INNER JOIN TableA ON Table1.ColumnZ = TableA.ColumnZ"
"SELECT OrderID, CompanyName FROM Orders INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID"

# Automate file download in Python
from urllib.request import urlretrieve
url = ''
urlretrieve(url, '.csv')

# Get requests using urllib
from urllib.request import urlopen, Request
url = 'https://en.wikipedia.org/wiki/Main_Page'
request = Request(url)
response = urlopen(request)
html = response.read()
response.close()

# Get requests using requests
import requests
url = 'https://en.wikipedia.org/'
r = requests.get(url)
text = r.text   # attribute

# Beautiful Soup
from bs4 import BeautifulSoup
import requests

url = 'https://www.crummy.com/software/BeautifulSoup/'
r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc)
soup.title   # getting the title
soup.get_text()   # getting the text

# Getting hyperlinks
for link in soup.find_all('a'): #   which define hyperlinks
    print(link.get('href'))

# JSON = JavaScript Object Notation
import json
with open('', 'r') as json_file:
    json_data = json.load(json_file)

# Using Tweepy:Authentication
import tweepy, json
access_token = '...'
access_token_secret = '...'
consumer_key = '...'
consumer_secret = '...'

stream = tweepy.Stream(consumer_key, consumer_secret, access_token, access_token_secret)
stream.filter(track=['apples', 'oranges'])

