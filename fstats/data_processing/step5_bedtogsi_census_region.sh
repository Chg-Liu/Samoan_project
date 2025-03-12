#!/bin/sh
plink --bfile ../../dataset/merged_1000G2504frz9/combined.Samoan_1000G2504frz9.normalized.bisnp.PASS.D12_het.missing0.02_maf0.01_LDpruned --recode --out combined.Samoan_1000G2504frz9.normalized.bisnp.PASS.D12_het.missing0.02_maf0.01_LDpruned --const-fid
echo "bedtoped done"
python replace_fID.py combined.Samoan_1000G2504frz9.normalized.bisnp.PASS.D12_het.missing0.02_maf0.01_LDpruned subcombined.Samoan_1000G2504frz9.normalized.bisnp.PASS.D12_het.missing0.02_maf0.01_LDpruned 3
echo "fID replaced"
python produce_par.py subcombined.Samoan_1000G2504frz9.normalized.bisnp.PASS.D12_het.missing0.02_maf0.01_LDpruned
convertf -p par.PED.EIGENSTRAT.subcombined.Samoan_1000G2504frz9.normalized.bisnp.PASS.D12_het.missing0.02_maf0.01_LDpruned
echo "gsi converted"
python replace_pop.py subcombined.Samoan_1000G2504frz9.normalized.bisnp.PASS.D12_het.missing0.02_maf0.01_LDpruned
echo "pop replaced"
