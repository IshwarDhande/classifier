import os
import csv

target_dir = '/home/eshwar/code/response/code/data/response_dataset_training'

for root, _, files in os.walk(target_dir):
    for filename in files:
        if filename.endswith('.csv'):
            filepath = os.path.join(root, filename)
            
            fieldnames = []
            new_rows = []
            has_utterance_id = False
            
            with open(filepath, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                fieldnames = reader.fieldnames
                if fieldnames and 'utterance_id' in fieldnames:
                    has_utterance_id = True
                    new_fieldnames = [field for field in fieldnames if field != 'utterance_id']
                    for row in reader:
                        new_row = {k: v for k, v in row.items() if k != 'utterance_id'}
                        new_rows.append(new_row)
                        
            if has_utterance_id:
                with open(filepath, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.DictWriter(f, fieldnames=new_fieldnames, quoting=csv.QUOTE_MINIMAL)
                    writer.writeheader()
                    writer.writerows(new_rows)
                print(f"Removed 'utterance_id' from {filepath}")
