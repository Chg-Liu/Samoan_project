#!/bin/sh
plink --bfile Samoan.normalized.bisnp.PASS --remove ../../../02_Samoa/preliminary_analysis/heterozygosity/exclude_het3sd_list.for_plink.txt --make-bed --keep-allele-order --out Samoan.normalized.bisnp.PASS.het 
plink --bfile Samoan_1000G2504frz9.normalized.bisnp.PASS --remove ../../../02_Samoa/preliminary_analysis/heterozygosity/exclude_het3sd_list.for_plink.txt --make-bed --out Samoan_1000G2504frz9.normalized.bisnp.PASS.het --keep-allele-order
