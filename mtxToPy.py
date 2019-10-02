from scipy.io import mmread
from scipy.sparse import csr_matrix

f = mmread('./3elt_dual.mtx')
f = f.toarray()

print(f)

c = csr_matrix(f)

print(c)
