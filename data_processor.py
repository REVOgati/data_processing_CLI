# program to clean and Process the data

import pandas as pd
import argparse

# : Function to read csv file and convert to dataframe

def read_csv_file(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("File could not be Found")
        return None

#Cleaning data

def clean_data(data):
    #-- Handling missing values
    data = data.dropna()
    # -- remove duplicates
    data = data.drop_duplicates()
    
    # -- converting Date column to date datatype
    data['Date']= pd.to_datetime(data['Date'])
    return data

