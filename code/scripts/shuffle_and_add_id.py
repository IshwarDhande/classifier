import csv
import random
import os

dirs = [
    '/home/eshwar/code/response/code/data/master/dataset_1',
    '/home/eshwar/code/response/code/data/master/dataset_2'
]

files = ['train.csv', 'val.csv', 'test.csv']

for d in dirs:
    for f in files:
        filepath = os.path.join(d, f)
        if not os.path.exists(filepath):
            continue
            
        with open(filepath, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)
            rows = list(reader)
            
        # Randomly shuffle rows
        random.seed(42) # Set seed for reproducibility, though not strictly required
        random.shuffle(rows)
        
        # Add serial_id to header
        new_header = ['serial_id'] + header
        
        # Write back to the same file
        with open(filepath, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(new_header)
            for i, row in enumerate(rows, start=1):
                serial = f"{i:03d}"
                writer.writerow([serial] + row)
                
        print(f"Shuffled and added serial_id to {filepath}")
