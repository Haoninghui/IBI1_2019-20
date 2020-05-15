# -*- coding: utf-8 -*-
"""
Created on Wed Apr 8 09:57:34 2020

@author: HaoNinghui
"""
#same as previous tasks
reseq = []
Name = []
gene = []
s=''
count = 0
s1 = ''
#open the file in the reading model
xfile = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
#select the info with the specific begining
for line in xfile:
    if line.startswith ('>'):
        if s!='':
            gene.append(s)
        s = line[1:8]
        Name.append(s)
        count = count + 1
        s = ''
    else:
        s = s + line 
gene.append(s)

#the second method in RC is better to involve in this task
#(there are al least 6 methods to perform RC on the internet and I choose one of them and make some modification)
for j in range(count):
    seq = gene[j]
    s1 = ''
    for i in range(len(seq)):    
        if seq[i] == 'A':
            s1 = 'T' + s1
        elif seq[i] == 'C':
            s1 = 'G' + s1
        elif seq[i] == 'G':
            s1 = 'C' + s1
        elif seq[i] == 'T':
            s1 = 'A' + s1
    reseq.append(s1)

n = input ('please input the file name')
#this time we need to save the info in a new file that is create a new file and open it as 'write mode'
fout = open(n,'w')
# there are only names and reserve sequences in the file 
for i in range(count):
    line1 = Name[i] + '   ' + str(len(gene[i])) + '\n'
    line2 = reseq[i] + '\n'
    fout.write(line1)
    fout.write(line2)

try:
	xfile = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
finally:
	if xfile:
		xfile.close()
fout.close()

#this is not all done by myself as we work in a group and others solve my question by offering and modifying code idea.:-(
#It works well anyway in the end. 
#Anyway, I do understand the logic and operations in the code.