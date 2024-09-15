# program to clean and Process the data

import pandas as pd
import argparse

# Function to read CSV file and convert to dataframe
def read_csv_file(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("File could not be found")
        return None

# Function to clean data
def clean_data(data):
    # Check the number of rows with missing values
    rows_with_missing_values = data.isnull().any(axis=1).sum()
    
    # If more than 10% of rows have missing values, fill with mode
    if rows_with_missing_values > 0.1 * data.shape[0]:
        # Fill missing values with the mode of each column
        for column in data.columns:
            mode_value = data[column].mode()[0]  # Get the mode of the column
            data[column].fillna(mode_value, inplace=True)  # Fill missing values with mode
        print("Filled missing values with mode.")
    
    # Otherwise, drop rows with missing values
    else:
        data = data.dropna()
        print("Dropped rows with missing values.")
    
    # Remove duplicates
    data = data.drop_duplicates()
    print("Removed duplicate rows.")
    
    # Convert 'Date' column to datetime type if present
    possible_date_columns = ['DATE', 'Date', 'date']
    date_column = next((col for col in possible_date_columns if col in data.columns), None)
    
    if date_column:
        data[date_column] = pd.to_datetime(data[date_column])
        print(f"Converted '{date_column}' column to datetime.")
    else:
        print('No Date column in this dataset.')

    return data

# Using argparse to enable user input in CLI
def main():
    my_parser = argparse.ArgumentParser(description="Data Cleaning and Processing Tool")
    my_parser.add_argument('input_file', help="Path to input CSV file")
    my_parser.add_argument('output_file', help="Path to save output file")
    
    my_args = my_parser.parse_args()
    
    data = read_csv_file(my_args.input_file)
    
    if data is not None:
        cleaned_data = clean_data(data)
        
        # Save transformed data into a new CSV file
        cleaned_data.to_csv(my_args.output_file, index=False)
        
        print(f"Data cleaning complete. Saved under {my_args.output_file}")

# To ensure that the main() function only runs when run directly
if __name__ == "__main__":
    main()
