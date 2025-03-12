import os,sys

Info={}

infofile='/gpfs/gibbs/pi/tucci/cl2549/02_Samoa/preliminary_analysis/sample_info/sample_info.txt'
f=open(infofile,'r')
while True:
	a=f.readline().strip()
	if not a:
		break
	a = a.split('\t')
	if ' ' in a[-1]:
		a[-1] = '_'.join(a[-1].split(' '))
	Info[a[0]]=a[int(sys.argv[3])]
f.close()

f=open(sys.argv[1]+'.ped','r')
fout=open(sys.argv[2]+'.replaced.ped','w')
Arch = ['AltaiNeandertal','Vindija33.19','Chagyrskaya-Phalanx','Denisova']
while True:
	a=f.readline()
	if len(a)<1000:
		break
	k=0
	x = []
	while True:
		if a[k]==' ':
			x.append(k)
		if len(x) == 2:
			break
		k += 1

	if a[x[0]+1:x[1]] in Info.keys():
		b = Info[a[x[0]+1:x[1]]]
	elif a[x[0]+1:x[1]] in Arch:
		b = a[x[0]+1:x[1]].split('-')[0]
	else:
		b = 'Chimpanzee'
	fout.write(b+' '+a[x[0]:])
	
os.system('cp '+sys.argv[1]+'.map '+sys.argv[2]+'.replaced.map')
f.close()
fout.close()
