 Rscript /gpfs/gibbs/pi/tucci/cl2549/software/SAIGE/extdata/createSparseGRM.R       \
     --plinkFile=/gpfs/gibbs/pi/tucci/cl2549/dataset/Samoa/bisnpPASS/Samoan.normalized.bisnp.PASS.D1_het \
     --nThreads=4  \
     --outputPrefix=sparseGRM       \
     --numRandomMarkerforSparseKin=2000      \
     --relatednessCutoff=0.125
