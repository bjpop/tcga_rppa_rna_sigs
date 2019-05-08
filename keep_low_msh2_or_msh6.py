'''
Only keep samples with low MSH2 or MSH6 protein expression
'''

import csv
import sys

# join_filename = "data/join_samples.csv"
join_filename = "data/join_samples_not_low_mlh1.csv" 

reader = csv.DictReader(open(join_filename)) 
fieldnames = reader.fieldnames
writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
writer.writeheader()


for row in reader:
    is_low = row['MSH2_or_MSH6_protein_low']
    if is_low == 'True': 
        writer.writerow(row)
