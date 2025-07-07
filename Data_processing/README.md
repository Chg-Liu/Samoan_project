# Data processing
This folder collected scripts for processing the Samoan dataset from the originally downloaded files to those commonly used by the analyses. 

All scripts kept the format of the output files vcf.gz or plink. bcftools and plink used in these scripts is in version 1.16 and version 1.9, respectively.
While ruuning plink, the parameter "--keep-allele-order" will be always added in the command to keep the allele order consistent with those vcf files.

From the original dataset, which is in the version of hg38, the following scripts have been run in order 

- normalize.sh: merge the multi-row records for variants with same position into a one-row multi-allelic record.
- bisnpPASS: snv with "PASS" in the column of "FILTER" and 1 alternative allele were extracted
- merge.sh: merge the Samoan dataset (output of bisnpPASS) with the 1000G dataset and also keep only snv with "PASS" in the column of "FILTER" and 1 alternative.
  For variants exsiting in one dataset while not exisiting in the other one, we fill the genotype of those variants in the dataset where they are missing by 0/0.
- phase.sh: phase the the Samoan dataset (output of bisnpPASS) and the merged dataset (output of merge.sh)
- heterozygosity.sh: calculating the heterozygosity of each individual in the Samoan dataset (output of bisnpPASS) and the merged dataset (output of merge.sh)
- exclude_het.sh: remove the individuals with heterozygosity above mean+3\*sd or below mean+3\*sd from the Samoan dataset (output of bisnpPASS) and the merged dataset (output of merge.sh) with use of king (version 2.2.7)
- kinship.sh: calculating relatedness of pairs of individuals in the Samoan dataset and the merged dataset (output of exclude_het.sh) with use of king (version 2.2.7).
- exclude_relate.sh: remove the individuals from the Samoan dataset and the merged dataset (output of exclude_het.sh) to exclude relatedness above different degree. 
- filter_missing_maf_LD.sh filter the merged dataset (output of exclude_relate.sh) by missing rate (0.02), maf (0.01 or 0.05) and LD (--indep-pairwise 50 5 0.2).
