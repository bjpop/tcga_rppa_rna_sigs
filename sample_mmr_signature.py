'''
For each sample:
   Compute total MMR signature by summing 6,15,20,26
   Check if an MMR signature is in the top 3 (non-trivial) 
   signatures for the sample
'''

import csv
import sys

signature_filename = "data/sample_signatures.csv"

signature_headings = ['Signature.{}'.format(n) for n in range(1,31)]
mmr_signatures = ['Signature.{}'.format(n) for n in [6,15,20,26]]

reader = csv.DictReader(open(signature_filename))


def has_mmr_sig(sigs):
    sig_list = sorted([(val, sig_name) for (sig_name, val) in sigs.items()], reverse=True)
    # only count a signature if its value is > 0
    top_3_sigs = [sig_name for (val, sig_name) in sig_list[:3] if val > 0.1]
    for sig_name in top_3_sigs:
        if sig_name in mmr_signatures:
            return True
    return False

header = 'sample,mmr_sig_total,has_mmr_sig'
print(header)

for row in reader:
    sample = row['sample']
    sigs = { sig_name: float(row[sig_name]) for sig_name in signature_headings }
    total_mmr_sig = sigs['Signature.6'] + sigs['Signature.15'] + sigs['Signature.20'] + sigs['Signature.26']
    this_has_mmr = has_mmr_sig(sigs)
    print(",".join([sample, str(total_mmr_sig), str(this_has_mmr)]))
