# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 08:39:39 2020

@author: HaoNinghui
"""
#editing the sequency
gene_lengths=[9410,3944141,4442,105338,19149,76779,126550,36296,842,15981]
gene_lengths.sort()#arrange it for min to max
L=gene_lengths
del(L[0],L[-1])#delete the extreme number

#box plot
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#using the input data without extreme values
data=pd.DataFrame({"distribution of remaining gene length":L})
#draw
data.boxplot(vert=True,#vertical box plot
            whis=2,
            patch_artist=True,
            meanline=False,
            showbox=True,
            showcaps=True,
            showfliers=True,
            notch=False)
plt.show()

print(L)