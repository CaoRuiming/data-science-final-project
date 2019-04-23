from sklearn.cluster import KMeans
import csv
import numpy.matlib
import numpy as np
import matplotlib.pyplot as plt

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
def main ():
	speedData = []
	income = []
	with open('./speed_income_NY.csv') as data:
		for row in data:
			row_data  = row.split(',')
			if len(row_data) > 1:
				speedData.append(float(row.split(',')[1]))
				income.append(float(row.split(',')[0]))

	k = 9
	xdata = np.array(speedData).reshape(-1, 1)
	centroids, closest_centroids, error = sklearn_cluster(xdata, income, k)
	plot_clusters(xdata, income, centroids, closest_centroids)
def plot_clusters(xdata, ydata, centroids, centroid_indices):
	colors = {0: 'red', 1: 'yellow', 2: 'blue', 3: 'green', 4: 'brown', 5:'orange', 6: 'pink', 7: 'black', 8: 'grey'}
	color = [colors[l] for l in centroid_indices]
	print('centroids: ', centroids)
	fig, ax = plt.subplots()
	plt.scatter(xdata, ydata, c=color)
	plt.xlabel('Average Downstream Speed')
	plt.ylabel('Total Household Income($k)')
	plt.savefig('income_speed_clusters')
	plt.show()
if __name__ == '__main__':
	main()