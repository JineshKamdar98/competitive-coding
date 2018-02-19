import os
import sys
#print (sys.argv[1])
filelistCommand = "ls input_random_*.txt > filelist.txt"    #store list of all input files into filelist.txt
os.system(filelistCommand)                                  #run the above command.
filelist = open("filelist.txt", 'r')                        #take the filelist into a variable

for filename in filelist:                                   #for each file in the list.
    bashCommand = "./"+sys.argv[1]+" < "+filename[:-1]+" > o1.txt" #the last character of "fil" (filename) is '\n'. store output in o1.txt
    os.system(bashCommand)                                  #execute file dijkstra and store output in o1.txt
    bash2 = "diff o1.txt out"+filename[2:-1]                #fil is input_random_*_*.txt\n" so we will remove first 2 chars.
    os.system(bash2)
