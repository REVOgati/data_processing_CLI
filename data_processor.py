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

def process_data(data, filter_column, threshold):
    # Filter data (example)
    filtered_data = data[data[filter_column] > threshold]
    # Perform calculations (example)
    filtered_data['Total_Sales'] = filtered_data['Quantity'] * filtered_data['Price']
    # Group and aggregate (example)
    aggregated_data = filtered_data.groupby('Month').sum()
    return aggregated_data

#Using argparse to enable user input in CLI

def main():
    my_parser = argparse.ArgumentParser(description= "Data Cleaning and Processing Tool")
    my_parser.add_argument('input_file', help= "Path to input CSV file")
    my_parser.add_argument('output_file', help="Path to save output file")
    my_parser.add_argument('--filter_column', help='Option to define filter column', default=None)
    my_parser.add_argument('--threshold', help='Option for threshhold', default= 0)
    
    my_args = my_parser.parse_args()
    
    data = read_csv_file(my_args.input_file)
    
    if data is not None:
        cleaned_data = clean_data(data)
        processed_data = process_data(cleaned_data, my_args.filter_column, my_args.threshold)
        #save transformed data into a new csv_file
        processed_data.to_csv(my_args.output_file, index= False)
        
        printf("Data Processing complete. Saved under {my_args.output_file}")
        
""" To ensure that the main() function only runs when run directly
and Not when imported as a module in another python program """

if __name__ = "__main__":
    main()

