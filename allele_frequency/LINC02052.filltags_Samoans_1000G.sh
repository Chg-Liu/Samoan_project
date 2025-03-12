#!/bin/sh
plink --bfile /gpfs/gibbs/pi/tucci/cl2549/dataset/Samoa/bisnpPASS/Samoan.normalized.bisnp.PASS.D1_het --extract range coordinate2.txt --make-bed --keep-allele-order --out LINC02052_150k.Samoan.normalized.bisnp.PASS.D1_het
