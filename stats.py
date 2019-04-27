import sys
import csv
import scipy.stats as stats

prad_file = "data/PRAD.join_samples.csv"
ucec_file = "data/UCEC.join_samples.csv"
coad_file = "data/COAD.join_samples.csv"

def bool_to_int(b):
    if b == 'True':
        return 1
    elif b == 'False':
        return 0

def print_stats(cancer, filename):
    reader = csv.DictReader(open(filename))
    low_contingency = [[0, 0], [0, 0]]
    very_low_contingency = [[0, 0], [0, 0]]
    low_mlh1_contingency = [[0, 0], [0, 0]]
    for row in reader:
        has_mmr_sig = bool_to_int(row['has_mmr_sig'])
        msh2_or_msh6_low = bool_to_int(row['MSH2_or_MSH6_protein_low'])
        msh2_or_msh6_very_low = bool_to_int(row['MSH2_or_MSH6_protein_very_low'])
        low_mlh1 = bool_to_int(row['mlh1_low'])
        # can transpose the contingency table and still get the same answer
        #low_contingency[has_mmr_sig][msh2_or_msh6_low] += 1
        low_contingency[msh2_or_msh6_low][has_mmr_sig] += 1
        # very_low_contingency[has_mmr_sig][msh2_or_msh6_very_low] += 1
        very_low_contingency[msh2_or_msh6_very_low][has_mmr_sig] += 1
        # low_mlh1_contingency[has_mmr_sig][low_mlh1] += 1
        low_mlh1_contingency[low_mlh1][has_mmr_sig] += 1
    oddsratio_low, pvalue_low = stats.fisher_exact(low_contingency)
    oddsratio_very_low, pvalue_very_low = stats.fisher_exact(very_low_contingency)
    oddsratio_mlh1, pvalue_mlh1 = stats.fisher_exact(low_mlh1_contingency)
    print(cancer)
    print("Has MMR versus MSH2/MSH6 low protein")
    print(low_contingency)
    print("odds ratio: {}, p-value: {}".format(oddsratio_low, pvalue_low))
    print("Has MMR versus MSH2/MSH6 very low protein")
    print(very_low_contingency)
    print("odds ratio: {}, p-value: {}".format(oddsratio_very_low, pvalue_very_low))
    print("Has MMR versus low MLH1 expression")
    print(low_mlh1_contingency)
    print("odds ratio: {}, p-value: {}".format(oddsratio_mlh1, pvalue_mlh1))
    print("")

print_stats('PRAD', prad_file)
print_stats('COAD', coad_file)
print_stats('UCEC', ucec_file)
