import re,requests
from uniprot import uniprot_parse
from PDB import PDB_parse
from Ensembl import Ensembl_id,Ens_trans,Orthologs
from NCBI import Gene,refseq_fct
from String import string_parse
from Go import go
from Prosite import Graph,Prosite
from Pfam import PFAM
from KEGG import Kegg


f=open('GeneSymbols.txt','r')
lignes=f.readlines()
f.close()
genes=[]
organism=[]

tempfile = open('table.html','r')
outputfile = open('Result.html','w')
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
	print('\n|'+gene+'|\n\n')
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
	print('KEGG....\n')
	outputfile.write("<td>") #KEGG id
	id_NCBI=Gene(gene,organism)[0]
	kegg_r=Kegg(id_NCBI[0])[0]
	kegg_url = "https://www.genome.jp/dbget-bin/www_bget?"
	for list_kegg in kegg_r:
		for kegg_id in list_kegg: 
			outputfile.write("<a href=\"{0}{1}\">{1}</a><br>\n".format(kegg_url, kegg_id))
	if len(id_NCBI)!=1:
		kegg_r=Kegg(id_NCBI[1])[0]
		kegg_url = "https://www.genome.jp/dbget-bin/www_bget?"
		for list_kegg in kegg_r:
			for kegg_id in list_kegg: 
				outputfile.write("<a href=\"{0}{1}\">{1}</a><br>\n".format(kegg_url, kegg_id))
	outputfile.write("</td>")
#-------------------------------------------------------------------------------------------
	outputfile.write("<td>") #KEGG Pathway
	pathway_url = "https://www.genome.jp/kegg-bin/show_pathway?"
	kegg_r2=Kegg(id_NCBI[0])[1]
	for list_id_name in kegg_r2:
		for id_name in list_id_name:
			outputfile.write("<a href=\"{0}{1}\">{1} : {2}</a><br>\n".format(pathway_url, id_name[0], id_name[1]))
	outputfile.write("</td>")
#-------------------------------------------------------------------------------------------
	print("Gene id Ensembl...."+'\n')
	
	outputfile.write("<td>") #Gene id
	ID_Ens=[]
	ID_Ens=Ensembl_id(organism,gene)
	outputfile.write(ID_Ens[0])
	outputfile.write('\n<br>')
	if Orthologs(ID_Ens[0],organism)[0]=="FALSE":
		outputfile.write("No Ortholog<br>")
	else:
		outputfile.write('<a href='+str(Orthologs(ID_Ens[0],organism)[0])+'>Othologs</a><br>')
	outputfile.write('<a href='+str(Orthologs(ID_Ens[0],organism)[2])+'>Genome Browser</a><br>')

	if len(ID_Ens)==2:
		outputfile.write('\n<br>')
		outputfile.write(ID_Ens[1])
		outputfile.write('\n<br>')
		if Orthologs(ID_Ens[1],organism)[0]=="FALSE":
			outputfile.write("No Ortholog"+'<br>')
		else:
			outputfile.write('<a href='+str(Orthologs(ID_Ens[1],organism)[0])+'>Othologs</a><br>')
		outputfile.write('<a href='+str(Orthologs(ID_Ens[1],organism)[2])+'>Genome Browser</a>')

	outputfile.write("</td>")

#-------------------------------------------------------------------------------------------
	print("UCSC link...\n")
	outputfile.write("<td>")
	outputfile.write('<a href='+str(Orthologs(ID_Ens[0],organism)[0])+'>Genome browser</a><br>')
	outputfile.write('<a href="http://genome.ucsc.edu/cgi-bin/hgTracks?org={}">UCSC link</a>'.format(organism))
	outputfile.write("</td>")

#-------------------------------------------------------------------------------------------
	print("Transcript Ensembl.."+'\n')
	outputfile.write("<td>") #Transcript Ensembl
	Transc=Ens_trans(ID_Ens[0])
	for j in range(0,len(Transc)):
		Transcript=Transc[j]['id']
		outputfile.write('<a href=\"https://www.ensembl.org/{0}/Transcript/Summary?db=core;t={1}">{1}</a><br>\n'.format(organism,Transcript))
		outputfile.write('\n')
		outputfile.write("<br>")
	outputfile.write("</td>")
	

