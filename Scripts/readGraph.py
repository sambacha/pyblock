from graph_tool.all import *
import graph_tool
import time

t = time.time()
print("Starting at: " + str(time.time()-t))

tmp_graph = load_graph("data/graphs/4369999_None.gt")


print("loaded After: " + str(time.time()-t))


print("motifs:")
graph_tool.clustering.motifs(tmp_graph,1)
print("calculated motifs After: " + str(time.time()-t))

print("motif_significance:")
graph_tool.clustering.motif_significance(tmp_graph,1)
print("calculated motif_significance After: " + str(time.time()-t))

print("local_clustering:")
graph_tool.clustering.local_clustering(tmp_graph)
print("calculated local clustering After: " + str(time.time()-t))

print("local_global_clustering:")
graph_tool.clustering.global_clustering(tmp_graph)
print("calculated global Clustering After: " + str(time.time()-t))

print("extended_clustering:")
graph_tool.clustering.extended_clustering(tmp_graph)
print("calculated extended_clustering After: " + str(time.time()-t))





print("StartHits:")
graph_tool.centrality.hits(tmp_graph)
print("calculated hits After: " + str(time.time()-t))

print("StartEigenvector:")
graph_tool.centrality.eigenvector(tmp_graph)
print("calculated eigenvector After: " + str(time.time()-t))

print("StartPagerank:")
graph_tool.centrality.pagerank(tmp_graph)
print("calculated pagerank After: " + str(time.time()-t))

#print("StartCloseness:")
#graph_tool.centrality.closeness(tmp_graph)
#print("calculated closeness After: " + str(time.time()-t))

#print("betweenness")
#graph_tool.centrality.betweenness(tmp_graph)
#print("calculated betweenness After: " + str(time.time()-t))

#print("StartKatz:")
#graph_tool.centrality.katz(tmp_graph)
#print("calculated katz After: " +str(time.time()-t))
#for address in addresses:
#	print(counter)
#	counter+=1