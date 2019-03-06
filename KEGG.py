import requests,re

def Kegg(id_NCBI):
	k_id=[]
	k_name=[]
	url = "http://rest.kegg.jp/conv/genes/ncbi-geneid:{}".format(id_NCBI)
	response = requests.get(url)
	if response.ok:
		kegg = response.text.rstrip()
		list_temp = kegg.split("\t") 
		list_kegg = list_temp[1::2]
		if len(list_kegg) != 0:
			k_id.append(list_kegg)


		for kegg_id in list_kegg: 
			url_path = "http://rest.kegg.jp/get/+{}".format(kegg_id)
			r = requests.get(url_path)
			if r.ok:
				letters = kegg_id[:3] 
				regex_path = " (" + letters + "\d{5})  (.*)" 
				list_id_name = re.findall(regex_path, r.text)
				if len(list_id_name) != 0:
					k_name.append(list_id_name)
	return k_id,k_name
