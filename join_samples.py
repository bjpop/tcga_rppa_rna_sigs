import csv
import sys

cancer_filename = "data/sample_cancer.csv"
#signatures_filename = "data/sample_signatures.csv"
mmr_signature_filename = "data/sample_mmr_signature.csv"
mmr_proteins_filename = "data/sample_mmr_proteins.csv"
mmr_rna_filename = "data/sample_mmr_rna.csv"
mutation_counts_filename = "data/sample_mutation_counts.csv"

cancer_types = ['COAD', 'PRAD', 'UCEC']

def read_cancer_data(filename):
    reader = csv.reader(open(filename))
    header = next(reader)[1:]
    results = {}
    for row in reader:
        sample = row[0]
        cancer = row[1]
        if cancer in cancer_types: 
            results[sample] = row[1:]
    return header, results

def read_data(filename):
    reader = csv.reader(open(filename))
    header = next(reader)[1:]
    results = {}
    for row in reader:
        sample = row[0]
        results[sample] = row[1:]
    return header, results

cancer_header, cancer_data = read_cancer_data(cancer_filename)
#signatures_header, signatures_data = read_data(signatures_filename)
mmr_signature_header, mmr_signature_data = read_data(mmr_signature_filename)
mmr_proteins_header, mmr_proteins_data = read_data(mmr_proteins_filename)
mmr_rna_header, mmr_rna_data = read_data(mmr_rna_filename)
mutation_counts_header, mutation_counts_data = read_data(mutation_counts_filename)

output_header = ",".join(["sample"] + cancer_header + mmr_signature_header + mmr_proteins_header + mmr_rna_header + mutation_counts_header)

print(output_header)

for sample in cancer_data:
    try:
        cancer = cancer_data[sample]
        mmr_signatures = mmr_signature_data[sample]
        mmr_proteins = mmr_proteins_data[sample]
        mmr_rna = mmr_rna_data[sample]
        mutation_counts = mutation_counts_data[sample]
        print(",".join([sample] + cancer + mmr_signatures + mmr_proteins + mmr_rna + mutation_counts))
    except:
        pass