#-------------------------------------------------------------------------------------------
	print('Proteins Ensembl.....'+'\n')
	outputfile.write("<td>") #Proteins
	j=0
	for j in range(0,len(Transc)):
		if Transc[j]["biotype"]=="protein_coding" :
			outputfile.write('<a href=\"https://www.ensembl.org/{0}/Transcript/ProteinSummary?db=core;t={1}">{2}</a><br>\n'.format(organism, Transcript, Transc[j]["Translation"]["id"]))	
			outputfile.write('\n')
			outputfile.write("<br>")
		else:
			outputfile.write("<br>")
	if len(ID_Ens)!=1:
		for j in range(0,len(Ens_trans(ID_Ens[1]))):
			if Ens_trans(ID_Ens[1])[j]["biotype"]=="protein_coding" :
				outputfile.write(Ens_trans(ID_Ens[1])[j]["Translation"]["id"])
				outputfile.write('\n')
				outputfile.write("<br>")
			else:
				outputfile.write("<br>")

	outputfile.write("</td>")
#-------------------------------------------------------------------------------------------
	print('Id Uniprot.....'+'\n')

	outputfile.write("<td>") #Uniprot
	Id_Uni=uniprot_parse(gene,organism)[0]
	for Id in Id_Uni:
		#print(Id)
		outputfile.write('<a href= "http://www.uniprot.org/uniprot/{0}">{0}</a><br>\n'.format(Id))

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
	url_Go = "https://www.ebi.ac.uk/QuickGO/term/"
	res_Go_id=go(Id_Uni,"biological_process")[0]
	res_Go_Name=go(Id_Uni,"biological_process")[1]
	for i in range(0,len(res_Go_Name)):
		#print('<a href="{}{}">{}</a>\n'.format(url_Go, res_Go_id[i], res_Go_Name[i]))
		outputfile.write('<a href="{}{}">{}</a>\n'.format(url_Go, res_Go_id[i], res_Go_Name[i])+'<br>')
	outputfile.write("</td>")
#-------------------------------------------------------------------------------------------
	outputfile.write("<td>") #Molecular fonction
	print("Go Molecular Function..."+'\n')
	res_Go_id=go(Id_Uni,"molecular_function")[0]
	res_Go_Name=go(Id_Uni,"molecular_function")[1]
	print(res_Go_Name)
	for i in range(0,len(res_Go_Name)):
		#print('<a href="{}{}">{}</a>\n'.format(url_Go, res_Go_id[i], res_Go_Name[i]))
		outputfile.write('<a href="{}{}">{}</a>\n'.format(url_Go, res_Go_id[i], res_Go_Name[i])+'<br>')

	outputfile.write("</td>")

#-------------------------------------------------------------------------------------------
	outputfile.write("<td>") #Cellular Component
	print("Go Cellular Component..."+'\n')
	res_Go_id=go(Id_Uni,"cellular_component")[0]
	print(res_Go_id)
	res_Go_Name=go(Id_Uni,"cellular_component")[1]
	print(res_Go_Name)
	for i in range(0,len(res_Go_Name)):
		#print('<a href="{}{}">{}</a>\n'.format(url_Go, res_Go_id[i], res_Go_Name[i]))
		outputfile.write('<a href="{}{}">{}</a>\n'.format(url_Go, res_Go_id[i], res_Go_Name[i])+'<br>')

	outputfile.write("</td>")
#-------------------------------------------------------------------------------------------
	print('PDB id.....'+'\n')
	outputfile.write("<td>") #PDB id
	lists=PDB_parse(Id_Uni)
	if len(lists[0]) != 0:
		for k in range(0,len(lists[0])):
			outputfile.write('<a href="https://www.rcsb.org/structure/{0}">{0}</a>'.format(lists[0][k])+' : '+lists[1][k]+'<br>\n')
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
	print("Prosite...."+'\n')
	for Id in Prosite(Id_Uni):
		outputfile.write(Id+'<br>')
	for link in Graph(Id_Uni):
		outputfile.write('<a href="{}">Graphical View</a><br>\n'.format(link))
	outputfile.write("</td>")
#-------------------------------------------------------------------------------------------
	outputfile.write("<td>") #PFAM id
	print('Pfam...'+'\n')
	id_pfam=PFAM(Id_Uni)
	if id_pfam:
		for id_p in id_pfam:
			outputfile.write('<a href=\"https://pfam.xfam.org/family/{1}\">{0} : {1}</a><br>\n'.format(id_p[0], id_p[1]))
		outputfile.write('<a href="https://pfam.xfam.org/protein/{0}">Protein : {1} </a><br>\n'.format(Id,id_p[1]))
	outputfile.write("</td>")

#-------------------------------------------------------------------------------------------
	print("----------------------------------------------------\n")
	outputfile.write("</tr>")
end_file=open('Endtable.html','r')
outputfile.write(end_file.read())
outputfile.write("</html>")


