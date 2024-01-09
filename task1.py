import pandas as pd 
import glob

import csv
from collections import Counter
import string


#dataframe = pd.read_csv (r'C:\Users\rosun\Desktop\python code\*.csv')

#df to list
#all_text_data = dataframe.values.flatten()

#print(all_text_data)

#for text in all_text_data:
#    print(text)


#Q:1 and 2

csv_files_path = (r'C:\Users\rosun\Desktop\python code\CSV1.csv')
output_txt_file = (r'C:\Users\rosun\Desktop\python code/output.txt')
all_texts = []


for csv_file in glob.glob(csv_files_path):
    #reading file
    df = pd.read_csv(csv_file)


    for row in df.values:
        for value in row:
            all_texts.append(str(value))
            
with open(output_txt_file, 'w', encoding='utf-8') as txt_file:
    txt_file.write('\n'.join(all_texts)) 


print(f"Text from all CSV files has been extracted and stored in {output_txt_file}")



#Q:3
texxt_file_path = r'C:\Users\rosun\Desktop\python code/output.txt'

with open(texxt_file_path, 'r', encoding='utf-8') as file:
    text = file.read()


#preprocess the text: Convert to lowercase and
translator = str.maketrans("", "", string.punctuation)
text = text.lower().translate(translator)

#tokenize the text into words
words = text.lower().translate(translator)

#tokenize the text into words
words = text.split()

#count the occurrences of each word
word_counts = Counter(words)

#get the  top 30 most coommon words
top_30_words = word_counts.most_common(30)

output_csv_path = r'C:\Users\rosun\Desktop\python code/top_30_words.csv'

with open(output_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Word', 'Count']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # Write the header
    writer.writeheader()
    
    # Write the data
    for word, count in top_30_words:
        writer.writerow({'Word': word, 'Count': count})

print(f"Top 30 common words and their counts have been stored in {output_csv_path}")