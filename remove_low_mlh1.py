'''
Remove samples with low MLH1 rna expression
'''

import csv
import sys

join_filename = "data/join_samples.csv"

reader = csv.DictReader(open(join_filename)) 
fieldnames = reader.fieldnames
writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
writer.writeheader()


# chosen by observing the distribution of MLH1 RNA exression levels
threshold = 1.5

for row in reader:
    mlh1 = float(row['mlh1_log_norm'])
    if mlh1 >= threshold:
        writer.writerow(row)
