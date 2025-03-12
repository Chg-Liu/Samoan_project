import os,gzip

f = gzip.open('AFannotated.CDRT8.Samoan_1000G2504frz9.normalized.bisnp.PASS.D1_het.vcf.gz','rt')
while True:
    a = f.readline().split()
    if not a:
        break
    if a[0][0] == '#' and a[0][1] !='#':
        break
b = f.readline().split()
print(b[7])
c = [i.split('=')[0] for i in b[7].split(';') if i[:2]=='AF' and '_' in i]
print(c)
f.close()
d = 'bcftools query -r chr17:15059112-15111065 -f "%CHROM\\t%POS\\t'+'\\t'.join(['%INFO/'+i for i in c])+'''\n" AFannotated.CDRT8.Samoan_1000G2504frz9.normalized.bisnp.PASS.D1_het.vcf.gz  > CDRT8.Samoan_1000G2504frz9.AF.tsv'''
print(d)
os.system(d)
f = open('head.txt','w')
f.write('\t'.join(['CHROM','POS']+c)+'\n')
f.close()
os.system('cat head.txt CDRT8.Samoan_1000G2504frz9.AF.tsv > CDRT8.Samoan_1000G2504frz9.AF.tsv1')
os.system('mv CDRT8.Samoan_1000G2504frz9.AF.tsv1 CDRT8.Samoan_1000G2504frz9.AF.tsv')
os.system('rm head.txt')
