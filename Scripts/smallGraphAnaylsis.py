import matplotlib
matplotlib.use('Agg')
from pylab import *
import time
from graph_tool.all import *
import graph_tool
import numpy
import matplotlib.pyplot as plt
from collections import Counter
import sys
import os
import pymongo
import json
import datetime


t = time.time()
print("Starting at: " + str(time.time()-t))

tmp_graph = load_graph("data/graphs/smallerGraph.gt")

print("loaded After: " + str(time.time()-t))

print("betweenness")
graph_tool.centrality.betweenness(tmp_graph)
print("calculated betweenness After: " + str(time.time()-t))

print("local_clustering:")
graph_tool.clustering.local_clustering(tmp_graph)
print("calculated local clustering After: " + str(time.time()-t))

print("motifs:")
motifs, counts = graph_tool.clustering.motifs(tmp_graph,k=3)
print("calculated motifs After: " + str(time.time()-t))


print("In After: " + str(time.time()-t))