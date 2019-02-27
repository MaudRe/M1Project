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
	r4=requests.get("https://rest.ensembl.org/homology/id/{}?format=condensed;type=orthologues;content-type=application/json".format(id_ens))
	result=r4.json()

	if len(result["data"])==0:
		r4=requests.get("https://rest.ensemblgenomes.org/homology/id/{}?format=condensed;type=orthologues;content-type=application/json".format(id_ens))
		result=r4.json()

	
	
	if len(result["data"][0]["homologies"])>1:
		r3 = requests.get("http://protists.ensembl.org/{}/Gene/Compara_Ortholog?db=core;g={}".format(organism, id_ens))
		#print("1",r3.ok)
		if not r3.ok:
			r3 = requests.get("http://bacteria.ensembl.org/{}/Gene/Compara_Ortholog?db=core;g={}".format(organism, id_ens))
			#print("2",r3.ok)
			if not r3.ok:
				r3 = requests.get("http://fungi.ensembl.org/{}/Gene/Compara_Ortholog?db=core;g={}".format(organism, id_ens))
				#print("3",r3.ok)
				if not r3.ok:
					r3 = requests.get("http://metazoa.ensembl.org/{}/Gene/Compara_Ortholog?db=core;g={}".format(organism, id_ens))
					#print("4",r3.ok)
					if not r3.ok:
						r3 = requests.get("http://plants.ensembl.org/{}/Gene/Compara_Ortholog?db=core;g={}".format(organism, id_ens))
						#print("5",r3.ok)			
						if not r3.ok:
							r3 = requests.get("https://www.ensembl.org/{}/Gene/Compara_Ortholog?db=core;g={}".format(organism, id_ens))
							#print("6",r3.ok)		
		result = r3.url
	return result
