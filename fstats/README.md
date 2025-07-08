# fstats

This folder collected the files for additional data processing for f-statistics and analyses of outgroup f3, Dstat and f4 ratio.

## data processing

- [step1_extract.sh](data_processing/step1_extract.sh): based on the merged dataset (the output of filter_missing_maf_LD.sh in Data processing), we extract the same variants from the archaic genomes and the chimapnzee genome.
- [step2_normalize_chim.sh](data_processing/step2_normalize_chim.sh): merge multi-row records of variants in the same position into a one-row multi-allelic record for the chimpanzee genome.
- [step3_merge.sh](data_processing/step3_merge.sh): merge Samoan_1000G dataset, the archaic genomes and the chimpanzee genome.
- [step4_bedtogsi_Samoans.sh](data_processing/step4_bedtogsi_Samoans.sh): convert the merged dataset from plink format to EIGENSOFT format.Samoan samples were labelled by "Samoans".
- [step5_bedtogsi_census_ragion.sh](data_processing/step5_bedtogsi_census_ragion.sh): convert the merged dataset from plink format to EIGENSOFT format.Samoan samples were labelled by their sensus region.

## outgroup f3, Dstat and f4 ratio

*_cmd.sh in each folder is used for performing the corresponding analysis. each analysis was performed with use of both data labelling Samoans as "Samoans" or census regions.

Please see [ADMIXTOOLS](https://github.com/DReichLab/AdmixTools) for instructions.

