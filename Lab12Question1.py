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
'''[ 2  5  8 11 14] [ 0 -1 -2 -3 -4] [ 1  6 15 28 45] [1.         0.66666667 0.6        0.57142857 0.55555556]

2ndQuestion

<class 'pandas.core.frame.DataFrame'>    
RangeIndex: 1309 entries, 0 to 1308      
Data columns (total 28 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   Passengerid  1309 non-null   int64  
 1   Age          1309 non-null   float64
 2   Fare         1309 non-null   float64
 3   Sex          1309 non-null   int64  
 4   sibsp        1309 non-null   int64  
 5   zero         1309 non-null   int64  
 6   zero.1       1309 non-null   int64  
 7   zero.2       1309 non-null   int64  
 8   zero.3       1309 non-null   int64  
 9   zero.4       1309 non-null   int64  
 10  zero.5       1309 non-null   int64  
 11  zero.6       1309 non-null   int64  
 12  Parch        1309 non-null   int64  
 13  zero.7       1309 non-null   int64  
 14  zero.8       1309 non-null   int64  
 15  zero.9       1309 non-null   int64
 16  zero.10      1309 non-null   int64
 17  zero.11      1309 non-null   int64
 18  zero.12      1309 non-null   int64
 19  zero.13      1309 non-null   int64
 20  zero.14      1309 non-null   int64
 21  Pclass       1309 non-null   int64
 22  zero.15      1309 non-null   int64
 23  zero.16      1309 non-null   int64
 24  Embarked     1307 non-null   float64
 25  zero.17      1309 non-null   int64
 26  zero.18      1309 non-null   int64
 27  2urvived     1309 non-null   int64
dtypes: float64(3), int64(25)
memory usage: 286.5 KB
None
   Passengerid   Age     Fare  Sex  sibsp  zero  zero.1  ...  Pclass  zero.15  zero.16  Embarked  zero.17  zero.18  2urvived
0            1  22.0   7.2500    0      1     0       0  ...       3        0        0       2.0        0        0         0      
1            2  38.0  71.2833    1      1     0       0  ...       1        0        0       0.0        0        0         1      
2            3  26.0   7.9250    1      0     0       0  ...       3        0        0       2.0        0        0         1      
3            4  35.0  53.1000    1      1     0       0  ...       1        0        0       2.0        0        0         1      
4            5  35.0   8.0500    0      0     0       0  ...       3        0        0       2.0        0        0         0      

[5 rows x 28 columns]
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1309 entries, 0 to 1308
Data columns (total 27 columns):
 #   Column       Non-Null Count  Dtype
---  ------       --------------  -----
 0   Passengerid  1309 non-null   int64
 1   Age          1309 non-null   float64
 2   Fare         1309 non-null   float64
 3   Sex          1309 non-null   int64
 4   sibsp        1309 non-null   int64
 5   zero.1       1309 non-null   int64
 6   zero.2       1309 non-null   int64
 7   zero.3       1309 non-null   int64
 8   zero.4       1309 non-null   int64
 9   zero.5       1309 non-null   int64
 10  zero.6       1309 non-null   int64
 11  Parch        1309 non-null   int64
 12  zero.7       1309 non-null   int64
 12  zero.7       1309 non-null   int64
 13  zero.8       1309 non-null   int64
 14  zero.9       1309 non-null   int64
 15  zero.10      1309 non-null   int64
 16  zero.11      1309 non-null   int64
 17  zero.12      1309 non-null   int64
 18  zero.13      1309 non-null   int64
 19  zero.14      1309 non-null   int64
 20  Pclass       1309 non-null   int64
 21  zero.15      1309 non-null   int64
 22  zero.16      1309 non-null   int64
 23  Embarked     1307 non-null   float64
 24  zero.17      1309 non-null   int64
 25  zero.18      1309 non-null   int64
 26  Survived     1309 non-null   int64
dtypes: float64(3), int64(24)
memory usage: 276.2 KB
None
female/male = 0.4678111587982833
'''
