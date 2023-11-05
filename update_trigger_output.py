import time
import pandas as pd
# import json

def generate_jsonl_file(csvFile):
    column_names = csvFile.columns
    
    with open('data/data.jsonl', 'w') as f:
        for row in range(len(csvFile)):
            print(column_names)
            print(csvFile.iat[row, 0])
            print()
            inner_dict_str = str({column_names[i]: csvFile.iat[row,i] for i in range(len(column_names))})
            outer_json_str = '{"doc": "' + inner_dict_str.replace('"', '\\"') + '"}'
            f.write(outer_json_str + '\n')

# Initialize last_known_row_count
last_known_row_count = 0


while True:  
    # Check current row count
    csvFile = pd.read_csv('30Days_Commodity_Prices.csv')
    current_row_count = len(csvFile)
    
    # Compare with last known row count
    if current_row_count != last_known_row_count:
        generate_jsonl_file(csvFile)
        last_known_row_count = current_row_count
    else:
        time.sleep(1)
