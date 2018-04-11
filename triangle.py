def triangle()
	coorList = []
	unknownCoord=[]
	add = 0

	while add <= 5:
		for coordinate in coordinates:
		 	coordinates = input("Podaj współrzędne: ")
		 	if coordinates
		  		coorList = coorList.append(coordinates)
		  		add += 1
	return coorlist, unknownCoord

x1 = coorList[0]
y1 = coorList[1]
x2 = coorList[2]
y2 = coorList[3]
x3 = coorList[4]
y3 = coorList[5]

a = (y2 - y1)/(x2 - x1);
b = y1 - a * x1;

unknownCoord.append(a, b)
print(unknownCoord)
