import pandas as pd 
import glob


#dataframe = pd.read_csv (r'C:\Users\rosun\Desktop\python code\*.csv')

#df to list
#all_text_data = dataframe.values.flatten()

#print(all_text_data)

#for text in all_text_data:
#    print(text)



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


