# !/chemin/python
import requests 
import re

f=open('GeneSymbols.txt','r')
lignes=f.readlines()
#print(lignes)
f.close()
genes=[]
organism=[]

for i in lignes:
	i=i[:-1] #enlever les \n
	i2=re.sub("(\s)$","",i)
	i3=re.sub(" ","_",i2)
	tmp=i3.split("\t")
	genes.append(tmp[0])
	organism.append(tmp[1])
print(genes)
print(organism)

def uniprot(gene_list,organism_list):
	liste=[]
	liste2=[]
	ID=[]
	#récupérer toute la liste et rajouter 

	for i in range(0,len(genes)):
		url = "http://www.uniprot.org/uniprot/"
		payload = {
			'query': 'gene_exact:' + genes[i] + ' AND organism:' + organism[i] + ' AND fragment:no',
			'format': 'tab',
			'columns': 'id,protein_names,organism,reviewed',
		}
		result = requests.get(url, params=payload)
		result=result.text
		#print(i,result)
		resultat=result.split('\n')
		print(i,resultat)
		del resultat[0]
		n=len(resultat)
		#print(n)
		#print(i,'\n')
		for j in range(0,n-1):
			donnee=resultat[j]
			#print(donnee)
			result2=donnee.split('\t')
			#print(type(donnee))
			#print(result2)
			result2[1]=re.sub('(\((.*)\))','',result2[1])
			liste2.append(result2)
			#print(j,result2)
			ID.append(result2[0])
			#print(liste2)
		liste.append(liste2)
		#print(i,liste[i][i])
	#print(liste[0][1])
	#print(liste[0][0][1])
	return ID
	


print(uniprot(genes,organism))




















	
#https://www.rcsb.org/pdb/protein/P51587?evtc=Suggest&evta=UniProtAccession&evtl=autosearch_SearchBar_querySuggest
#print(resultat2)
