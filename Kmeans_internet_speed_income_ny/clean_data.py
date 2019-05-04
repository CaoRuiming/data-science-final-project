import numpy as np
import csv

def main ():
	with open("../DS final project/NY-Fixed-Dec2017-v1.csv") as broaband_data:
		csv_reader = csv.DictReader(broaband_data, delimiter = ',')
		xdata = {}
		ydata = []
		for row in csv_reader:
			if (row["Consumer"]):
				key = row["BlockCode"][:-3]
				if (key not in xdata.keys()):
					xdata[key] = {}
				key1 = row["TechCode"]
				if ( key1 not in xdata[key].keys()):
					xdata[key][key1] = []
				xdata[key][row["TechCode"]].append(float(row["MaxAdDown"]))
	with open("./nyincomeallblocksnozero.csv") as census_data:
		csv_reader = csv.DictReader(census_data, delimiter = ',')
		cdata = {}
		for row in csv_reader:
			key = row["STATEA"] + row["COUNTYA"] + row["TRACTA"] + row["BLKGRPA"]
			cdata[key] = float(row["AH1PE001"])
	speedData = []
	labels = []
	with open('./downstream_income_NY.csv', mode='w') as speed_inc_file:
		fieldnames = ['Income', '10', '11', '12', '20', '30', '40', '60', '70', '42', '50', '43', '41']
		writer = csv.DictWriter(speed_inc_file, fieldnames=fieldnames)
		writer.writeheader()
		for key in xdata:
			if key in cdata:
				income = cdata[key]
				rdata = {'Income': cdata[key], '11': 0, '50': 0, '12': 0, '70': 0, '10': 0, '42' : 0, '60': 0, '43': 0, '30': 0, '40': 0, '41':0, '20': 0 }
				for key1 in xdata[key].keys():
					if key1 in rdata:
						rdata[key1] = (sum(xdata[key][key1])/len(xdata[key][key1]))
				labels.append(cdata[key])
				writer.writerow(rdata)
if __name__ == '__main__':
	main()