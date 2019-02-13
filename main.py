import re
import requests
#from uniprot import uniprot_parse
#from PDB import PDB_parse
from Ensembl import Ensembl_id,Ens_trans


f=open('GeneSymbols.txt','r')
lignes=f.readlines()
#print(lignes)
f.close()
genes=[]
organism=[]

tempfile = open('table.html','r')
outputfile = open('index.html','w')
outputfile.write(tempfile.read())

for i in lignes:
	i=i[:-1] #enlever les \n
	i2=re.sub("(\s)$","",i)
	i3=re.sub(" ","_",i2)
	tmp=i3.split("\t")
	genes.append(tmp[0])
	organism.append(tmp[1])
'''print(genes)
print(organism)'''

#ID=uniprot_parse(genes,organism)[0]
#liste=uniprot_parse(genes,organism)[1]

#PDB_parse(ID) #a finir
ID_Ens=[]
for i in range(0,len(genes)):
	ID_Ens.append(Ensembl_id(organism[i],genes[i]))

print(ID_Ens)

for i in ID_Ens:
	if len(i)!=1:
		print(i)
		print(len(Ens_trans(i[0])))
		for j in range(0,len(Ens_trans(i[0]))):
			print(Ens_trans(i[0])[j]['id'])
		print(len(Ens_trans(i[1])))
		for j in range(0,len(Ens_trans(i[1]))):
			print(Ens_trans(i[1])[j]['id'])
	else:
		print(i)
		print(len(Ens_trans(i[0])))
		for j in range(0,len(Ens_trans(i[0]))):
			print(Ens_trans(i[0])[j]['id'])



