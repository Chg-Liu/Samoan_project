import os,gzip

f = gzip.open('../HGDP_Choin_AF_261/AFannotated.lifted_over.Oceania.HGDP_SGDP_Choin.bisnpnomissing.chr8.vcf.gz','rt')
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
d = 'bcftools query -r chr8:32279754-32304077 -f "%CHROM\\t%POS\\t'+'\\t'.join(['%INFO/'+i for i in c])+'''\n" ../HGDP_Choin_AF_261/AFannotated.lifted_over.Oceania.HGDP_SGDP_Choin.bisnpnomissing.chr8.vcf.gz > NRG1.HGDP_SGDP_Choin.AF_261.tsv'''
print(d)
os.system(d)
f = open('head.txt','w')
f.write('\t'.join(['CHROM','POS']+c)+'\n')
f.close()
os.system('cat head.txt NRG1.HGDP_SGDP_Choin.AF_261.tsv > NRG1.HGDP_SGDP_Choin.AF_261.tsv1')
os.system('mv NRG1.HGDP_SGDP_Choin.AF_261.tsv1 NRG1.HGDP_SGDP_Choin.AF_261.tsv')
os.system('rm head.txt')
