import json
from pprint import pprint

with open('dollarPrice.json') as data_file:
	data = json.load(data_file)

for i in data:
	print(i["close"])