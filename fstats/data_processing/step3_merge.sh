#!/bin/sh
bcftools concat -f list1.txt -Oz -o archaic.vcf.gz --threads 8; tabix -f archaic.vcf.gz
bcftools concat -a -f list2.txt -Oz -o chim.unsorted.vcf.gz --threads 8; tabix -f chim.unsorted.vcf.gz
bcftools sort -Oz -o chim.vcf.gz chim.unsorted.vcf.gz; tabix -f chim.vcf.gz
bcftools merge -m snps --threads 8 -Oz -o combined.vcf.gz Samoan_1000G2504frz9.normalized.bisnp.PASS.D12_het.missing0.02_maf0.01_LDpruned.vcf.gz  archaic.vcf.gz chim.vcf.gz; tabix -f combined.vcf.gz
bcftools view -m 2 -M 2 -v snps --threads 8 -Oz -o combined.Samoan_1000G2504frz9.normalized.bisnp.PASS.D12_het.missing0.02_maf0.01_LDpruned.vcf.gz combined.vcf.gz; tabix -f combined.Samoan_1000G2504frz9.normalized.bisnp.PASS.D12_het.missing0.02_maf0.01_LDpruned.vcf.gz
