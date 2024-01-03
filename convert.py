import json
import csv

# Read the text file and split paragraphs
with open('expr.txt', 'r', encoding='utf-8') as file:
    paragraphs = file.read().split('\n')

# Convert to JSON
json_data = json.dumps({'paragraphs': paragraphs}, indent=2)

# Write JSON to a file
with open('expr.json', 'w') as json_file:
    json_file.write(json_data)

# Convert to CSV
csv_data = [{'paragraph': paragraph} for paragraph in paragraphs]

# Write CSV to a file
csv_columns = ['paragraph']
csv_file = 'expr.csv'

with open(csv_file, 'w', encoding='utf-8', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_columns)
    writer.writeheader()
    for data in csv_data:
        writer.writerow(data)
