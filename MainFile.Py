'''
Authour  : M.S.Dinesh Kumar
Date     : 25/03/2025
Purpouse : Data pipeline for Amazon Customer Review Analysis
'''

# Import the required libraries
import pandas as pd

# get the data and store it in a data set
df=pd.read_excel(r'C:\Users\HP\Desktop\Guvi\Amazon-Product-Review-Analysis\Amazon-Product-Review-Analysisustomer-Analysis\aws_data.xlsx')

# Start the data cleaning and preparation activity
# Remove the duplicates
df_no_duplicates=df.drop_duplicates()

# Drop null values
df_no_null=df_no_duplicates.dropna()

