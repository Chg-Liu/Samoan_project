f = open('../dataset/merged_phenotype/WGS_phenotype.txt','r')
A = [i.strip().split('\t') for i in f.readlines()]
f.close()

B = {i[0]:i for i in A[1:]}

f = open('../PCAIR2/pcs.tsv','r')
C = {i.split()[0]:i.split() for i in f.readlines()}
f.close()


fout = open('PCmerged_phenotype.tsv','w')
fout.write('\t'.join(A[0][:1]+['PC'+str(i) for i in range(1,6)]+A[0][1:])+'\n')

f = open('Nean_spec_intro.Samoan.normalized.bisnp.PASS.D1_het.fam','r')
while True:
    a = f.readline().split()
    if not a:
        break
    fout.write('\t'.join([a[1]]+C[a[1]][1:6]+B[a[1]][1:])+'\n')

f.close()
fout.close()


