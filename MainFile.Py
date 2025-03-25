'''
Authour  : M.S.Dinesh Kumar
Date     : 25/03/2025
Purpouse : Data pipeline for Amazon Customer Review Analysis
'''

# Import the required libraries
import pandas as pd
import requests
from io import BytesIO

#Get the data from the link
url='https://docs.google.com/spreadsheets/d/1B2fF-9GKOk3HBb6I40kNnfbaNOaTeDJjhht-iDSz9r0/edit?usp=sharing'

response=requests.get(url)

data=pd.read_parquet(BytesIO(response.content),engine='pyarrow')

print(data.head())
