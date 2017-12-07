file_1 = open("AddressAndPLocation.txt", "r+")

file_2 = open("Plocations.txt", "r+")

file_3 = open("addresses.txt", "r+")

content = file_1.readlines()

plocations = []

address = []

weird = []

for line in content:
		x = line.split("-P")
		if len(x) == 2:
			
			address.append(x[0])
			plocations.append(x[1])
			
		else:
			x = line.split("P1")
			if len(x) == 2:
				address.append(x[0])			
				plocations.append("1"+x[1])
		
			else:
				print x
			
		
file_2.write('P'.join(plocations))

file_3.write('\n'.join(address))

