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
text_file_path = r'C:\Users\rosun\Desktop\python code/output.txt'

with open(text_file_path, 'r', encoding='utf-8') as file:
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


#Q 3.2

from transformers import AutoTokenizer
from collections import Counter
import string

def count_top_tokens(text_file_path, model_name,top_n=30 ):

    #initialize the tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    #read the text file
    with open(text_file_path, 'r', encoding = 'utf-8') as file:
        text = file.read()



     # Preprocess the text: Convert to lowercase and remove punctuation
    translator = str.maketrans("", "", string.punctuation)
    text = text.lower().translate(translator)

    # Tokenize the text
    tokens = tokenizer.tokenize(text)

    # Count the occurrences of each token
    token_counts = Counter(tokens)

    # Get the top N most common tokens
    top_tokens = token_counts.most_common(top_n)

    return top_tokens

# Example usage:
#text_file_path = 'path/to/your/textfile.txt'
model_name = 'bert-base-uncased'  # You can replace this with any other transformer model
top_tokens = count_top_tokens(text_file_path, model_name)

# Print the top 30 tokens and their counts
print("Top 30 Tokens:")
for token, count in top_tokens:
    print(f"{token}: {count}")