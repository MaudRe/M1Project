# !/chemin/python
import requests 
import re


ID_pdb=[]
def PDB_parse(ID_list):
	list_id=[]
	list_struct=[]
	uniprot_string = ','.join(ID_list) 
	header={'Content-Type': 'application/x-www-form-urlencoded'}
	url = 'http://www.rcsb.org/pdb/rest/search'
	data="""
	<orgPdbQuery>
	<queryType>org.pdb.query.simple.UpAccessionIdQuery</queryType>
	<accessionIdList>""" + uniprot_string + """</accessionIdList>
	</orgPdbQuery>
	"""
	response = requests.post(url, data=data, headers=header)
	#print(response.text)
	if response.text != "null\n":  
		ID_pdb = re.sub('\n', ',', response.text[:-1])  
		clean_list_id = re.sub('(:\d+)', '', ID_pdb)
		id_struct = requests.get("""http://www.rcsb.org/pdb/rest/customReport.csv?pdbids=""" +clean_list_id+"""&customReportColumns=structureId,structureTitle,&format=csv""")
		list_id_struct = id_struct.text.split("<br />")
		#print(list_id_struct)
		del list_id_struct[0]  
		del list_id_struct[len(list_id_struct)-1]  
		#print(list_id_struct)
		for id_struct in list_id_struct:  
			pdb_list = id_struct.split(',')  
			id = pdb_list[0]
			clean_id = re.sub('\"', '', id)  
			list_id.append(clean_id)
			structure = pdb_list[1]
			clean_structure = re.sub('\"', '', structure) 
			list_struct.append(clean_structure)
	return list_id,list_struct
