# -*- coding: utf-8 -*-
"""
Created on Wed Apr 8 08:45:59 2020

@author: HaoNinghui
"""
#create variables and can be changed afterwards
Name = []
gene = []
leng = []
s=''
count = 0
length = 0
#a variable using Boolean to judge the output
x = False
#open the file in the reading model
xfile = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
#select the info with the specific begining
for line in xfile:
    if line.startswith ('>'):
        if s!='':
            gene.append(s)
            leng.append(length)
        s = line[1:8]
        length = 0
        Name.append(s)
        count = count + 1
        s = ''#to separate
    else:
        s = s + line 
        length = length + len(line)
gene.append(s)#add to 'gene'

seq = input ('please input the gene name')
l = int(input('please input the gene length'))
for i in range (count):
    if seq == Name[i]:
        print(gene[i])
        x = True
        break
if x == False:
    print ('No such sequence here')#judgement
    
fout = open('mito_gene.fa','w')
line1 = Name[i] + '   ' + str(leng[i]) + '\n' #format
line2 = gene[i]
fout.write(line1)#write in the file
fout.write(line2)

#open the file in reading mode and use 'try' to better achieve
try:
	xfile = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
finally:
	if xfile:
		xfile.close()
fout.close()

#join the previous two tasks together
