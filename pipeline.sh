#!/bin/bash

# echo "sample_cancer"
# python3 sample_cancer.py > data/sample_cancer.csv

# echo "sample_signatures"
# python3 sample_signatures.py > data/sample_signatures.csv

# echo "sample_mmr_signature"
# python3 sample_mmr_signature.py > data/sample_mmr_signature.csv

# echo "sample_mmr_proteins"
# python3 sample_mmr_proteins.py > data/sample_mmr_proteins.csv

# echo "sample_mmr_rna"
# python3 sample_mmr_rna.py > data/sample_mmr_rna.csv

# echo "sample_mutation_counts"
# python3 sample_mutation_counts.py > data/sample_mutation_counts.csv

# echo "join_samples"
# python3 join_samples.py > data/join_samples.csv

echo "remove low MLH1"
python3 remove_low_mlh1.py > data/join_samples_low_mlh1.csv

echo "split_by_cancer low MLH1"
python3 split_by_cancer.py data/join_samples_low_mlh1.csv

# echo "split_by_cancer"
# python3 split_by_cancer.py data/join_samples.csv
