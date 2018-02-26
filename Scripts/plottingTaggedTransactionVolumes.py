import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import json
import collections
import seaborn as sns
import datetime
import matplotlib.dates as mdate



with open('tagged_timeseries/from_tags.json') as data_file:
    data = json.load(data_file)

x=[]
y=[]


quadrillion = 1000000000000000000

ordered= collections.OrderedDict(sorted(data.items()))
timepoints={}
values=[]

tags=['1','2','3','4','5','6','7','10']
legend=['Exchanges','Tokens','Mining Pools','Dapps','Scam','Eth Developer','Genesis','Untagged']


#calculate commulated volume for a timepoint
volumes={}
for timepoint in ordered:
	volume=0
	for tag in tags:
		#the [2] is just the number of tx. [1] --> dollar, [0]--> ether
		volume+=data[timepoint][tag][2]
	volumes[timepoint]=volume
	#tagValues.append(data[timepoint][tag])


for tag in tags:
	tagValues=[]
	for timepoint in ordered:
		tagValues.append(data[timepoint][tag][2]/max(1,volumes[timepoint]))
	y.append(tagValues)


for i in ordered.keys():
	x.append(int(i))




fig = plt.figure()
ether = fig.add_subplot(2,2,1)
#dollar = fig.add_subplot(2,2,2)
#number = fig.add_subplot(2,2,3)
pal = sns.color_palette("Set1")
ether.stackplot(x,y,labels=tags,colors=pal, alpha=0.4 )
plt.legend(loc='upper right')
ether.legend(legend,bbox_to_anchor=(1.05, 1),loc=2, borderaxespad=0.,fontsize=5)



fig.savefig("tagged_from_plot_stacked.svg")


#   https://python-graph-gallery.com/255-percentage-stacked-area-chart/