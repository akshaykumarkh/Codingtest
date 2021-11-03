text = open("sample.txt", "r")
dt = dict()
for line in text:
	line = line.strip()
	line = line.lower()
	words = line.split(" ")
	for word in words:
		if word in dt:
			dt[word] = dt[word] + 1
		else:
			dt[word] = 1
for key in list(dt.keys()):
	print(key, ":", dt[key], ",")
	
