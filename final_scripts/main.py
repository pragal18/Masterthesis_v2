#!/usr/bin/python 
import sentence_nltk, token_nltk, pos_nltk, sentence_sio, token_sio, pos_sio ,sentence_ttb , token_ttb, pos_ttb, sentence_pat
import search_sentence, search_token, search_pos
import sys

def exec():
	if tool=="NLTK":
		assign="english"
		if task=="SEN":
			sentence_nltk.main(n,lang,assign)
		elif task=="TOK":
			token_nltk.main(n,lang,assign)
		elif task=="POS":
			pos_nltk.main(n,lang,assign)
		# elif task=="LINK":
			# link_nltk.main(n,lang,assign)
		else:
			print("Invalid task")
	elif tool=="SIO":
		if task=="SEN":
			sentence_sio.main(n,lang)
		elif task=="TOK":
			token_sio.main(n,lang)
		elif task=="POS":
			pos_sio.main(n,lang)
		# elif task=="LINK":
			# link_sio.main(n,task,search,tool,lang)
		else:
			print("Invalid task")	
	elif tool=="TTB":
		if task=="SEN":
			sentence_ttb.main(n,lang)
		elif task=="TOK":
			token_ttb.main(n,lang)
		elif task=="POS":
			pos_ttb.main(n,lang)
		# elif task=="LINK":
			# link_ttb.main(n,task,search,tool,lang)
		else:
			print("Invalid task")
	elif tool=="PAT":
		if task=="SEN":
			sentence_pat.main(n,lang)
		# elif task=="TOK":
			# token_ttb.main(n,lang)
		# elif task=="POS":
			# pos_ttb.main(n,lang)
		else:
			print("Invalid task for PATTERN library")			
	else:
		print("Invalid tool chosen")

def exec_search():
	if task=="SEN":
		search_sentence.main(lang,search)
	elif task=="TOK":
		search_token.main(lang,search)
	elif task=="POS":
		search_pos.main(lang,search)
	# elif task=="LINK":
		# link_ttb.main(n,task,search,tool,lang)
	else:
		print("Invalid task")		

n=sys.argv[1]
task=sys.argv[2]
search=sys.argv[3]
tool=sys.argv[4]
lang=sys.argv[5]
if search == "NA" :
	exec()
else:
	exec_search()
#submain2.main(n,task,search,tool,lang)