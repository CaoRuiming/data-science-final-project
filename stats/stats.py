import csv
from math import sqrt
import re

def z_test(p1, p2, n1, n2):
	p = (p1 * n1 + p2 * n2) / (n1 + n2)
	SE = sqrt(p * (1 - p) * ((1/n1) + (1/n2)))
	z = (p1 - p2) / SE
	return z

def significant(z, alpha=0.05):
	if alpha == 0.01:
		threshold = 2.58
	elif alpha == 0.1:
		threshold = 1.645
	else:
		threshold = 1.96
	if z >= -threshold and z <= threshold:
		return False
	return True

def test(p1, p2, n1, n2):
	z = z_test(p1, p2, n1, n2)
	return significant(z) 

def isFloat(inp):
	try:
		float(inp)
	except ValueError:
		return False
	return True
def getFloat(k, d):
	if isFloat(d[columnNames[k]]):
		return float(d[columnNames[k]])
	else:
		return False

with open('data.csv') as file:
	csv_reader = csv.reader(file, delimiter=',')
	data = list(csv_reader)
	columnNames = {d : i for i, d in enumerate(data[0])}
	data = data[1:]
	idx = columnNames["variable"]
	variable = "internetAtHome"
	filtered_data = [d for d in data if d[idx] == variable]

	for d in filtered_data:
		# age
		# age_p1 = getFloat("age1524Prop", d)
		# age_n1 = getFloat("age1524Count", d)
		# age_p2 = getFloat("age2544Prop", d)
		# age_n2 = getFloat("age2544Count", d)
		# age_p3 = getFloat("age4564Prop", d)
		# age_n3 = getFloat("age4564Count", d)
		# age_p4 = getFloat("age65pProp", d)
		# age_n4 = getFloat("age65pCount", d)

		# print("Ages 15-24 v. 25-44: ", str(age_p1), str(age_p2), test(age_p1, age_p2, age_n1, age_n2))
		# print("Ages 15-24 v. 45-64: " + test(age_p1, age_p3, age_n1, age_n3))
		# print("Ages 15-24 v. 65+: " + test(age_p1, age_p4, age_n1, age_n4))
		# print("Ages 25-44 v. 45-64: " + test(age_p2, age_p3, age_n2, age_n3))
		# print("Ages 25-44 v. 65+: " + test(age_p2, age_p4, age_n2, age_n4))
		# print("Ages 45-64 v. 65+: " + test(age_p3, age_p4, age_n3, age_n4))

		# income
		visited = set()
		print("============== Year:", d[columnNames["dataset"]][6:10], " ==============")
		for k1 in columnNames:
			if not ("Prop" in k1 and not "PropSE" in k1): continue
			if k1[0].isupper(): continue
			a = re.search(r'(Prop)', k1)
			index = a.start()
			prefix1 = k1[:index]
			for k2 in columnNames:
				if (k1, k2) in visited or (k2, k1) in visited: continue
				if not ("Prop" in k2 and not "PropSE" in k2): continue
				if k2[0].isupper(): continue
				if k1 == k2: continue
				b = re.search(r'(Prop)', k2)
				index2 = b.start()
				prefix2 = k2[:index2]
				if not prefix2[0:2] == prefix1[0:2]: continue
				p1 = getFloat(k1, d)
				n1 = getFloat(prefix1 + "Count", d) 
				p2 = getFloat(k2, d)
				n2 = getFloat(prefix2 + "Count", d) 
				if p1 is False or p2 is False or n1 is False or n2 is False: continue
				if n1 == 0 or n2 == 0: continue

				if test(p1, p2, n1, n2):
					print(k1, "and", k2, "are significant, alpha=0.05")
				visited.add((k1, k2))
		print("=========================================")