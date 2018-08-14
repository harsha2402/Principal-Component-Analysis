# Principal-Component-Analysis

Python implementation of PCA with bioinformatics datasets. It allows you to choose the dataset file and performs PCA on 
the attributes based on the eigen values and eigen vectors. 

</br>
What to infer from this code:</br >
1. The scatter plots tell us that there is a relationship between the attributes.
2. The relation between the attributes matter more than the size of the dataset. As you can see that plot of pca_c.txt is 
much more clustered together that plot of pca_b.txt. As pca_b has more number of attributes than pca_c, but pca_b has negative values.
3. Also that negative values of attributes can contribute a lot to the medical data, that positive close constructed data.

</br>
Flow of the code:</br >
1. Take the whole dataset consisting of d-dimensional samples ignoring the class labels
2. Compute the d-dimensional mean vector (i.e., the means for every dimension of the whole dataset)
3. Compute the scatter matrix (alternatively, the covariance matrix) of the whole data set
4. Compute eigenvectors (e1,e2,...,ed) and corresponding eigenvalues (λ1,λ2,...,λd)
5. Sort the eigenvectors by decreasing eigenvalues and choose k eigenvectors with the largest eigenvalues to form a d×k dimensional
matrix W (where every column represents an eigenvector)
6. Use this d×k eigenvector matrix to transform the samples onto the new subspace. This can be summarized by the 
mathematical equation: y=WT×x (where x is a d×1-dimensional vector representing one sample, and y is the transformed
k×1-dimensional sample in the new subspace.)
