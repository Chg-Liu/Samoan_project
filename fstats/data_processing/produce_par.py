import sys
n = sys.argv[1]
f = open('par.PED.EIGENSTRAT.'+n,'w')
f.write('genotypename: '+n+'.replaced.ped\n')
f.write('snpname:      '+n+'.replaced.map\n')
f.write('indivname:    '+n+'.replaced.ped\n')
f.write('outputformat:    EIGENSTRAT\n')
f.write('genooutfilename:   '+n+'.geno\n')
f.write('snpoutfilename:    '+n+'.snp\n')
f.write('indoutfilename:    '+n+'.ind\n')
