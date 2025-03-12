import os,gzip

f = gzip.open('../HGDP_Choin_AF_261/AFannotated.lifted_over.Oceania.HGDP_SGDP_Choin.bisnpnomissing.chr3.vcf.gz','rt')
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
d = 'bcftools query -r chr3:186412645-186467939 -f "%CHROM\\t%POS\\t'+'\\t'.join(['%INFO/'+i for i in c])+'''\n" ../HGDP_Choin_AF_261/AFannotated.lifted_over.Oceania.HGDP_SGDP_Choin.bisnpnomissing.chr3.vcf.gz > LINC02020.HGDP_SGDP_Choin.AF_261.tsv'''
print(d)
os.system(d)
f = open('head_261.txt','w')
f.write('\t'.join(['CHROM','POS']+c)+'\n')
f.close()
os.system('cat head_261.txt LINC02020.HGDP_SGDP_Choin.AF_261.tsv > LINC02020.HGDP_SGDP_Choin.AF_261.tsv1')
os.system('mv LINC02020.HGDP_SGDP_Choin.AF_261.tsv1 LINC02020.HGDP_SGDP_Choin.AF_261.tsv')
os.system('rm head_261.txt')
