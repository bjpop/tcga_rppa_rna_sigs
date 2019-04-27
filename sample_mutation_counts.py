'''
Associate each sample with its mutation counts
'''

import csv
import sys

mutation_filename = "data/all.tcga_mutations.tsv"

reader = csv.DictReader(open(mutation_filename), delimiter='\t')

"Sample	SNVs	MS SNVs	Indels	MS Indels"

print("sample,snvs,ms_snvs,indels,ms_indels")

for row in reader:
    sample = row['Sample']
    snvs = row['SNVs']
    ms_snvs = row['MS SNVs']
    indels = row['Indels']
    ms_indels = row['MS Indels']
    print(",".join([sample, snvs, ms_snvs, indels, ms_indels]))
