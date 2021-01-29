"""
Created on Thurs Sept 10 2020
@author: Andrew Sydor

To compare two BioID Datasets, both with multiple baits, and generate a 
resulting heatmap to show how many preys are in common between the baits. 
Saves the resulting heatmap as a PDF file.

"""
import pylab as plt
from collections import defaultdict
import pandas as pd
import numpy as np
         
# Opening and reading the files; DO NOT INCLUDE FILE EXTENSIONS
file1 = "SARS-CoV2 BioID"   # File name of file 1
file2 = "SARS-CoV2 BioID"    # File name of file 2

dict1 = defaultdict(list)
dict2 = defaultdict(list)

with open(file1 + ".txt") as f1:
    for line in f1:
        if line.strip():
            a,b =  line.strip().split()
            dict1[a].append(b)
            
with open(file2 + ".txt") as f2:
    for line in f2:
        if line.strip():
            a,b =  line.strip().split()
            dict2[a].append(b)

# Compare the two BioID datasets and generate a dataframe with number of common proteins
dict_panda = defaultdict(list)

for key in dict1.keys():
    for key2 in dict2.keys():
        common = set(dict1[key]) & set(dict2[key2])
        dict_panda[key].append(len(common))

dict2_keys = list(dict2.keys())
index = list(range(len(dict2_keys)))

df2 = pd.DataFrame.from_dict(dict_panda)
df3 = df2.transpose()
df4 = df3.iloc[::-1]
df4.columns = dict2_keys

# Generate a heatmap from the dataframe
plt.figure(figsize = (40, 10), dpi = 600, facecolor = 'w', edgecolor = 'k')
plt.pcolor(df4)
plt.xticks(np.arange(0.5, len(df4.columns), 1), df4.columns, rotation = 90, ha = 'center')
plt.yticks(np.arange(0.5, len(df4.index), 1), df4.index)
heatmap = plt.pcolor(df4)
plt.colorbar(heatmap)
plt.savefig('BioID Comparison Heatmap.png')
