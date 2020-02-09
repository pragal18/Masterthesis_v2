Enrichment of DBpedia NIF Dataset
Enrichment of DBpedia NIF Dataset is a compilation of Bash and Python3 scripts that enables to perform various Natural Language
Processing tasks on wikipedia on normal off-the-shelf hardware (e.g., a quad-core CPU, 8 GB of main memory, and 250 GB hard disk 
storage). 

Step 1:
Download the "nif_context_<language>.ttl" file from https://wiki.dbpedia.org/downloads-2016-10 . Languages supported by this project are 
English, French, German, Spanish and Japanese. So make sure you download the nif-context for any one of these languages

Step 2:
Run the 'separate_scripts.sh' by giving an argument -p followed by the path to the location of "nif_context_<language>.ttl" in your 
system. This is a preprocessing step to perform various Natural Language Processing tasks on individual articles. 
Example - ./separate_scripts.sh -p F:/Master_thesis/nif_context_en.ttl

Also you could run the script along with search argument -s , i.e if you want to extract only a subset of "nif_context_<language>.ttl".
//Extract all articles that starts with "St"
./separate_scripts.sh -p F:/Master_thesis/nif_context_en.ttl -s St

//Extract only the article "Augustus"
./separate_scripts.sh -p F:/Master_thesis/nif_context_en.ttl -s Augustus

Step 3:
Perform various NLP tasks by running 'runme.sh' with the following arguments :
1) Language (-l) - "en" for english, "fr" for French, "de" for German, "ja" for Japanese, "es" for spanish
		 Default language is English if the language parameter is not specified. 
		 Even if you have your own text file, store it under this location and all the tasks could be performed.
2) NLP task (-t) - "SEN" for sentence splitting
	      	   "TOK" for Tokenisation
	           "POS" for Part of speech tagging
	           "ADL" for enrichment of additional links
3) Instance size (-n) - specify the number of wikipedia articles the operation should be performed on.
4) Search(-s) - Article name specify a particular article name for which the operation has to be performed.
5) Tool name(-e)- "NLTK" for Using Natural Language Tool Kit package from Python3 , "TTB" for using TextBlob , "SIO" for using Spacy IO 
                   and "PAT" for Pattern.
		   Default is NLTK is none of it is specified.	


PROCESSING 
	We downloads the required DBpedia NIF files from https://wiki.dbpedia.org/downloads-2016-10 , separate into individual articles 
	, perform NLP tasks on various languages with a variety of tools. 

OUTPUT

REQUIREMENTS
python>=3.4
NLTK >= 3.0
GENSIM>=3.4
SPACY>=2.0
rdflib>=4.0
numpy>=1.16.3 
Usage
  usage: ./run.sh [-h] [-p PROJECT] [-i ITERATIONS] [-d DAMPING] [-s START]
                     [-b] [-l]
                     wikilang

  Compute PageRank on Wikipedia.

  positional arguments:
    wikilang              Wikipedia language edition, e.g. "en". "ALL" for
                          computing PageRank over all languages available in a
                          project.

  optional arguments:
    -h, --help            show this help message and exit
    -p PROJECT, --project PROJECT
                          Wiki project, currently supported [wiki, books,
                          source, versity, news]. (default: wiki)
    -i ITERATIONS, --iterations ITERATIONS
                          PageRank number of iterations. (default: 40)
    -d DAMPING, --damping DAMPING
                          PageRank damping factor. (default: 0.85)
    -s START, --start START
                          PageRank starting value. (default: 0.1)
    -b, --bigmem          PageRank big memory flag. (default: False)
    -l, --links           Only extract links (skip PageRank). (default: False)
Examples
Compute PageRank on the current dump of English Wikipedia:

$ ./danker.sh en
$ ./danker.sh en --bigmem
Compute PageRank on the union of all language editions:

$ ./danker.sh ALL
$ ./danker.sh ALL --bigmem    # caution, you will need some main memory for that
Compute PageRank for each Wikipedia language edition separately:

$ for i in $(./script/get_languages.sh); do ./danker.sh "$i"; done
$ for i in $(./script/get_languages.sh); do ./danker.sh "$i" -b; done
Compute PageRank on the English version of Wikibooks:

$ ./danker.sh en --project books
$ ./danker.sh en --bigmem --project books
Compute PageRank on any other graph

Download
Output of ./danker.sh ALL on bi-weekly Wikipedia dumps.

2019-10-29
https://danker.s3.amazonaws.com/2019-10-29.allwiki.links.stats.txt
https://danker.s3.amazonaws.com/2019-10-29.allwiki.links.rank.bz2
2019-10-09
https://danker.s3.amazonaws.com/2019-10-09.allwiki.links.stats.txt
