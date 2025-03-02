import os
import pandas as pd

def combine_csv_files(input_folder1, input_folder2, output_file, encoding='utf-8'):
    """
    Reads all CSV files from a specified folder and combines them into a single CSV file.
    
    Parameters:
    - input_folder (str): Path to the folder containing CSV files.
    - output_file (str): Path to the output combined CSV file (e.g., 'combined_reviews.csv').
    - encoding (str): Encoding to use when reading CSV files (default: 'utf-8').
    
    Returns:
    - None: Saves the combined DataFrame to the output_file.
    """
    # List to hold all DataFrames
    all_dataframes = []
    
    # Check if the input folder exists
    if not os.path.exists(input_folder1):
        print(f"Error: The folder '{input_folder1}' does not exist.")
        return
    if not os.path.exists(input_folder2):
        print(f"Error: The folder '{input_folder2}' does not exist.")
        return
    
    # Get all CSV files in the folder
    csv_files_1 = [f for f in os.listdir(input_folder1) if f.endswith('.csv')]
    csv_files_2 = [f for f in os.listdir(input_folder2) if f.endswith('.csv')]
    
    if not csv_files_1:
        print(f"No CSV files found in '{input_folder1}'.")
        return
    if not csv_files_2:
        print(f"No CSV files found in '{input_folder2}'.")
        return
    
    # Read each CSV file and append to the list
    for csv_file in csv_files_1:
        file_path = os.path.join(input_folder1, csv_file)
        try:
            df = pd.read_csv(file_path, encoding=encoding)
            all_dataframes.append(df)
            print(f"Successfully read '{csv_file}' with {len(df)} rows.")
        except Exception as e:
            print(f"Error reading '{csv_file}': {e}")

    for csv_file in csv_files_2:
        file_path = os.path.join(input_folder2, csv_file)
        try:
            df = pd.read_csv(file_path, encoding=encoding)
            all_dataframes.append(df)
            print(f"Successfully read '{csv_file}' with {len(df)} rows.")
        except Exception as e:
            print(f"Error reading '{csv_file}': {e}")
    
    # Combine all DataFrames
    if all_dataframes:
        # Concatenate all DataFrames vertically (stacking rows)
        combined_df = pd.concat(all_dataframes, ignore_index=True, sort=False)
        
        # Remove duplicates if any (optional)
        combined_df = combined_df.drop_duplicates()
        
        # Save to the output file
        try:
            combined_df.to_csv(output_file, index=False, encoding=encoding)
            print(f"Combined {len(csv_files_1)+len(csv_files_2)} files into '{output_file}' with {len(combined_df)} total rows.")
        except Exception as e:
            print(f"Error saving combined CSV to '{output_file}': {e}")
    else:
        print("No data to combine.")


if __name__ == "__main__":
    # Specify the folder with your CSV files and the output file path
    input_folder_1 = r'Reviews\Jumia'
    input_folder_2 = r'Reviews\Ebay'
    input_folder_3 = r'Reviews\Shopify'
    output_file = r'all_reviews.csv'  # Adjust to your desired output path
    
    # Run the function
    combine_csv_files(input_folder_1, input_folder_2, output_file)