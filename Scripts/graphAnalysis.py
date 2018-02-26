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

tmp_graph = load_graph("data/graphs/graph.gt")

print("loaded After: " + str(time.time()-t))



def load_tagged_addresses():
	addresses={}

	for fn in os.listdir('./tagged_addresses'):
		with open("./tagged_addresses/"+fn) as addr_json:
			addresses.update(json.load(addr_json))
	return addresses

tags=load_tagged_addresses()

# numerOfV=0
# for i in tmp_graph.vertices():
# 	numerOfV+=1
# print("number of vertices" +str(numerOfV))



# indegrees = []
# outdegrees = []
# comdegrees = []


# for i in tmp_graph.vertices():
# 	indegrees.append(i.in_degree())
# print("In After: " + str(time.time()-t))

# for i in tmp_graph.vertices():
# 	outdegrees.append(i.out_degree())
# print("Out After: " + str(time.time()-t))

# for i in tmp_graph.vertices():
# 	comdegrees.append(i.out_degree()+i.in_degree())
# print("Commulated After: " + str(time.time()-t))

# incounted = Counter(indegrees)
# counted = Counter(outdegrees)
# comcounted = Counter(comdegrees)

# insort = sorted(incounted.items(), reverse=True)
# sort = sorted(counted.items(), reverse=True)
# comsort = sorted(comcounted.items(), reverse=True)


# fig = plt.figure()
# inax = fig.add_subplot(2,2,1)
# ax = fig.add_subplot(2,2,2)
# comax = fig.add_subplot(2,2,3)

# inline, = inax.plot(*zip(*insort),"*")
# line, = ax.plot(*zip(*sort),"*")
# comlin, = comax.plot(*zip(*comsort),"*")

# inax.set_xscale('log')
# inax.set_yscale('log')
# inax.set_xlabel("Number of Ingoing TX")
# inax.set_ylabel("Number of address")

# ax.set_xscale('log')
# ax.set_yscale('log')
# ax.set_xlabel("Number of outgoing TX")
# ax.set_ylabel("Number of address")

# comax.set_xscale('log')
# comax.set_yscale('log')
# comax.set_xlabel("Number of comulated TX")
# comax.set_ylabel("Number of address")




# fig.savefig("powerLaw.png")
# print("saves")




#fig = plt.figure()
#ax = fig.add_subplot(2,1,1)

#line, = ax.scatter(*zip(*sort))
#ax.set_yscale('log')
#plt.hist(vert,bins=range(max(vert)+2))



#for i in tmp_graph.ep.weight.sort():
#	print(str(i))
#asd=0
#for e in tmp_graph.edges():
#	print(tmp_graph.ep.weight[e])
#	asd+=1
#	if asd%10000==0:
#		print(asd)


#print(numberOfEdges)
#for e in tmp_graph.edges():
#	print("weight: "+str(tmp_graph.ep.weight[e]))

#for v in tmp_graph.vertices():
#	print("address: "+tmp_graph.vp.address[v])


#for e in tmp_graph.edges():
#	tmp_graph.ep.dollar[e]+=0.000001

print("StartPagerank:")
#propertyMap=graph_tool.centrality.pagerank(tmp_graph,weight =tmp_graph.ep.dollar)
propertyMap=graph_tool.centrality.pagerank(tmp_graph,weight =tmp_graph.ep.weight)
print("calculated pagerank After: " + str(time.time()-t))


tmp_graph.vp.pr=propertyMap



pageranking=[]#np.array([[0.000000000000001,"0xa1"]])
counter=0

#creating address pagerank association
for v in tmp_graph.vertices():
	newEntry=[tmp_graph.vp.pr[v],tmp_graph.vp.address[v]]
	pageranking.append(newEntry)
	counter+=1
	if counter%10000 == 0:
		print(counter)


#convert from array to ndarray
print("Create Numpy Array: " + str(time.time()-t))
numpied=np.array(pageranking)
print("Created Numpy Array: " + str(time.time()-t))

#sort by first column
print("Sort Numpy Array: " + str(time.time()-t))
numpied2=numpied[numpied[:,0].argsort()]
print("Sorted Numpy Array: " + str(time.time()-t))

#give top 10 rated addresses
numberOfTags={'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'10':0}

for i in numpied2.tolist()[:10000]:
	if i[1] in tags:
		numberOfTags[str(tags[i[1]])]+=1
		print("LOL")
	else:
		numberOfTags['10']+=1


with open('pagerankResults.json', 'w') as outfile:
    json.dump(numberOfTags, outfile)



#for v in tmp_graph.vertices():
#	print("address: "+tmp_graph.vp.address[v])

#for i in propertyMap:
	#print(i)






# print("local_clustering:")
# graph_tool.clustering.local_clustering(tmp_graph)
# print("calculated local clustering After: " + str(time.time()-t))

# print("local_global_clustering:")
# graph_tool.clustering.global_clustering(tmp_graph)
# print("calculated global Clustering After: " + str(time.time()-t))

# print("extended_clustering:")
# graph_tool.clustering.extended_clustering(tmp_graph)
# print("calculated extended_clustering After: " + str(time.time()-t))





# print("StartHits:")
# graph_tool.centrality.hits(tmp_graph)
# print("calculated hits After: " + str(time.time()-t))

# print("StartEigenvector:")
# graph_tool.centrality.eigenvector(tmp_graph)
# print("calculated eigenvector After: " + str(time.time()-t))




# print("motifs:")
# motifs, counts = graph_tool.clustering.motifs(tmp_graph,k=2,motif_list=([g1]))
# print("calculated motifs After: " + str(time.time()-t))

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