from sklearn.cluster import KMeans
import csv
import numpy.matlib
import numpy as np
import matplotlib 
matplotlib.use('Agg')
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
	row_keys = ['Income', '10', '11', '12', '20', '30', '40', '60', '70', '42', '50', '43', '41']
	speedTechData = []
	with open('./downstream_income_NY.csv') as data:
		for row in data:
			row_data  = row.split(',')
			if len(row_data) > 1:
				curr_row = {}
				for i in range( 1, len(row_data)):
					if (row_data[0] != 'Income'):
						curr_row[row_keys[i]] = (float(row_data[i]))			
				if (row_data[0] != 'Income'):
					income.append(float(row_data[0]))
					speedTechData.append(curr_row)
					speedData.append(list(curr_row.values()))
	k = 9
	xdata = np.array(speedData)
	labels = row_keys[1:]
	colors = {0: 'red', 1: 'yellow', 2: 'blue', 3: 'green', 4: 'brown', 5:'orange', 6: 'pink', 7: 'black', 8: 'grey'}
	centroids, closest_centroids, error = sklearn_cluster(xdata, income, k)
	new_x = make_data(xdata, income)
	plot_clusters( new_x, income, centroids, closest_centroids, 'income_speed_clusters', 'Average speed vs Income', colors)
	for i, centroid in enumerate(centroids):
		plot_centroid(centroid,colors[i], labels)
def plot_clusters(xdata, ydata, centroids, centroid_indices, name, title, colors):
	color = [colors[l] for l in centroid_indices]
	plt.figure()
	fig, ax = plt.subplots()
	plt.scatter(xdata, ydata, c=color)
	plt.title(title)
	plt.xlabel('Average Downstream Speed(mbps)')
	plt.ylabel('Median Household Income($)')
	plt.savefig(name)
def plot_centroid(centroid, color, labels):
	sizes = []
	new_labels = []
	joint_label = ''
	small_sizes = []
	fig1, ax1 = plt.subplots()
	sum_centroid = sum(centroid)
	for i, x in enumerate(centroid):
		ratio  = (x/sum_centroid) * 100
		if ratio < 1:
			small_sizes.append(ratio)
			joint_label = joint_label + ', ' + labels[i]
		else: 
			sizes.append(ratio)
			new_labels.append(labels[i])
	sizes.append(sum(small_sizes))
	new_labels.append(joint_label[1:])
	slices, text= ax1.pie(sizes, labels=new_labels, startangle=90)
	plt.legend(slices,  new_labels, loc='best')
	plt.title(('Centroid for ' + color + ' clusters'))
	ax1.axis('equal')
	plt.savefig(('centroid' + color))
def make_data (xdata,income):
	new_x = []
	for i in range(len(xdata)):
		temp_x = []
		data = xdata[i]
		for x_i in data:
			if x_i > 0.0:
				temp_x.append(x_i)
		new_x.append( (sum(temp_x)/len(temp_x)))
	return np.array(new_x)



if __name__ == '__main__':  
	main()