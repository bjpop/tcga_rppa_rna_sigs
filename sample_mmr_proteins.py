'''
Compute the MSH2 and MSH6 protein levels for each sample.
Only check for COAD, PRAD and UCEC cancer types

We analyse each cancer type separately, so as to compute
a z-score for that cancer type, rather than all the 3 cancers
bundled together.
'''

import csv
import sys
import scipy.stats

cancer_types = ['COAD', 'PRAD', 'UCEC']
protein_filename = "data/TCGA-PANCAN32-L4.csv"

reader = csv.DictReader(open(protein_filename))

cancer_rows = {'COAD': [], 'UCEC': [], 'PRAD': []}

for row in reader:
    cancer = row['Cancer_Type']
    if cancer in cancer_types:
        cancer_rows[cancer].append(row)

print("sample,MSH2_protein,MSH2_protein_z,MSH2_protein_low,MSH2_protein_very_low,MSH6_protein,MSH6_protein_z,MSH6_protein_low,MSH6_protein_very_low,MSH2_or_MSH6_protein_low,MSH2_or_MSH6_protein_very_low")

for cancer in cancer_rows:
    msh2_levels = []
    msh6_levels = []
    sample_levels = [] 
    rows = cancer_rows[cancer]
    for row in rows:
        sample = row['Sample_ID'][:12]
        # skip samples that don't have recoreded MSH2 or MSH6 levels
        try:
            msh2 = float(row['MSH2'])
            msh6 = float(row['MSH6'])
            sample_levels.append((sample, msh2, msh6))
            msh2_levels.append(msh2)
            msh6_levels.append(msh6)
        except:
            pass

    msh2_z_scores = scipy.stats.zscore(msh2_levels)
    msh6_z_scores = scipy.stats.zscore(msh6_levels)

    for index in range(len(sample_levels)):
        sample, msh2, msh6 = sample_levels[index]
        msh2_z = msh2_z_scores[index]
        msh6_z = msh6_z_scores[index]
        msh2_low = msh2_z <= -1.0
        msh2_very_low = msh2_z <= -1.5
        msh6_low = msh6_z <= -1.0
        msh6_very_low = msh6_z <= -1.5
        msh2_or_msh6_low = msh2_low or msh6_low
        msh3_or_msh6_very_low = msh2_very_low or msh6_very_low
        print("{},{},{},{},{},{},{},{},{},{},{}".format(sample, msh2, msh2_z, msh2_low, msh2_very_low, msh6, msh6_z, msh6_low, msh6_very_low,msh2_or_msh6_low,msh3_or_msh6_very_low))
