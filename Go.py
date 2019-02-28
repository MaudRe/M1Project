import requests,re

def go(Id_Uni,go_type):
	url = "https://www.ebi.ac.uk/QuickGO/term/"

	for Id in Id_Uni:
		url_id = "https://www.ebi.ac.uk/QuickGO/services/annotation/search?includeFields=goName&aspect=" + go_type + "&geneProductId=" + Id
		r = requests.get(url_id, headers={"Accept": "application/json"})
		if r.ok:
			list_Go_Name=[]
			list_go=[]
			json_Go=r.json()
			i=0
			while i<len(json_Go['results']):  
				if json_Go['results'][i]['goId'] not in list_go:  
					list_go.append(json_Go['results'][i]['goId'])
					go_id = json_Go['results'][i]['goId']
					go_name = json_Go['results'][i]['goName']
					list_Go_Name.append('<a href="{}{}">{}</a>\n'.format(url, go_id, go_name))
				i+=1
	
	return(list_Go_Name)
	
