'''
Authour  : M.S.Dinesh Kumar
Date     : 25/03/2025
Purpouse : Data pipeline for Amazon Customer Review Analysis
'''

# Import the required libraries
import pandas as pd
import re
import logging

# Function declaration
# Function to clean and format the text columns
def clean_text(text):
   # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation and special characters, keep only letters and spaces
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Remove extra spaces between words and strip leading/trailing spaces
    text = re.sub(r'\s+', ' ', text).strip()

    return text


# get the data and store it in a data set
df=pd.read_excel(r'C:\Users\HP\Desktop\Guvi\Amazon-Product-Review-Analysis\Amazon-Product-Review-Analysisustomer-Analysis\aws_data.xlsx')

# Start the data cleaning and preparation activity
# Remove the duplicates
df_no_duplicates=df.drop_duplicates()

# Drop null values
df_cleaned=df_no_duplicates.dropna()

# convert the data to correct data type
df_cleaned['star_rating']=df_cleaned['star_rating'].astype(int)
df_cleaned['review_date']=pd.to_datetime(df_cleaned['review_date'])

# standardize market place and product_category
df_cleaned['marketplace']=df_cleaned['marketplace'].astype(str)
df_cleaned['marketplace']=df_cleaned['marketplace'].str.strip()
df_cleaned['marketplace']=df_cleaned['marketplace'].str.upper()
df_cleaned['product_category']=df_cleaned['product_category'].astype(str)
df_cleaned['product_category']=df_cleaned['product_category'].str.strip()
df_cleaned['product_category']=df_cleaned['product_category'].str.lower()

#Transform the dataframe to required format
df_cleaned['review_date'] = df_cleaned['review_date'].dt.strftime('%Y-%m-%d')
df_cleaned['review_body'] = df_cleaned['review_body'].apply(clean_text)
df_cleaned['review_headline'] = df_cleaned['review_headline'].apply(clean_text)

# create new columns for easy processing
df_cleaned['review_month'] = df_cleaned['review_date'].dt.month
df_cleaned['review_year']=df_cleaned['review_date'].dt.year