# FLARE (local ancestry inference)

We used [flare_cmd.sh](flare_cmd.sh) for running FLARE with reference panels of East Asian, European and Near Ocenaic ancestires. 
The Samoan dataset used here is with heterozygosity outliers and relatedness of duplicates and 1st degree excluded. 
The ref-panel file should contain two columns of which the first is individual IDs and the second is the reference panel names.
The minimal minor allele count was specified as 1 in order to involve the varaints that are archaic introgressed while present low allele frequencies.

For more information to run flare, please see [here](https://github.com/browning-lab/flare).

We summarized the global ancestry proportion based on the results of FLARE by [summary_global_anc.py](summary_global_anc.py).
