from scipy.io import mmread
from scipy.sparse import csr_matrix
import sys
import networkx as nx

def readInput(filename):
	f = mmread(filename)
	f = f.toarray()
	print(f)
	c = csr_matrix(f)
	return c

if __name__ == "__main__":
	#"./3elt_dual.mtx"
	filen = sys.argv[1]
	#print(sys.argv[0], sys.argv[1])
	mat = readInput(filen)
