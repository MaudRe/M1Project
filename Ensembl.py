import requests, sys,re

def Ensembl_id(organism,gene):
	list_res=[]
	server = "https://rest.ensembl.org"
	ext = "/xrefs/symbol/{}/{}?".format(organism, gene)
	r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
	
	if not r.ok:
		server = "https://rest.ensemblgenomes.org"
		ext = "/xrefs/symbol/{}/{}?".format(organism, gene)
		r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
 		
	decoded = r.json()
	#print(len(decoded))
	list_res.append(decoded[0]['id'])
	if len(decoded) !=1:
		#print(decoded[1]['id'])
		list_res.append(decoded[1]['id'])
	#print(list_res)
	return list_res

def Ens_trans(Id):
 
	server = "https://rest.ensembl.org"
	ext = "/lookup/id/{}?expand=1".format(Id)
 
	r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
 
	if not r.ok:
		server = "https://rest.ensemblgenomes.org"
		ext = "/lookup/id/{}?expand=1".format(Id)
		r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})

 
	decoded = r.json()
	return decoded['Transcript']
