# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 03:38:27 2019

@author: Evelina
"""

from collections import defaultdict
#meshDictionary = defaultdict(list)

def defaultValue() :
    return 9

d = defaultdict(defaultValue)

import argparse, sys

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser(description='Clean Pubtator Disease data to include only cancer-related articles and remove redundant Mesh IDs')
ap.add_argument("meshFile", help = "MeshTreeHierarchyWithScopeNotes txt")
ap.add_argument("inputFile", help = "disease2pubtator file")
#ap.add_argument("--types",type=str,default="C04",
#                    help="choose between: no-C04 or C04")
ap.add_argument("outputFile", help = "output filepath and name")

# prints help if no arguments are provided
if len(sys.argv)==1:
    ap.print_help(sys.stderr)
    sys.exit(1)

args = vars(ap.parse_args())

###Intializers###
mesh = args['meshFile'] #Mesh_Scope Notes File
file = args['inputFile'] #pubtator file
outFile = args['outputFile']
#put types in this format

cancer = []
pmidDictionary = {}
names = {}
###

print("Reading", mesh, "...")

"""
 *Here we read in the mesh tree file
 *Set up key variables that are separated by the tabs so we have the following:
     key = tree id
     value = mesh id
 *This puts it all in a dictionary 
"""
with open(mesh) as infile :    
   for line in infile :
       items = line.strip()
       items = items.split("\t")
       treeid = items[0]
       value = items[1]
       names[value] = treeid
print("Finished reading", mesh, "!")

""" *Dictionary containing only cancer related diseases """
cancerMeshdict = dict(filter(lambda item: 'C04' in item[1], names.items())) #This one contains list including C04
cancerMeshIDs_noC04 = dict(filter(lambda item: 'C04.' in item[1], names.items())) #Eliminates C04 as an option in the dict
#print(cancerMeshdict) #tester


#print("Information found", cancerMeshdict)

print("Getting Cancer Mesh Info...")

"""
 *Here we are reading in the disease2pubtator file
 *We remove the "MESH:" from the meshID and extract all valid ID numbers
 *We also match them with the PMID variable
"""
with open(file) as infile :
   for line in infile :             
       line = line.replace("MESH:","")         
       items = line.strip()
       items = items.split("\t")
       pmid = items[0]
       mesh = items[1]
       pmidDictionary[pmid] = mesh
       
#print("MeshId's found:", pmidDictionary)  #tester
print("Extracted the MeshID's from", file, "!")


""" filters out only the files that have C04 in them
TO DO: It returns C04 
"""
length = len(pmidDictionary)
for pmid, mesh in pmidDictionary.items() :        
    print(pmid, ":", mesh)
    
   # look up the mesh id in the cancerMeshDict
   # if the id returns C04*, then add the pmid and mesh to
   
   # the 'cancer' list
    a = cancerMeshdict.get(mesh)
    if a is None :
        pass
    else :
        cancer.append(pmid + "\t" + mesh)
    
   #cancer.append(tree + ":" + mesh for tree, mesh in cancerMeshdict ) #FIX THIS LINE! keyerror0
num = 0


""" Writes the file to the output file indicated """

with open(outFile, 'w') as outfile : 
    outfile.write("PMID\tMeshID\n")    
    for i in cancer :
       outfile.write(i)
       outfile.write("\n")
       num += 1

#for pmid, mesh in enumerate(pmidDictionary):
#    print(pmid,"\t", mesh)
print("Created results file")

"""
fout = open(outFile, "w")
fout.write("PMID\tMeshID\n")
for pmid, mesh in pmidDictionary.items() :    
    a = "\n".join([pmid + '\t' + x for x in mesh])
    fout.write(a+'\n')


#TO DO. FILE LOOKS MESSY. 


#TEST to filter out the C04 matched files or not. says dict no attributes to type. has to do with args = (vars)parser
if args.types == 'C04':
    print("Information found", cancerMeshdict)
elif args.types == 'no-C04':
    print("Information found: ")
else:
    print("Information found", cancerMeshdict)
    
"""