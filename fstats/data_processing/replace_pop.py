import os,sys


f=open(sys.argv[1]+'.ind','r')
fout=open(sys.argv[1]+'.replaced.ind','w')

while True:
	a=f.readline().split()
	if not a:
		break
	a[-1] = a[0].split(':')[0]
	fout.write('\t'.join(a)+'\n')
f.close()
fout.close()

os.system('mv '+sys.argv[1]+'.replaced.ind '+sys.argv[1]+'.ind')

