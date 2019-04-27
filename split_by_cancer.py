'''
Split the joined file by cancer type
'''

import sys
import csv
import os.path

cancer_types = ['PRAD', 'UCEC', 'COAD']

# joined_filename = "data/join_samples.csv"
joined_filename = sys.argv[1]

reader = csv.reader(open(joined_filename))
header = next(reader)

cancer_data = {'PRAD': [], 'UCEC': [], 'COAD': []}

for row in reader:
    cancer = row[1]
    cancer_data[cancer].append(row)

for cancer in cancer_data:
    output_filename = os.path.join('data', cancer + '.join_samples.csv')
    output_file = open(output_filename, "w")
    print(",".join(header), file=output_file)
    for row in cancer_data[cancer]:
        print(",".join(row), file=output_file)
    output_file.close()
