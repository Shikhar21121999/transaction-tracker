import json
import sys
from datetime import datetime

def read_json_file(path):
    print(f'reading json file: {path}')
    with open(path, 'rb') as file:
        data = json.load(file)
    return data

def update_json_file(new_data, path):
    print(f'Updating file: {path}')
    with open(path, 'w') as file:
        file.write(json.dumps(new_data, indent=4))

def print_data_summary(data):
    if type(data) is list and len(data) != 0:
        print(data[0])
    
    else:
        print(data)

def get_date_from_str(date_str: str):
    date_digs = [int(x) for x in date_str.split('/')]
    return datetime(date_digs[1], date_digs[0], date_digs[2])