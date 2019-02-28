import requests
import re


def Prosite(Id_Uni):
	result=[]
	for Id in Id_Uni:
		url_rest = "https://prosite.expasy.org/cgi-bin/prosite/PSScan.cgi?seq={}&output=json".format(Id)
		r= requests.get(url_rest)
		if r.ok:
			json_result = r.json()
			i = 0
			url = "https://prosite.expasy.org/"
			while i < len(json_result["matchset"]):  
				acc = json_result["matchset"][i]["signature_ac"]  
				id = json_result["matchset"][i]["signature_id"]
				result.append('<a href=\"{0}{2}\">{1} : {2}</a>'.format(url, id, acc)) 
				i = i + 1
	return(result)

