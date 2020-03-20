# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 08:31:29 2020

@author: HaoNinghui
"""

gene_lengths=[9410,3944141,4442,105338,19149,76779,126550,36296,842,15981]
gene_lengths.sort()
L=gene_lengths
del(L[0],L[-1])
print(L)