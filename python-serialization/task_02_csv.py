#!/usr/bin/python3

import csv
import json

def convert_csv_to_json(filename):
    try:
        ls = []
        with open(filename, 'r', newline="") as f:
            reader = csv.DictReader(f)
            for i in reader:
                ls.append(i)
  
        with open("data.json", 'w') as f:
            json.dump(ls, f)
        return True
    except Exception:
        return False
