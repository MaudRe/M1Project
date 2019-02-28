import requests


def string_parse(Id_Uni):
	list_id_fonctionnel=[]
	url = "https://string-db.org/api/highres_image/network?identifiers="
	for Id in Id_Uni:
		r=requests.get(url+Id)
		if r.ok:
			list_id_fonctionnel.append(Id)
	return(list_id_fonctionnel,url)

