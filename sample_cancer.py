'''
Assign a cancer type to each sample ID.
Make sure that each sample has only one cancer type.
'''

import csv
import sys

protein_filename = "data/TCGA-PANCAN32-L4.csv"

reader = csv.DictReader(open(protein_filename))

sample_cancer = {}

print("sample,cancer")

for row in reader:
    sample = row['Sample_ID'][:12]
    cancer = row['Cancer_Type']
    if sample not in sample_cancer:
        sample_cancer[sample] = cancer
        print(",".join([sample, cancer]))
    else:
        exit("Sample {} has multiple cancers {}".format(sample, (sample_cancer[sample], cancer)))
