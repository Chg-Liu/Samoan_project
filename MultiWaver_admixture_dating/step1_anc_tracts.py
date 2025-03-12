import sys,os,gzip

def gedis(x,y,i):
    lastgedis = 0
    lastphdis = 0
    f1 = open('../FLARE/data/plink.chr'+str(i)+'.GRCh38.map','r')
    while True:
        a = f1.readline().split()
        if not a:
            break
        if int(x)<int(a[-1]) and int(x)>=lastphdis:
            nx = (lastgedis+(float(a[-2])-lastgedis)*(int(x)-lastphdis)/(int(a[-1])-lastphdis))/100
        if int(y)<int(a[-1]) and int(y)>=lastphdis:
            ny = (lastgedis+(float(a[-2])-lastgedis)*(int(y)-lastphdis)/(int(a[-1])-lastphdis))/100
            break
        lastphdis = float(a[-2])
        lastgedis = int(a[-1])
    f1.close()
    return nx,ny

fout = open('summary3_hap_anc.tsv','w')

for i in range(1,23):
    lastgedis = 0
    lastphdis = 0

    f = gzip.open('../FLARE5/FLARE5_ref2_minmac1.Samoan.chr'+str(i)+'.anc.vcf.gz','rt')
    f1 = open('../FLARE/data/plink.chr'+str(i)+'.GRCh38.map','r')
    p = f1.readline().split()
    curgedis = float(p[-2])
    curphdis = int(p[-1])

    while True:
        a = f.readline().split()
        if 'ANCESTRY' in a[0]:
            b = a[0].split('<')[1][:-1].split(',')
            anc = {j.split('=')[1]:j.split('=')[0] for j in b}
        if a[0][0]=='#' and a[0][1]!='#':
            ind = a
            lastanc = [0 for j in range(2*len(ind[9:]))]
            curstart = [0 for j in range(2*len(ind[9:]))]
            break
    lastpos = 0
    while True:
        a = f.readline().split()
        if not a:
            for j in range(len(curstart)):
#                x,y = gedis(curstart[j],lastpos,i)
                fout.write(str(round(curstart[j],8))+'\t'+str(round(curposgedis,8))+'\t'+anc[lastanc[j]]+'\thap'+str(j)+'\n')
            break
        if int(a[1]) >= curphdis:
            while True:
                p = f1.readline().split()
                if not p:
                    break
                lastgedis = curgedis
                lastphdis = curphdis
                curgedis = float(p[-2])
                curphdis = int(p[-1])
                if int(a[1]) >= lastphdis and int(a[1]) < curphdis:
                    break
        curposgedis = (lastgedis+(curgedis-lastgedis)*(int(a[1])-lastphdis)/(curphdis-lastphdis))/100
#        print(a[1],curposgedis)
        b = []
        for j in a[9:]:
            b += j.split(':')[1:3]
        for j,k in enumerate(b):
            if lastanc[j]==0:
                curstart[j]=curposgedis
            elif b[j] != lastanc[j]:
#                x,y = gedis(curstart[j],a[1],i)
                fout.write(str(round(curstart[j],8))+'\t'+str(round(curposgedis,8))+'\t'+anc[lastanc[j]]+'\thap'+str(j)+'\n')
                curstart[j] = curposgedis
            lastanc[j] = b[j]
        lastpos = a[1]
    print(i,'finish')
