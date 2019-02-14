import re
import requests
from uniprot import uniprot_parse
from PDB import PDB_parse
from Ensembl import Ensembl_id,Ens_trans,Orthologs


f=open('GeneSymbols.txt','r')
lignes=f.readlines()
#print(lignes)
f.close()
genes=[]
organism=[]

tempfile = open('table.html','r')
outputfile = open('index.html','w')
outputfile.write(tempfile.read())
tempfile.close()

for i in lignes:
	i=i[:-1] #enlever les \n
	i2=re.sub("(\s)$","",i)
	i3=re.sub(" ","_",i2)
	tmp=i3.split("\t")
	outputfile.write("<tr>")
	gene=tmp[0]
	organism=tmp[1]
	'''print(genes)
	print(organism)'''
	print(gene)
	
	outputfile.write("<td>") #gene Symbol
	outputfile.write(gene)
	outputfile.write("</td>")

	outputfile.write("<td>") #Specie
	outputfile.write(organism)
	outputfile.write("</td>")

	outputfile.write("<td>") #Gene NCBI
	outputfile.write("Coming Soon")
	outputfile.write("</td>")

	outputfile.write("<td>") #Transcript id
	outputfile.write("Coming Soon")
	outputfile.write("</td>")

	outputfile.write("<td>") #Proteins id
	outputfile.write("Coming Soon")
	outputfile.write("</td>") 

	outputfile.write("<td>") #KEGG id
	outputfile.write("Coming Soon")
	outputfile.write("</td>")

	outputfile.write("<td>") #KEGG Pathway
	outputfile.write("Coming Soon")
	outputfile.write("</td>")

	print("Gene id Ensembl...."+'\n')
	
	outputfile.write("<td>") #Gene id
	ID_Ens=[]
	ID_Ens=Ensembl_id(organism,gene)
	#print(ID_Ens)
	outputfile.write(ID_Ens[0])
	if len(ID_Ens)!=1:
		outputfile.write('\n')
		outputfile.write("<br>")
		outputfile.write(ID_Ens[0])	
	outputfile.write("</td>")

	print("Transcript Ensembl.."+'\n')
	outputfile.write("<td>") #Transcript
	Transc=Ens_trans(ID_Ens[0])

	for j in range(0,len(Transc)):
			outputfile.write(Transc[j]['id'])
			outputfile.write('\n')
			outputfile.write("<br>")
	outputfile.write("</td>")
	
	print('Proteins Ensembl.....'+'\n')


	outputfile.write("<td>") #Proteins
	j=0
	for j in range(0,len(Transc)):
		#print(Orthologs(ID_Ens[0]))
		if Transc[j]["biotype"]=="protein_coding" :
			#print('proteine')
			outputfile.write(Transc[j]["Translation"]["id"])		
			#print(protein)
			outputfile.write('\n')
			outputfile.write("<br>")
		else:
			outputfile.write("<br>")
	if len(ID_Ens)!=1:
		#outputfile.write('\n')
		#outputfile.write("<br>")
		#print(len(Ens_trans(idens[1])))
		for j in range(0,len(Ens_trans(ID_Ens[1]))):
			#print(Ens_trans(idens[1])[j]['id'])
			if Ens_trans(ID_Ens[1])[j]["biotype"]=="protein_coding" :
				#print('proteine')
				outputfile.write(Ens_trans(ID_Ens[1])[j]["Translation"]["id"])
				outputfile.write('\n')
				outputfile.write("<br>")
				#print(protein)
			else:
				outputfile.write("<br>")

	outputfile.write("</td>")

	print('Id Uniprot.....'+'\n')

	outputfile.write("<td>") #Uniprot
	Id_Uni=uniprot_parse(gene,organism)
	for Id in Id_Uni:
		#print(Id)
		outputfile.write(Id)
		outputfile.write('\n')
		outputfile.write("<br>")
	outputfile.write("</td>")

	outputfile.write("<td>") #GProtein name UNIPROT
	outputfile.write("Coming Soon")
	outputfile.write("</td>")

	outputfile.write("<td>") #Biological Process
	outputfile.write("Coming Soon")
	outputfile.write("</td>")

	outputfile.write("<td>") #Molecular fonction
	outputfile.write("Coming Soon")
	outputfile.write("</td>")


	outputfile.write("<td>") #Cellular Component
	outputfile.write("Coming Soon")
	outputfile.write("</td>")

	print('PDB id.....'+'\n')
	outputfile.write("<td>") #PDB id
	lists=PDB_parse(Id_Uni)
	if len(lists[0]) != 0:
		for k in range(0,len(lists[0])):
			outputfile.write(lists[0][k]+" : "+lists[1][k]+'\n'+"<br>")
	else:
		outputfile.write("No Data Available"+'\n'+"<br>")
	outputfile.write("</td>")

	outputfile.write("<td>") #Interactions (STRING)
	outputfile.write("Coming Soon")
	outputfile.write("</td>")

	outputfile.write("<td>") #PROSITE id
	outputfile.write("Coming Soon")
	outputfile.write("</td>")

	outputfile.write("<td>") #PFAM id
	outputfile.write("Coming Soon")
	outputfile.write("</td>")

	outputfile.write("</tr>")
end_file=open('Endtable.html','r')
outputfile.write(end_file.read())
outputfile.write("</html>")


