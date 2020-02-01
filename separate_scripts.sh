#$ tr -d '\r' <q.sh >q-new.sh
#$ mv q-new.sh q.sh
#sed -i 's/\r//' run.sh
#!/bin/sh
while getopts "p:" opt
do
   case "$opt" in
      p) parameterA="$OPTARG" ;;
   esac
done
# Print helpFunction in case parameters are empty
if [ -z "$parameterA" ] 
then
   echo "Please enter path to nif-context or nif-text-link file downloaded from DBPedia";
fi

if echo "$parameterA" | grep 'context'; then
  python final_scripts/separation_context.py $parameterA 
fi

python final_scripts/separation_textlink.py $parameterA 