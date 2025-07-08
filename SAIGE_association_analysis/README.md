# SAIGE (association analysis)

This folder collected all scripts related to the association analysis performed by SAIGE.

we carried out the association analysis between archaic introgressed variants and selected phenotypes using the following scrips in order:
- step1_extract.sh: archaic introgressed variants were separated into three categories (matching Neanderthal, matching Denisovan and matching both).
  We generated three dataset corresponding to the three categories by extracting the variants from the Samoan dataset.
- step2_produce_pheno.py: we merged the first five PCs and phenotypes.
- step3_GRM.sh, step4.sh and step5.sh: these three steps are the part directly running SAIGE based on https://saigegit.github.io/SAIGE-doc/.
  step3_GRM.sh is creating the sparse GRM (the section of "creat the sparse" https://saigegit.github.io/SAIGE-doc/docs/createSparseGRM.html).
  step4.sh is the step1 in the section of single variant test (https://saigegit.github.io/SAIGE-doc/docs/single_step1.html).
  step5.sh is the step2 in the section of single variant test (https://saigegit.github.io/SAIGE-doc/docs/single_step2.html).
- step6_qvaule.sh is running [qvalue.R](qvalue.R) which used the R package "qvalue" to calculate q-value.
- step7_screen.py is extracting the variants with q-value less than 0.05.

For each gene region significantly associated with diastolic blood pressure, 
we extracted the variants in each region and performed two steps (\[gene name\]_step1.sh,\[gene_name\]_step2.sh)same as step4.sh and step5.sh above 
(the section of single variant test https://saigegit.github.io/SAIGE-doc/docs/single.html).
The sparse GRM used here is same as used above (the output of step3_GRM.sh)
