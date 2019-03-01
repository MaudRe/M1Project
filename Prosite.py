import requests
import re

def Graph(Id_Uni):
	result=[]
	for Id in Id_Uni:
		url = "https://prosite.expasy.org/cgi-bin/prosite/PSScan.cgi?seq={}".format(Id)
		r = requests.get(url)
		if r.ok:
			page = r.text
			graph_link = re.findall("<a href=\"(.*)\">Graphical view</a>",page)
			if graph_link[0] not in result:
				result.append(graph_link[0])
	return result



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
				res='<a href=\"{0}{2}\">{1} : {2}</a>'.format(url, id, acc)
				if res not in result:
					result.append('<a href=\"{0}{2}\">{1} : {2}</a>'.format(url, id, acc)) 
				i = i + 1
		else:
			result.append('No Data Available \n')
	return(result)

