#!/bin/python3
##**Use this script to get PDB ids from JSON file of RCSB
import json
filename=input("Enter the name of JSON file withon extension: ")
file=open('ids-'+filename+'.dat','w')
with open(filename+".json") as jsonfile:
    data=json.load(jsonfile)
length_of_list=len(data["result_set"]) ##Get total entries
i=0
name=[]
while i<length_of_list:
    getid=data["result_set"][i]["identifier"]
    name.append(getid)
    file.write('%s \t'%(getid))
    i+=1
print(name)
file.close()
