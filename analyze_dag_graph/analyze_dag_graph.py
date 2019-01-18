import sys

import matplotlib.pyplot as plt
import networkx as nx

# D:\Users\pwangsom\git\python_utilities\analyze_dag_graph
main_source = 'D:/Users/pwangsom/git/python_utilities/analyze_dag_graph/'

fh = open(main_source + "dag_test.csv", 'rb')
G = nx.read_adjlist(fh)

nx.write_adjlist(G, sys.stdout.buffer)

nx.draw(G)
plt.show()