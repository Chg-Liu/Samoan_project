import os,gzip

f = gzip.open('../HGDP_Choin_AF_261/AFannotated.lifted_over.Oceania.HGDP_SGDP_Choin.bisnpnomissing.chr17.vcf.gz','rt')
while True:
    a = f.readline().split()
    if not a:
        break
    if a[0][0] == '#' and a[0][1] !='#':
        break
b = f.readline().split()
print(b[7])
c = [i.split('=')[0] for i in b[7].split(';') if i[:2]=='AF' and '_' in i and i.split('=')[0][-3:] not in ['AFR','AMR','EUR','EAS','OCN','MDE','CSA','SEA']]
print(c)
f.close()
d = 'bcftools query -r chr17:15059112-15111065 -f "%CHROM\\t%POS\\t'+'\\t'.join(['%INFO/'+i for i in c])+'''\n" ../HGDP_Choin_AF_261/AFannotated.lifted_over.Oceania.HGDP_SGDP_Choin.bisnpnomissing.chr17.vcf.gz > CDRT8.HGDP_SGDP_Choin.AF_261.tsv'''
print(d)
os.system(d)
f = open('head.txt','w')
f.write('\t'.join(['CHROM','POS']+c)+'\n')
f.close()
os.system('cat head.txt CDRT8.HGDP_SGDP_Choin.AF_261.tsv > CDRT8.HGDP_SGDP_Choin.AF_261.tsv1')
os.system('mv CDRT8.HGDP_SGDP_Choin.AF_261.tsv1 CDRT8.HGDP_SGDP_Choin.AF_261.tsv')
os.system('rm head.txt')
