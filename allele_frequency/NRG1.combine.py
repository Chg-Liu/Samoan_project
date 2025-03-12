f = open('../NRG1_analysis/NRG1.Samoan_1000G2504frz9.AF.tsv','r')
A = [i.split() for i in f.readlines()]
f.close()

D1 = {i[1]:i for i in A[1:] if float(i[2]) != 0}

f = open('NRG1.HGDP_SGDP_Choin.AF_261.tsv','r')
B = [i.split() for i in f.readlines()]
f.close()

D2 = {i[1]:i for i in B[1:]}

fout = open('NRG1.Samoan_1000G2504frz9_HGDP_SGDP_Choin.AF_261.tsv','w')
fout.write('\t'.join(A[0]+B[0][2:])+'\n')
for i in A[1:]:
    if i[1] in D1.keys():
        x = D1[i[1]]
        if i[1] in D2.keys():
            y = D2[i[1]][2:]
        else:
            y = ['9' for j in B[0][2:]]
            print(i)
        fout.write('\t'.join(x+y)+'\n')
fout.close()

        

