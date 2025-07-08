# allele frequency

We calculate allele frequency of variants in the regions by bcftools (filltags_HGDP_Choin.sh, \[gene_name\].filltags_Samoans_1000G.sh).

Then we extracted variants significantly assoicated with diastolic blood pressure from the tag filled dataset (\[gene_name\].extract_HGDP_Choin.py, \[gene_name\].extract_Samoans_1000G.py).

Finally, we combined the allele freqeuncies from the two datasets.(\[gene_name\].combbine.py).
