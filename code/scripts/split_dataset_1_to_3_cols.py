import csv
import os

input_file = '/home/eshwar/code/response/code/data/master/dataset_1/dataset_1.csv'
out_dir = '/home/eshwar/code/response/code/data/master/dataset_1/'

records_train = []
records_val = []
records_test = []

with open(input_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        out_row = {
            'utterance_id': row['utterance_id'],
            'utterance': row['utterance'],
            'response_category': row['response_category']
        }
        if row['split'] == 'train':
            records_train.append(out_row)
        elif row['split'] == 'validation':
            records_val.append(out_row)
        elif row['split'] == 'test':
            records_test.append(out_row)

def write_csv(filename, records):
    with open(os.path.join(out_dir, filename), 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['utterance_id', 'utterance', 'response_category'])
        writer.writeheader()
        writer.writerows(records)
        print(f"Written {len(records)} rows to {filename}")

write_csv('train.csv', records_train)
write_csv('val.csv', records_val)
write_csv('test.csv', records_test)
