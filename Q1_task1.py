import os
import pandas as pd 
import glob


# Q:1 and 2
csv_files_path = r'C:\Users\rosun\Desktop\python code\csvs'
output_txt_file = r'C:\Users\rosun\Desktop\python code\output.txt'
all_texts = []

# Join the folder path with the file pattern
full_pattern = os.path.join(csv_files_path, '*.csv')

# Use glob.glob with the full path
for csv_file in glob.glob(full_pattern):
    try:
        # reading file
        df = pd.read_csv(csv_file)

        # Check if the DataFrame has columns
        if not df.empty and len(df.columns) > 0:
            for row in df.values:
                for value in row:
                    all_texts.append(str(value))
        else:
            print(f"Warning: File '{csv_file}' is empty or does not contain any columns.")
    except pd.errors.EmptyDataError:
        print(f"Error: File '{csv_file}' is empty.")

with open(output_txt_file, 'w', encoding='utf-8') as txt_file:
    txt_file.write('\n'.join(all_texts))

print(f"Text from all CSV files has been extracted and stored in {output_txt_file}")

