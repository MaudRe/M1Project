# !/chemin/python
import requests 
import re



f=open('GeneSymbols.txt','r')
lignes=f.readlines()
#print(lignes)
f.close()
genes=[]
organism=[]

for i in lignes:
	i=i[:-1] #enlever les \n
	tmp=i.split("\t")
	genes.append(tmp[0])
	organism.append(tmp[1])
'''print(genes[7])
print(organism[7])'''

header={'Content-Type': 'application/x-www-form-urlencoded'}
'''for i in liste:
	url = 'http://www.rcsb.org/pdb/rest/search'
  
        data= """
        <orgPdbQuery>
        <queryType>org.pdb.query.simple.UpAccessionIdQuery</queryType>
        <accessionIdList>""" + i + """</accessionIdList>
        </orgPdbQuery>
        """
	response = requests.post(url, data=data, headers=header)
	print response'''


url = 'http://www.rcsb.org/pdb/rest/search'
  
data= """
<orgPdbQuery>
<queryType>org.pdb.query.simple.UpAccessionIdQuery</queryType>
<accessionIdList>P50225</accessionIdList>
</orgPdbQuery>
"""
response = requests.post(url, data=data, headers=header)
print(response)
