from collections import Counter
import re
import pandas as pd
import os

from transformers import AutoTokenizer
import string


def count_word_occurrences(file_path):
    word_counter = Counter()

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Using regular expression to extract words
            words = re.findall(r'\b\w+\b', line.lower())
            word_counter.update(words)

    # Get the top 30 most common words
    top_30_words = word_counter.most_common(30)

    return top_30_words

file_path = r'C:\Users\rosun\Desktop\python code\output.txt'
result = count_word_occurrences(file_path)

# Specifying the directory for saving the CSV file
output_directory = r'C:\Users\rosun\Desktop\output_directory'
os.makedirs(output_directory, exist_ok=True)

# Create a Pandas DataFrame
df = pd.DataFrame(result, columns=['Word', 'Count'])

# Specify the full path for saving the CSV file
csv_file_path = os.path.join(output_directory, 'word_occurrence.csv')

# Save the DataFrame to a CSV file
df.to_csv(csv_file_path, index=False)

print(f"CSV file saved at: {csv_file_path}")


# Q 3.2
def count_top_tokens(text_file_path, model_name, top_n=30):
    # Initialize the tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    CHUNK_SIZE = 1024

    # Read the text file
    with open(text_file_path, 'r', encoding='utf-8') as file:
        for chunk in iter(lambda: file.read(CHUNK_SIZE), ''):
            # Preprocess the text: Convert to lowercase and remove punctuation
            translator = str.maketrans("", "", string.punctuation)
            chunk = chunk.lower().translate(translator)

            # Tokenize the text
            tokens = tokenizer.tokenize(chunk)

            # Count the occurrences of each token
            token_counts = Counter(tokens)

            # Get the top N most common tokens
            top_tokens = token_counts.most_common(top_n)

            return top_tokens

# Example usage:
text_file_path = r'C:\Users\rosun\Desktop\python code\output.txt'
model_name = 'bert-base-uncased'  # You can replace this with any other transformer model
top_tokens = count_top_tokens(text_file_path, model_name)

# Print the top 30 tokens and their counts
print("Top 30 Tokens:")
for token, count in top_tokens:
    print(f"{token}: {count}")
