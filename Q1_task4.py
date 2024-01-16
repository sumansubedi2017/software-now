#Github Repository link :https://github.com/sumansubedi2017/software-now


import spacy
from transformers import pipeline
from collections import Counter

# Loading spaCy modelsp
nlp_sci = spacy.load('en_core_sci_sm')
nlp_bc5cdr = spacy.load('en_ner_bc5cdr_md')

# Loading BioBERT NER pipeline
ner_biobert = pipeline("ner", model="dmis-lab/biobert-v1.1", tokenizer="dmis-lab/biobert-v1.1")

def extract_entities_sci(text):
    doc = nlp_sci(text)
    diseases = [ent.text for ent in doc.ents if ent.label_ == 'DISEASE']
    drugs = [ent.text for ent in doc.ents if ent.label_ == 'CHEMICAL']
    return diseases, drugs

def extract_entities_bc5cdr(text):
    doc = nlp_bc5cdr(text)
    diseases = [ent.text for ent in doc.ents if ent.label_ == 'DISEASE']
    drugs = [ent.text for ent in doc.ents if ent.label_ == 'CHEMICAL']
    return diseases, drugs

def extract_entities_biobert(text):
    entities = ner_biobert(text)
    diseases = [ent['word'] for ent in entities if ent['entity'] == 'DISEASE']
    drugs = [ent['word'] for ent in entities if ent['entity'] == 'CHEMICAL']
    return diseases, drugs

# Specify the input text file
input_text_file = r'C:\Users\rosun\Desktop\python code\output.txt'

# Read the text from the input file
with open(input_text_file, 'r', encoding='utf-8') as file:
    text = file.read()

# Extract entities using spaCy models
diseases_sci, drugs_sci = extract_entities_sci(text)
diseases_bc5cdr, drugs_bc5cdr = extract_entities_bc5cdr(text)

# Extract entities using BioBERT
diseases_biobert, drugs_biobert = extract_entities_biobert(text)

# Comparing the results
common_diseases = set(diseases_sci) & set(diseases_bc5cdr) & set(diseases_biobert)
common_drugs = set(drugs_sci) & set(drugs_bc5cdr) & set(drugs_biobert)

print("Total entities detected by spaCy (en_core_sci_sm):", len(diseases_sci + drugs_sci))
print("Total entities detected by spaCy (en_ner_bc5cdr_md):", len(diseases_bc5cdr + drugs_bc5cdr))
print("Total entities detected by BioBERT:", len(diseases_biobert + drugs_biobert))

print("\nCommon diseases:", common_diseases)
print("Common drugs:", common_drugs)

# Calculating differences
differences_diseases = Counter(diseases_sci + diseases_bc5cdr + diseases_biobert) - \
                      (Counter(diseases_sci) & Counter(diseases_bc5cdr) & Counter(diseases_biobert))

differences_drugs = Counter(drugs_sci + drugs_bc5cdr + drugs_biobert) - \
                   (Counter(drugs_sci) & Counter(drugs_bc5cdr) & Counter(drugs_biobert))

print("\nDifferences in diseases:", differences_diseases)
print("Differences in drugs:", differences_drugs)
