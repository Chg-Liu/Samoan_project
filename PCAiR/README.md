# PCAiR (PCA with related samples)

[step1_runkinship.sh](step1_runkinship.sh) is used to run [king](https://www.kingrelatedness.com/history.shtml) to generate the kinship matrix. The Samoan dataset 
with heterozygosity outliers and the relatedness of duplicates and 1st degree excluded is the input. MAF filtering and LD pruning were also oparated in the Samoan dataset.

[step2_runpcair.sh] is used to run the R script [run.R](run.R) to perform PCA with the kinship matrix involved.

