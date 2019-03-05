import requests,re


def PFAM(Id_Uni):
	result=[]
	for Id in Id_Uni:
		url = "https://pfam.xfam.org/protein/{}?output=xml".format(Id)
		r= requests.get(url)
		if r.ok:
			rep = r.text
			id_list = re.findall("<match accession=\"(.*)\" id=\"(.*)\" type", rep)
			for id in id_list:
				if id not in result:
					result.append(id)
	return(result)


