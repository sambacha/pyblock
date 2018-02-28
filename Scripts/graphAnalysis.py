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



measurements=[None,tmp_graph.ep.weight,tmp_graph.ep.dollar]
measurementNames=["number","ether","dollar"]

for measure in [0,1,2]:
	print("Starting with measurement: "+measurementNames[measure])
	# inDegrees=tmp_graph.get_in_degrees(range(tmp_graph.get_vertices().size),eweight=measurements[measure])
	# tmp_graph.vp.ins=inDegrees
	# print("calculated inDegrees")
	# outDegrees=tmp_graph.get_out_degrees(range(tmp_graph.get_vertices().size),eweight=measurements[measure])
	# tmp_graph.vp.outs=outDegrees
	# print("calculated outDegrees")
	pagerank=graph_tool.centrality.pagerank(tmp_graph,weight =measurements[measure])
	tmp_graph.vp.pr=pagerank
	print("calculated pageranks")
	eig,auth,hub=graph_tool.centrality.hits(tmp_graph,weight =measurements[measure])
	tmp_graph.vp.auth=auth
	tmp_graph.vp.hub=hub
	print("calculated HITS")

	mappings=[]
	counter=0
	#creating address association
	for v in tmp_graph.vertices():
		mapping=[int(v),v.in_degree(weight =measurements[measure]),v.out_degree(weight =measurements[measure]),tmp_graph.vp.pr[v],tmp_graph.vp.auth[v],tmp_graph.vp.hub[v]]
		mappings.append(mapping)
		counter+=1
		if counter%100000 == 0:
			print(counter)

	numpiedMappings=np.array(mappings).astype(float)
	print("Created Numpy Array: " + str(time.time()-t))

	#sort by columns
	inSorted=numpiedMappings[numpiedMappings[:,1].argsort()]
	outSorted=numpiedMappings[numpiedMappings[:,2].argsort()]
	prSorted=numpiedMappings[numpiedMappings[:,3].argsort()]
	authSorted=numpiedMappings[numpiedMappings[:,4].argsort()]
	hubSorted=numpiedMappings[numpiedMappings[:,5].argsort()]

	print("Sorted Numpy Arrays: " + str(time.time()-t))

	print(str(inSorted[-1]))
	print(str(outSorted[-1]))
	print(str(prSorted[-1]))
	print(str(authSorted[-1]))
	print(str(hubSorted[-1]))


	allsorted=[inSorted,outSorted,prSorted,authSorted,hubSorted]

	allTaggedRanks=[]

	for oneSorted in allsorted:
		rank=10000
		TaggedRanks=[]
		for topranked in oneSorted[-10000:]:
			addr=tmp_graph.vp.address[int(topranked[0])]
			if addr in tags:
				taggedRank=[addr,str(tags[addr]),str(rank)]
				TaggedRanks.append(taggedRank)
				print('TAGGED')
			rank-=1
		allTaggedRanks.append(TaggedRanks)

	with open(measurementNames[measure]+'taggedRankings.json', 'w') as outfile:
		json.dump(allTaggedRanks, outfile)









# print("StartPagerank:")
# pagerankNumber=graph_tool.centrality.pagerank(tmp_graph)
# pagerankEther=graph_tool.centrality.pagerank(tmp_graph,weight =tmp_graph.ep.weight)
# pagerankDollar=graph_tool.centrality.pagerank(tmp_graph,weight =tmp_graph.ep.dollar)
# print("calculated pagerank After: " + str(time.time()-t))


# tmp_graph.vp.prNumber=pagerankNumber
# tmp_graph.vp.prEther=pagerankEther
# tmp_graph.vp.prDollar=pagerankDollar



# pagerankingNumber=[]
# pagerankingEther=[]
# pagerankingDollar=[]
# counter=0

# #creating address pagerank association
# for v in tmp_graph.vertices():
# 	number=[tmp_graph.vp.prNumber[v],tmp_graph.vp.address[v]]
# 	ether=[tmp_graph.vp.prEther[v],tmp_graph.vp.address[v]]
# 	dollar=[tmp_graph.vp.prDollar[v],tmp_graph.vp.address[v]]
# 	pagerankingNumber.append(number)
# 	pagerankingEther.append(ether)
# 	pagerankingDollar.append(dollar)
# 	counter+=1
# 	if counter%100000 == 0:
# 		print(counter)


# #convert from array to ndarray
# print("Create Numpy Arrays: " + str(time.time()-t))
# numpiedNumber=np.array(pagerankingNumber)
# numpiedEther=np.array(pagerankingEther)
# numpiedDollar=np.array(pagerankingDollar)
# print("Created Numpy Arrays: " + str(time.time()-t))

# #sort by first column
# print("Sort Numpy Arrays: " + str(time.time()-t))
# numpiedNumberSorted=numpiedNumber[numpiedNumber[:,0].argsort()]
# numpiedEtherSorted=numpiedEther[numpiedEther[:,0].argsort()]
# numpiedDollarSorted=numpiedDollar[numpiedDollar[:,0].argsort()]
# print("Sorted Numpy Arrays: " + str(time.time()-t))

# #give top 10 rated addresses

# place=1
# rankingsNumber={}

# for i in numpiedNumberSorted.tolist()[:10000]:
# 	if i[1] in tags:
# 		rankingsNumber[str(i[1])]=[str(tags[i[1]]),str(place)]
# 	place+=1

# with open('pagerankNumber.json', 'w') as outfile:
#     json.dump(rankingsNumber, outfile)



# place=1
# rankingsEther={}

# for i in numpiedEtherSorted.tolist()[:10000]:
# 	if i[1] in tags:
# 		rankingsEther[str(i[1])]=[str(tags[i[1]]),str(place)]
# 	place+=1

# with open('pagerankEther.json', 'w') as outfile:
#     json.dump(rankingsEther, outfile)


# place=1
# rankingsDollar={}

# for i in numpiedDollarSorted.tolist()[:10000]:
# 	if i[1] in tags:
# 		rankingsDollar[str(i[1])]=[str(tags[i[1]]),str(place)]
# 	place+=1
# with open('pagerankDollar.json', 'w') as outfile:
#     json.dump(rankingsDollar, outfile)




# print("StartHits:")
# graph_tool.centrality.hits(tmp_graph)
# print("calculated hits After: " + str(time.time()-t))

