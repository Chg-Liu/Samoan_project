# MultiWaver 2.0 (admixture dating)

We used [MultiWaver 2.0](https://github.com/Shuhua-Group/MultiWaver2.0) to infer the admixutre model of the Samoan popualtion and estimate the admxiture time.

[step1_anc_tracts.py](step1_anc_tracts.py) convert the ancestral tracts in the output file of FLARE from the unit of base pair to the unit of Morgan.

[step2_runMultiWaver,sh](step2_runMultiWaver,sh) run Multiwaver2.0 with tracts shorter than 0.005 Morgan discarded. We used discrete model to infer the admixutre history. 100 bootstrappings have been operated.

Please see [here](https://github.com/Shuhua-Group/MultiWaver2.0/blob/master/Manual%20for%20MultiWaver%202.0.pdf) for instructions to run MultiWaver 2.0
