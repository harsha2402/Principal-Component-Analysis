import numpy as np
import scipy.stats
import pandas as pd
import matplotlib.pyplot as plt

data=a=S=mean=std=B=[]

#Select the dataset, along with the path
file=input()
data = pd.read_csv(file, sep="\t", header=None, nrows=1)
r,c=data.shape

#Take the whole dataset consisting of d-dimensional samples ignoring the class labels
for i in range(0,c-1):
    a.append(i)
O = pd.read_csv(file, sep="\t", header=None, usecols=a)
print (type(B))
#Save the transposed mate
B = O.T
a=[c-1]
data = pd.read_csv(file, sep="\t", header=None, usecols=a)

#Compute the d-dimensional mean vector (i.e., the means for every dimension of the whole dataset)
for i in range(0,c-1):
    mean.append(np.mean(O[i]))
for i in range(0,c-1):
    std.append(np.std(O[i]))

#Compute the scatter matrix (alternatively, the covariance matrix) of the whole data set
cov=(np.cov(B))

#Compute eigenvectors (e1,e2,...,ed) and corresponding eigenvalues (λ1,λ2,...,λd)
evalue,evector = np.linalg.eig(cov)
print ("The eigen values are",evalue)
print ("The eigen vectors are")
print (evector)

#Sort the eigenvectors by decreasing eigenvalues and choose k eigenvectors with the largest
#eigenvalues to form a d×k dimensional matrix WW(where every column represents an eigenvector)
fmax=max(evalue)
for i in range (0,len(evalue)):
    if(fmax==evalue[i]):
        f=i;
        break;

evalue[f]=0
smax=max(evalue)
evalue[f]=fmax
print(fmax,smax)

for i in range (0,len(evalue)):
    if(smax==evalue[i]):
        s=i;
        break;
    else:
        continue;

#we have finally found the eigen values and eigen vectors and also which columns to be converted to pca
S=evector.T
pca=[]

#PCA Transformation
pca.append(S[f])
pca.append(S[s])
pca1=pd.DataFrame(pca)

#printing new pca transformed dataset
print (pca1)
j=0
data=pd.DataFrame()
L=[]
B=O.T
PCA_Transform=[]
PCA_Transform=np.matmul(pca1,B)

#Scatter Plots of the new Dataset
colors=['red','blue']
plt.scatter(PCA_Transform[0],PCA_Transform[1], s=data, c=colors, alpha=0.5)
str='Scatter plot PCA of '+file
plt.title(str)
plt.xlabel('pca1')
plt.ylabel('pca2')
plt.show()
