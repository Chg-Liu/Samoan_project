import gzip

data = {}
chrlen = []
for i in range(1,23):
    f = gzip.open('FLARE5_ref2_minmac1.Samoan.chr'+str(i)+'.anc.vcf.gz','rt')
    while True:
        a = f.readline().split()
        if not a:
            break
        if a[0][0] == '#' and a[0][1] !='#':
            if i==1:
                Ind = a[9:]
                for x in Ind:
                    data[x]=[0,0,0]
            break
    start = int(f.readline().split()[1])
    last = 0
    while True:
        a = f.readline()
        if len(a)<10:
            end = int(last[1])
            break
        last = a.split()
    f.close()
    chrlen.append(end-start)
    f = gzip.open('FLARE5_ref2_minmac1.Samoan.chr5.global.anc.gz','rt')
    head = f.readline().split()
    while True:
        a = f.readline().split()
        if not a:
            break
        data[a[0]] = [float(a[i+1])*(end-start) + data[a[0]][i] for i in range(3)]
    f.close()
    print(i,'finish')
f = open('/gpfs/gibbs/pi/tucci/cl2549/02_Samoa/preliminary_analysis/sample_info/sample_info.txt','r')
cr = {i.split()[0]:i.split()[3] for i in f.readlines()[1:]}
Ind = sorted(Ind, key=lambda x: (cr[x],x))
for i in Ind:
    data[i] = [str(round(x/sum(chrlen),6)) for x in data[i]]

fout = open('summary_global_anc.tsv','w')
fout.write('\t'.join(head+['Census_Region'])+'\n')
fout.writelines(['\t'.join([i]+data[i]+[cr[i]])+'\n' for i in Ind])
fout.close()

