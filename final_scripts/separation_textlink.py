#Separating contents of text link file downloaded from NIF DBpedia 
import os
import sys
previousSubject=None
path=sys.argv[1]
check=path[len(path)-6:len(path)-4]
with open(path,encoding="utf-8") as openfileobject:
    for line in openfileobject:
        s=line.find('?')
        thisSubject=line[32:s]
        if previousSubject==thisSubject:
            f.write(line);
        else:
            try:  
                f=open("Files/Link"+check+"/"+thisSubject+".ttl",'a',encoding="utf-8")
                f.write(line);
            except:
                pass  