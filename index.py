import csv

with open('preiadeaici.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
