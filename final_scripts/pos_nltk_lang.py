# import nltk
# from nltk.tag.stanford import StanfordPOSTagger
# st=StanfordPOSTagger('french.tagger')
# print(st.tag('Il mourut avant la naissance de son fils et sa veuve, Amina, mourut en 577 quand l’enfant n’avait que six ans ; il fut élevé par son grand-père Abd al-Muttalib et son oncle Abû Tâlib.'))
#Performing Part-of-speech tagging on all files in the Context folder
import rdflib
import nltk
from rdflib import Graph,term,Literal,XSD
from rdflib.namespace import RDFS,RDF, FOAF, NamespaceManager
import string
import os
import sys
import codecs
import pandas as pd
import re
from nltk.tag.stanford import StanfordPOSTagger

data = [
['NNP','Noun','ProperNoun'], 
['NN','Noun','Noun'], 
['NNS','Noun','NounPlural'],
['DT','DET','Determiner'], 
['JJS',	'ADJ',	'Adjective'],
['JJR',	'ADJ',	'Adjective'],
['NN',	'Noun',	'Noun'],
['NNS',	'Noun',	'NounPlural'],
['JJ',	'ADJ',	 'Adjective'],
['VB',	'Verb',	'Noun'],
['VBD',	'Verb',	'VerbPastTense'],
['VBN',	'Verb',	'VerbPastParticiple'],
['VBZ',	'Verb',	'VerbSingularPresent'],
['RB',	'ADV',	'Adverb'],
['RBR',	'ADV',	'Adverb'],
['RBS',	'ADV',	'Adverb'],
['WDT',	'DET',	'Wh-Determiner'],
['PDT',	'DET',	'Predeterminer'],
['WP',	'Pronoun',	'wh-Pronoun'],
['PRP',	'Pronoun',	'PersonalPronoun'],
['VBG',	'Verb',	'Verb'],
['VBP',	'Verb',	'Verb'],
['IN',	'preposition',	'Preposition']
 ]
df = pd.DataFrame(data, columns = ['POS','SF','FF'])  
i=0
def main(data,lang,assign):
	st=StanfordPOSTagger(''+assign+'-ud.tagger')
	if lang=="de":
		st=StanfordPOSTagger('german-fast.tagger')	
	nif=rdflib.Namespace("http://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core#")
	track=0
	print("NLTK code trigerred")
	def spans(txt):
		tagged=st.tag(txt.split())
		offset = 0
		check=0		
		for i in range(len(tagged)):
			offset = txt.index(tagged[i][0], offset)
			yield tagged[i][0], offset, offset+len(tagged[i][0]) , tagged[i][1]
			offset += len(tagged[i][0])
			check=check+1
  
	for filename in os.listdir('Files/Input'+lang+'/'):
		if(track < int(data)):
			name=filename.split(".")[0]
			graph2=rdflib.Graph()
			graph2.parse("Files/Input"+lang+"/"+filename,format='nt')
			g=Graph()
			for s,p,o in graph2:
				if type(o)==rdflib.term.Literal and nif.isString in p:
					sentences = nltk.sent_tokenize(o,language=''+assign+'')
					for i in range(len(sentences)):
						try:
							BII=o.find(sentences[i])
							for token in spans(sentences[i]):
								assert token[0]==sentences[i][token[1]:token[2]]
								BI=BII+token[1]
								EI=BII+token[2]
								#print(BI)
								#print(EI)
								#value=df['SF'][df['POS']==token[3]
								#for val in value:
								#hell="http://purl.org/olia/olia.owl#"+val
								#fullvalue=df['FF'][df['POS']==token[3]
								#print(fullvalue[0])
								#for jval in  fullvalue:
								#hello="http://purl.org/olia/olia.owl#"+jval
							
								if token[0] not in string.punctuation:
									g.add([rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=word_"+str(BI)+"_"+str(EI)),RDF.type,nif.Word])
									g.add([rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=word_"+str(BI)+"_"+str(EI)),nif.beginIndex,rdflib.term.Literal(str(BI))])
									g.add([rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=word_"+str(BI)+"_"+str(EI)),nif.endIndex,rdflib.term.Literal(str(EI))])
									g.add([rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=word_"+str(BI)+"_"+str(EI)),nif.anchorOf,rdflib.term.Literal(token[0])])
									g.add([rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=word_"+str(BI)+"_"+str(EI)),nif.referenceContext,rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=context")])       
									g.add([rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=word_"+str(BI)+"_"+str(EI)),nif.oliaLink,rdflib.term.URIRef("http://purl.org/olia/penn.owl#"+token[3])])
									#g.add([rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=word_"+str(BI)+"_"+str(EI)),nif.oliaCategory,term.URIRef(hello)])                         
									#g.add([rdflib.term.URIRef("http://dbpedia.org/resource/"+name+"?dbpv=2016-10&nif=word_"+str(BI)+"_"+str(EI)),nif.oliaCategory,term.URIRef(hell)])
						except:
							pass
                               
			g.bind("nif",nif)        
			g.serialize(destination="Files/POS/"+filename,format="turtle")
			track=track+1
	print("Please Check the POS folder for output files")

if __name__ == "__main__":
    main(data,lang,assign)


