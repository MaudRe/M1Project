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

def Orthologs(id_ens,organism):
	db_list = ["ensembl", "plants.ensembl", "bacteria.ensembl", "fungi.ensembl", "protists.ensembl", "metazoa.ensembl"]
	for db in db_list:
		final_url = "http://{}.org/{}/Gene/Summary?db=core;g={}".format(db, organism,id_ens)
		test_url = requests.get(final_url)
		if test_url.ok: 
			result=test_url.url
			gb_link = "http://www.{}.org/{}/Location/View?db=core;g={}".format(db, organism, id_ens)
			break 
	return result,gb_link
