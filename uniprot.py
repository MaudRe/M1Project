# !/chemin/python
import requests 
import re

def uniprot_parse(gene,organism):
	liste=[]
	liste2=[]
	ID=[]
	#récupérer toute la liste et rajouter 
	url = "http://www.uniprot.org/uniprot/"
	payload = {
		'query': 'gene_exact:' + gene + ' AND organism:' + organism + ' AND fragment:no',
		'format': 'tab',
		'columns': 'id,protein_names,organism,reviewed',
	}
	result = requests.get(url, params=payload)
	result=result.text
	#print(gene,'\n',result)
	resultat=result.split('\n')
	#print(gene,'\n',resultat)
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
	#print(ID)
	#print(i,liste[i][i])
#print(liste[0][1])
#print(liste[0][0][1])
	return ID
	





















	
#https://www.rcsb.org/pdb/protein/P51587?evtc=Suggest&evta=UniProtAccession&evtl=autosearch_SearchBar_querySuggest
#print(resultat2)
