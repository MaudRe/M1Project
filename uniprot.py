# !/chemin/python
import requests 
import re

def uniprot_parse(gene,organism):
	ID=[] 
	list_Name=[] 
	url = "http://www.uniprot.org/uniprot/"
	payload = {
		'query': 'gene_exact:' + gene + ' AND organism:' + organism,
		'format': 'tab',
		'columns': 'id,protein_names,organism,reviewed',
	}
	result = requests.get(url, params=payload)
	result=result.text
	resultat=result.split('\n')
	del resultat[0]
	n=len(resultat)
	for j in range(0,n-1):
		donnee=resultat[j]
		result2=donnee.split('\t')
		result2[1]=re.sub('(\((.*)\))','',result2[1])
		ID.append(result2[0])
		list_Name.append(result2[1])
	return ID,list_Name

