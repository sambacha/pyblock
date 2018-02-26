import matplotlib
matplotlib.use('Agg')
from pylab import *
import time
from graph_tool.all import *
import graph_tool
import numpy
import matplotlib.pyplot as plt
from collections import Counter

t = time.time()
print("Starting at: " + str(time.time()-t))

tmp_graph = load_graph("data/graphs/finalGraph (2).gt")

print("loaded After: " + str(time.time()-t))


counter=0
for e in tmp_graph.edges():
	tmp_graph.ep.dollar[e]+=0.000000000000000001
	tmp_graph.ep.weight[e]+=0.000000000000000001
	counter+=1
	if counter%100000==0:
		print(counter)


tmp_graph.save("graph.gt", fmt="gt")