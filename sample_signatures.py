'''
Assign mutation signatures to each sample. 
'''

import csv
import sys

signature_filename = "data/signature_profile_sample.txt"

sample_signatures = {}

# Sample IDs look like:
# TCGA.OR.A5J1 
# we join the fields to be consistent with the RPPA datah
# TCGA-OR-A5J1
# There are some non TCGA sample IDs in the data, we return them unchanged
def parse_sig_sample_id(sample_id):
    if sample_id.startswith('TCGA') and len(sample_id) == 12:
        return sample_id.replace('.', '-')
    else:
        #logging.info("Non TCGA sample ID in signature data: {}".format(sample_id))
        return sample_id


def read_sigs(sigs_filename):
    num_missing_sig_values = 0
    num_valid_sig_values = 0
    unique_samples = set()
    # sample_id->sig_name->value
    results = {}
    with open(sigs_filename) as sigs_file:
        reader = csv.DictReader(sigs_file, delimiter='\t')
        for row in reader:
            this_sample = parse_sig_sample_id(row['Tumor_Sample_Barcode'])
            unique_samples.add(this_sample)
            if this_sample not in results:
                results[this_sample] = {}
            this_signature = row['Signature']
            try:
                this_signature_value = float(row['Contribution'])
                num_valid_sig_values += 1
            except:
                this_signature_value = None
                num_missing_sig_values += 1
            if this_signature not in results[this_sample]:
                results[this_sample][this_signature] = this_signature_value
            else:
                exit_with_error("Duplicate signature {} for sample {}".format(this_signature, this_sample), EXIT_BAD_INPUT)
    #print(len(unique_samples))
    return results

signature_headings = ['Signature.{}'.format(n) for n in range(1,31)]
header = ','.join(['sample'] + signature_headings)

def print_sigs(results):
    for sample in results:
        sample_vals = []
        for sig_name in signature_headings:
           if sig_name in results[sample]:
               sig_val = results[sample][sig_name]
           else:
               sig_val = 0.0
           sample_vals.append(str(sig_val))
        print(",".join([sample] + sample_vals))
        
 
print(header)
results = read_sigs(signature_filename)
print_sigs(results)
