# -*- coding: utf-8 -*-
"""
Created on Sun May 17 22:12:18 2020

@author: HaoNinghui
"""

#import some useful libiaries
import xml.dom.minidom
import pandas as pd 
List = []#could store various lines in excel
index = []#to count the row number
#variable 'count' used for storing the number of childnodes
count = 0
DOMTree = xml.dom.minidom.parse('go_obo.xml')#open the file
collection = DOMTree.documentElement #pick the elements out 
GO = collection.getElementsByTagName("term")#get out all the descendants with the tag 'term'
#define a function that find all childnodes matched inout-genes
def finding(a):  
    #globalize variable
    global id,id1,child,count
#the variable 'count' will add 1 everytime when the function is called, thus the total childnodes number will be count-1 later
    count += 1
    c={}   #store the element in is_a tag
# go through all the descendants with tag 'term'
    for go in GO:
#line 30~32 used to check if the 'go' has the tag 'is_a'
        child = go.getElementsByTagName('is_a')
        b = child.length#know how many element was found
        if b !=0:
            #if <is_a> tag existed, the element was got out in the is_a tag
            for j in range(b):
#put the element in tag <is_a>
                child1 = go.getElementsByTagName('is_a')[j]
                c[j] = child1.childNodes[0].data
# if genes are found, put it in the tag 'is_a' , then do recursion until no more childnodes are found
                if c[j].find(a) != -1:#wanted gene existed
                    id = go.getElementsByTagName('id')[0]
                    id1 = id.childNodes[0].data# find out the id which contains wanted gene
                    finding(id1)#recursion and find more childnodes until no more childnodes existed
#-1 because we +1 previous in the line 23\24
    return(count-1)
i = 1
for go in GO:
#select the element in tag <defstr> and get them out 
    check = go.getElementsByTagName('defstr')[0]
    a = check.childNodes[0].data
#check if it is associated with autophagosome
    if a.find('autophagosome') != -1:#if its description contains autophagosome
        name = go.getElementsByTagName('name')[0]
        name1 = name.childNodes[0].data#get out its name in <name> tag
#select the id out
        id = go.getElementsByTagName('id')[0]
        id2 = id.childNodes[0].data#get out its id in tag <id>
        #RESET THE COUNT VALUE
        count = 0
        childnodes = finding(id2)#find childnodes suitable for id2
# form a list contains (id,name,definition and childnodes number)
        b=[id2,name1,a,childnodes]
        List.append(b) #column content in excel
        # index list used to document the row number ,add one each turn
        i += 1
        index.append(i)
#output the file.excel
#list 1 as the content for each column, index list as the row number
df = pd.DataFrame(List,index,columns=['id', 'names', 'definition','chilnodes'])
df.to_excel("GO task.xls")
