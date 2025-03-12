arch = ['Neanderthal','Denisovan','Ambiguous']
shortarch = ['Nean','Den','Ambi']

pheno = {'Height':'quantitative','BMI':'quantitative','Systolic_BP_Av3':'quantitative','Diastolic_BP_Av3':'quantitative','Heart_Rate':'quantitative','Diabetes_diagnosis':'binary','Heart_disease_diagnosis':'binary','BIA_BF':'quantitative','SKF_BF':'quantitative','BMI_BF':'quantitative'}

for i in range(3):
    for j in pheno.keys():
        f = open(shortarch[i]+'_'+j+'.step2_output.qvalue_added','r')
        A = [k.split() for k in f.readlines()[1:]]
        f.close()
        for k in A:
            if float(k[-1])<0.05:
                print(arch[i],j,k[0],k[1],k[-1])

