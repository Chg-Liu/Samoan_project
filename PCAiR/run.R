library("GENESIS")
library("SNPRelate")
library("GWASTools")

snpgdsBED2GDS(bed.fn = "/gpfs/gibbs/pi/tucci/cl2549/dataset/Samoa/bisnpPASS/Samoan.normalized.bisnp.PASS.D1_het.missing0.02_maf0.01_LDpruned.bed", 
              bim.fn = "/gpfs/gibbs/pi/tucci/cl2549/dataset/Samoa/bisnpPASS/Samoan.normalized.bisnp.PASS.D1_het.missing0.02_maf0.01_LDpruned.bim", 
              fam.fn = "/gpfs/gibbs/pi/tucci/cl2549/dataset/Samoa/bisnpPASS/Samoan.normalized.bisnp.PASS.D1_het.missing0.02_maf0.01_LDpruned.fam", 
              out.gdsfn = "Samoan.normalized.bisnp.PASS.D1_het.missing0.02_maf0.01_LDpruned.gds")

KINGmat <- kingToMatrix("Samoan.normalized.bisnp.PASS.D1_het.missing0.02_maf0.01_LDpruned.kin", estimator = "Kinship")

geno <- GdsGenotypeReader(filename = "Samoan.normalized.bisnp.PASS.D1_het.missing0.02_maf0.01_LDpruned.gds")
genoData <- GenotypeData(geno)

mypcair <- pcair(genoData,kinobj = KINGmat, divobj = KINGmat)

summary(mypcair)
plot(mypcair)
xxx <- mypcair$vectors
write.table(xxx,"pcs.tsv",sep='\t',quote=FALSE,col.names=FALSE)
