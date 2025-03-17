f=open("age.txt",'r')
e=open("elig.txt",'w')
g=open("not elig",'w')
for i in f:
	h=int(i)
	if(2023-h>=18):
		print(e.write(str(h)+'\n'))
	else:
		print(g.write(str(h)+'\n'))
