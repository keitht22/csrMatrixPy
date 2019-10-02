from scipy.io import mmread
from scipy.sparse import csr_matrix

f = mmread('/Users/tylerkeith/Documents/Research/BatchLayoutCode-master/datasets/input/3elt_dual.mtx')
f = f.toarray()

print(f)

c = csr_matrix(f)

print(c)
