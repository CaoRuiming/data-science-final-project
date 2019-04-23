from sklearn.cluster import KMeans
import csv
import numpy.matlib
import numpy as np
import matplotlib.pyplot as plt
# import pymysql
# connection = pymysql.connect(host='35.196.53.153',
#                              user='diane',
#                              password='',
#                              db='census2')
def sklearn_cluster(X, Y, K):
	kmeans = KMeans(K)
	clusters = kmeans.fit_predict(X)
	cluster_centers = kmeans.cluster_centers_
	error = kmeans.inertia_
	return cluster_centers, clusters, error
def elbow_point_plot(xdata, ydata):
	k = 3
	clusters = []
	errors = []
	while k < 15:
		centrois, closest_centroids, error =  sklearn_cluster(xdata, ydata, k) 
		clusters.append(k)
		errors.append(error)
		k += 1
	plt.plot(clusters, errors)
	plt.show()
import pdb
def main ():
	with open("../DS final project/NY-Fixed-Dec2017-v1.csv") as broaband_data:
		csv_reader = csv.DictReader(broaband_data, delimiter = ',')
		xdata = {}
		ydata = []
		for row in csv_reader:
			if (row["Consumer"]):
				key = row["BlockCode"][:-3]
				if (key not in xdata.keys()):
					xdata[key] = []
				xdata[key].append(float(row["MaxAdDown"]))
	with open("./New York Group Blkgrp Income Estimate.csv") as census_data:
		csv_reader = csv.DictReader(census_data, delimiter = ',')
		cdata = {}
		for row in csv_reader:
			key = row["STATEA"] + row["COUNTYA"] + row["TRACTA"] + row["BLKGRPA"]
			cdata[key] = float(row["AH1OE001"])
	speedData = []
	labels = []
	for key in xdata:
		if key in cdata:
			speedData.append(sum(xdata[key])/len(xdata[key]))
			labels.append(cdata[key])

	k = 8
	print(len(labels), 'length', '\n', len(cdata), '\n')
	print(len(speedData), 'length', '\n', len(xdata))
	# print(xdata)
	#centroids, closest_centroids = sklearn_cluster(xdata, ydata, k)
	# elbow_point_plot(xdata, ydata)
	#plot_clusters(xdata, ydata, centroids, closest_centroids)
def plot_clusters(xdata, ydata, centroids, centroid_indices):
	colors = {0: 'red', 1: 'yellow', 2: 'blue', 3: 'green', 4: 'brown', 5:'orange', 6: 'pink', 7: 'black'}
	color = [colors[l] for l in centroid_indices]
	print('centroids: ', centroids)
	fig, ax = plt.subplots()
	plt.scatter(xdata, ydata, c=color)
	plt.show()
if __name__ == '__main__':
	main()