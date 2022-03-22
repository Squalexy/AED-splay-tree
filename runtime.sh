#!/bin/bash
files=$(ls ./"$2")

python3 "$1"
rm ./"$3"
for file in $files
do
	echo "$file"
	python3 "$1" < ./"$2"/"$file" >> ./"$3"
done

