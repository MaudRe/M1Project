import re
import requests
from uniprot import uniprot_parse
from PDB import PDB_parse
from Ensembl import Ensembl_id,Ens_trans,Orthologs
from NCBI import *
from String import string_parse
from Go import *
from Prosite import *


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
#-------------------------------------------------------------------------------------------	
	outputfile.write("<td>") #gene Symbol
	outputfile.write(gene)
	outputfile.write("</td>")
#-------------------------------------------------------------------------------------------
	outputfile.write("<td>") #Specie
	outputfile.write(organism)
	outputfile.write("</td>")
#-------------------------------------------------------------------------------------------
	print("NCBI...."+'\n')
	outputfile.write("<td>") #Gene NCBI
	outputfile.write('<a href="https://www.ncbi.nlm.nih.gov/gene/{0}">{0}</a>'.format(Gene(gene,organism)[0][0]))
	outputfile.write(" : ")
	outputfile.write(Gene(gene,organism)[1][0])
	if len(Gene(gene,organism)[0]) !=1 :
		outputfile.write("<br>")

		outputfile.write('<a href="https://www.ncbi.nlm.nih.gov/gene/{0}">{0}</a>'.format(Gene(gene,organism)[0][1]))
		outputfile.write(" : ")
		outputfile.write(Gene(gene,organism)[1][1])
	outputfile.write("</td>")
#-------------------------------------------------------------------------------------------
	outputfile.write("<td>") #Transcript id Refseq
	print("Transcript Refseq....."+'\n')
	list_id=refseq_fct("nucleotide", "M", organism, gene)
	if len(list_id) != 0:				
		for id_ref in list_id:
			if "NM" in id_ref:
				ucsc_url = "http://genome.ucsc.edu/cgi-bin/hgTracks?org={}&position={}".format(organism, id_ref)
				outputfile.write('<a href="https://www.ncbi.nlm.nih.gov/nuccore/{0}">{0}</a><br>\n'.format(id_ref, ucsc_url))
			else:
				outputfile.write('<a href="https://www.ncbi.nlm.nih.gov/nuccore/{0}">{0}</a><br>\n'.format(id_ref))
	else:
		outpufile.write('No data available\n')

	outputfile.write("</td>")
#-------------------------------------------------------------------------------------------
	outputfile.write("<td>") #Proteins id Refseq
	print("Proteine Refseq....."+'\n')
	list_id_prot=refseq_fct("protein", "P", organism, gene)
	if len(list_id_prot) != 0:				
		for id_ref in list_id_prot:
			if "NM" in id_ref:
				ucsc_url = "http://genome.ucsc.edu/cgi-bin/hgTracks?org={}&position={}".format(organism, id_ref)
				outputfile.write('<a href="https://www.ncbi.nlm.nih.gov/nuccore/{0}">{0}</a><br>\n'.format(id_ref, ucsc_url))
			else:
				outputfile.write('<a href="https://www.ncbi.nlm.nih.gov/nuccore/{0}">{0}</a><br>\n'.format(id_ref))
		outputfile.write('</td>\n')
	else:
		outpufile.write('No data available\n')
	outputfile.write("</td>") 
#-------------------------------------------------------------------------------------------
	outputfile.write("<td>") #KEGG id
	outputfile.write("Coming Soon")
	outputfile.write("</td>")
#-------------------------------------------------------------------------------------------
	outputfile.write("<td>") #KEGG Pathway
	outputfile.write("Coming Soon")
	outputfile.write("</td>")
#-------------------------------------------------------------------------------------------
	print("Gene id Ensembl...."+'\n')
	
	outputfile.write("<td>") #Gene id
	ID_Ens=[]
	ID_Ens=Ensembl_id(organism,gene)
	#print(ID_Ens)
	outputfile.write(ID_Ens[0])
	outputfile.write("<br>")
	outputfile.write(str(Orthologs(ID_Ens[0],organism)))
	if len(ID_Ens)!=1:
		outputfile.write('\n')
		outputfile.write("<br>")
		outputfile.write(ID_Ens[1])
		outputfile.write("<br>")
		outputfile.write(str(Orthologs(ID_Ens[1],organism)))

	outputfile.write("</td>")


#-------------------------------------------------------------------------------------------
	print("Transcript Ensembl.."+'\n')
	outputfile.write("<td>") #Transcript
	Transc=Ens_trans(ID_Ens[0])

	for j in range(0,len(Transc)):
			outputfile.write(Transc[j]['id'])
			outputfile.write('\n')
			outputfile.write("<br>")
	outputfile.write("</td>")
	
	print('Proteins Ensembl.....'+'\n')

#-------------------------------------------------------------------------------------------
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
#-------------------------------------------------------------------------------------------
	print('Id Uniprot.....'+'\n')

	outputfile.write("<td>") #Uniprot
	Id_Uni=uniprot_parse(gene,organism)[0]
	for Id in Id_Uni:
		#print(Id)
		outputfile.write(Id)
		outputfile.write('\n')
		outputfile.write("<br>")
	outputfile.write("</td>")
#-------------------------------------------------------------------------------------------
	outputfile.write("<td>") #Protein name UNIPROT
	liste=uniprot_parse(gene,organism)[1]
	for name in liste:
		outputfile.write(name+"<br>")
	outputfile.write("</td>")
#-------------------------------------------------------------------------------------------
	outputfile.write("<td>") #Biological Process
	print("Go Biological Process..."+'\n')
	for name in go(Id_Uni,'biological_process'):
		outputfile.write(name+'<br>')
	outputfile.write("</td>")
#-------------------------------------------------------------------------------------------
	outputfile.write("<td>") #Molecular fonction
	print("Go Molecular Function..."+'\n')
	for name in go(Id_Uni,'molecular_function'):
		outputfile.write(name+'<br>')
	outputfile.write("</td>")

#-------------------------------------------------------------------------------------------
	outputfile.write("<td>") #Cellular Component
	print("Go Cellular Component..."+'\n')
	for name in go(Id_Uni,'cellular_component'):
		outputfile.write(name+'<br>')
	outputfile.write("</td>")
#-------------------------------------------------------------------------------------------
	print('PDB id.....'+'\n')
	outputfile.write("<td>") #PDB id
	lists=PDB_parse(Id_Uni)
	if len(lists[0]) != 0:
		for k in range(0,len(lists[0])):
			outputfile.write(lists[0][k]+" : "+lists[1][k]+'\n'+"<br>")
	else:
		outputfile.write("No Data Available"+'\n'+"<br>")
	outputfile.write("</td>")
#-------------------------------------------------------------------------------------------
	print("String..."+'\n')
	outputfile.write("<td>") #Interactions (STRING)
	res=string_parse(Id_Uni)[0]
	url=string_parse(Id_Uni)[1]
	for Id in res:
		outputfile.write('<a href="{0}{1}">{1} interaction map </a><br>'.format(url,Id))
	outputfile.write("</td>")
#-------------------------------------------------------------------------------------------
	outputfile.write("<td>") #PROSITE id
	print("Prosite....")
	for Id in Prosite(Id_Uni):
		outputfile.write(Id+'<br>')
	outputfile.write("</td>")
#-------------------------------------------------------------------------------------------
	outputfile.write("<td>") #PFAM id
	outputfile.write("Coming Soon")
	outputfile.write("</td>")
#-------------------------------------------------------------------------------------------
	outputfile.write("</tr>")
end_file=open('Endtable.html','r')
outputfile.write(end_file.read())
outputfile.write("</html>")


