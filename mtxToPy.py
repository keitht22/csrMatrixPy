from scipy.io import mmread
from scipy.sparse import csr_matrix
import sys
import networkx as nx

def readInput(filename):
	# output is implemented to __main__ as variable 'mat'
	a = mmread(filename)
	b = a.toarray()
	c = csr_matrix(f)
	return c

if __name__ == "__main__":
	# "./3elt_dual.mtx"
	fileN = input('Enter an mtx file path: ')
	mat = readInput(fileN)
	return mat
	G = nx.DiGraph()
