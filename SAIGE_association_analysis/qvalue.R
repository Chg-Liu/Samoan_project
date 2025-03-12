library(qvalue)

arg = commandArgs(TRUE)
input = arg[1]
output = arg[2]

A <- read.table(input,sep='\t',header=TRUE)
A$q.value <- qvalue(A$p.value)$qvalues

write.table(A,sep='\t',file=output,quote=FALSE,row.names=FALSE)

