import requests
import re


def Gene(gene_symbol, organism):
	Name_list=[]
	url = """https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=gene&term={}[ORGN] {}[sym]&retmode=json""".format(organism, gene_symbol)
	response = requests.get(url)
	if response.ok:
		json_rep = response.json()
		list_id = json_rep["esearchresult"]["idlist"]
	for id in list_id:
		url= "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=gene&id={}&retmode=json".format(id)
		response = requests.get(url)

		if response.ok:
			decoded=response.json()
			Name_list.append(decoded['result']['{}'.format(id)]['description'])

	return(list_id,Name_list)


#result/id/description
