#import libraries numpy, pds,matplotlib, using numpy create array and perform mathematical operations, using pds createa a dataframe and perform filtering and analysis, using mtplotlib plot graphs, for visual representatio of data
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
arr = np.array([1,2,3,4,5])
arr2 = np.arange(1,11,2)
print(arr+arr2,arr-arr2,arr*arr2,arr/arr2)
print("\n2ndQuestion\n")
tnc = pd.read_csv(r'C:\Users\LAB121\Downloads\titanic.csv')
print(tnc.info())
print(tnc.head())
tnc["Survived"] = tnc["2urvived"]
tnc = tnc.drop(["zero","2urvived"],axis = 1)
print(tnc.info())
survivors = tnc[tnc["Survived"]==1]
male_srv = (survivors[survivors["Sex"]==0]).shape[0]
female_srv = (survivors[survivors["Sex"]==1]).shape[0]
print("female/male =",male_srv/female_srv)
plt.plot(tnc["Sex"],tnc["Survived"])
plt.show()