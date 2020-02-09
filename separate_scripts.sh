#$ tr -d '\r' <q.sh >q-new.sh
#$ mv q-new.sh q.sh
#sed -i 's/\r//' run.sh
#!/bin/sh
while getopts "p:s:" opt
do
   case "$opt" in
      p) parameterA="$OPTARG" ;;
	  s) parameterB="$OPTARG" ;;
   esac
done
# Print helpFunction in case parameters are empty
if [ -z "$parameterA" ] 
then
   echo "Please enter path to nif-context/nif-text-links file downloaded from DBPedia";
fi

if [ -z "$parameterB" ] 
then
	if echo "$parameterA" | grep 'context'; 
	then
		python final_scripts/separation_context.py $parameterA 
	elif echo "$parameterA" | grep 'links';
	then 
		python final_scripts/generating_link_dataset.py $parameterA
	else
		echo "Please enter correct path to nif-context/nif-text-links file downloaded from DBPedia";
	fi
	
else
	python final_scripts/context_search.py $parameterA $parameterB		
fi