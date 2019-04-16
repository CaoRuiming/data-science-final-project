import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
import numpy as np
import sys, csv, time

# prints progress bar; used below
def printProgress(current, total):
	num_increments = 100
	current_prog = int((current / total) * num_increments)
	prog_left = num_increments - current_prog
	prog_string = "\r[" + ("#" * current_prog) + (" " * prog_left) + "]"
	sys.stdout.write(prog_string)
	sys.stdout.flush()

cols = ["NIS ID","Municipality Name","Municipality Type","2010 Muni Population","2010 Muni Housing Units","Muni Area (sq mi)","County","REDC Region","# Cable Providers","# Hse Units Cable","% Hse Units Cable","# of DSL Providers","# Hse Units DSL","% Hse Units DSL","# Fiber Providers","# Hse Units Fiber","% Hse Units Fiber","# Wireline Providers","# Hse Units Wireline","% Hse Units Wireline","# Wireless Providers","# Hse Units Wireless","% Hse Units Wireless","# Satellite Providers"]

raw_data = []
with open('ny_broadband_availability.csv') as csvDataFile:
	csvReader = csv.reader(csvDataFile)
	for row in csvReader:
		raw_data.append(row)

raw_data.pop(0)

# filter out Economic Development Regions from data
raw_data = filter(lambda x: x[cols.index("Municipality Type")] != "Economic Development Region", raw_data)

num_cable_providers = []
num_dsl_providers = []
num_fiber_providers = []
num_wireless_providers = []
num_satellite_providers = []
municipality_names = []
municipality_types = []
for datum in raw_data:
	if datum[0] != "9999999": # get rid of New York State as a whole -> is outlier
		num_cable_providers.append(datum[cols.index("# Cable Providers")])
		num_dsl_providers.append(datum[cols.index("# of DSL Providers")])
		num_fiber_providers.append(datum[cols.index("# Fiber Providers")])
		num_wireless_providers.append(datum[cols.index("# Wireless Providers")])
		num_satellite_providers.append(datum[cols.index("# Satellite Providers")])
		municipality_names.append(datum[cols.index("County")])
		municipality_types.append(datum[cols.index("Municipality Type")])

num_cable_providers = list(map(int, num_cable_providers))
num_dsl_providers = list(map(int, num_dsl_providers))
num_fiber_providers = list(map(int, num_fiber_providers))
num_wireless_providers = list(map(int, num_wireless_providers))
num_satellite_providers = list(map(int, num_satellite_providers))

X = list(zip( \
	num_cable_providers, \
	num_dsl_providers, \
	num_fiber_providers, \
	num_wireless_providers, \
	num_satellite_providers))
Y = municipality_names

# plot elbow curve for kmeans error to find best K
K = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Err = list(map(lambda k: KMeans(n_clusters=k).fit(X).inertia_, K))
plt.plot(K, Err)
plt.xlabel("K")
plt.ylabel("Error (Squared)")
plt.show()
# best K turned out to be 4

# calculate and print centroids when K=4; this is repeated and averaged over
# ITERS number of runs
ITERS = 1000
centroids_history = []
start = time.time()
print("running kmeans with 4 clusters " + str(ITERS) + " times")
for i in range(ITERS):
	model = KMeans(n_clusters=4).fit(X)
	centroids = np.array(sorted(model.cluster_centers_, key=lambda x: x[0]))
	centroids_history.append(centroids)
	printProgress(i, ITERS)
print("\ntask completed in", time.time() - start, "seconds")

# average the centroids
unzipped_centroids_hist = np.array(list(zip(*centroids_history)))
avg_centroids = np.array(list(map(lambda x: np.mean(x, axis=0), unzipped_centroids_hist)))

# print results
print("\ncentroids for 4 centroids across ", str(ITERS), " runs:" )
print("  cable      dsl        fiber      wireless   satellite")
print(avg_centroids)


# recalcuate labels for each data point in X based on sorted centroids
distances = cdist(X, avg_centroids, 'euclidean') # calculate dists
sortedInds = np.argsort(distances, axis=1) # sort indices by dist
labels = sortedInds[:,0] # select the first column for each row

# show histogram of distribution of data points in X that belong to each centroid
plt.hist(labels, bins=4)
plt.xlabel("Index of Centroid Label (Printed in order in Console)")
plt.ylabel("Number of Municipalities Grouped to Centroid")
plt.show()
