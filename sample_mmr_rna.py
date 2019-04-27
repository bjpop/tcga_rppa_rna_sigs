import sys
import math
import os

rna_dir = "data/rna_counts/"

MLH1_ensembl = "ENSG00000076242"
MSH2_ensembl = "ENSG00000095002"
MSH6_ensembl = "ENSG00000116062"
PMS2_ensembl = "ENSG00000122512"
MSH3_ensembl = "ENSG00000113318"

def trim_mean(counts):
    sorted_counts = sorted(counts)
    num_counts = len(sorted_counts)
    five_percent = int(round((num_counts / 100.0) * 5))
    trimmed_counts = sorted_counts[five_percent:-five_percent]
    result = sum(trimmed_counts) / len(trimmed_counts)
    return result

def process_file(sample, filename):
    with open(filename) as file:
        all_log_counts = []
        mlh1_count = None
        msh6_count = None
        msh2_count = None
        msh3_count = None
        pms2_count = None
        for line in file:
            gene, count = line.split()
            count = int(count)
            if count > 0:
                log_count = math.log(count, 2)
                all_log_counts.append(log_count)
                if gene.startswith(MLH1_ensembl):
                    mlh1_count = count
                if gene.startswith(MSH6_ensembl):
                    msh6_count = count
                if gene.startswith(MSH2_ensembl):
                    msh2_count = count
                if gene.startswith(MSH3_ensembl):
                    msh3_count = count
                if gene.startswith(PMS2_ensembl):
                    pms2_count = count
        trimmed_log_mean = trim_mean(all_log_counts)
        return(trimmed_log_mean, mlh1_count, msh2_count, msh6_count, msh3_count, pms2_count)

files = os.listdir(rna_dir)

results = []
for rna_filename in files:
    fields = rna_filename.split('.')
    sample = fields[0]
    trimmed_log_mean, mlh1_count, msh2_count, msh6_count, msh3_count, pms2_count = process_file(sample, os.path.join(rna_dir, rna_filename))
    norm_log_mlh1 = math.log(mlh1_count, 2) / trimmed_log_mean
    norm_log_msh2 = math.log(msh2_count, 2) / trimmed_log_mean
    norm_log_msh6 = math.log(msh6_count, 2) / trimmed_log_mean
    norm_log_msh3 = math.log(msh3_count, 2) / trimmed_log_mean
    norm_log_pms2 = math.log(pms2_count, 2) / trimmed_log_mean
    mlh1_low = norm_log_mlh1 < 1.5
    results.append((sample, str(norm_log_mlh1), str(mlh1_low), str(norm_log_msh2), str(norm_log_msh6), str(norm_log_msh3), str(norm_log_pms2)))

print("sample,mlh1_log_norm,mlh1_low,msh2_log_norm,msh6_log_norm,msh3_log_norm,pms2_log_norm")
for r in results:
    print(",".join(r))
