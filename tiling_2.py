import string
import numpy as np

file = open("tiling_0124.k", "w")	

file.write(";!knitout-2\n")
file.write(";;Carriers: 6\n")
file.write("inhook 6\n")
#file.write("x-stitch-number 96\n")

Carriers = "6"

#unit pattern size
unitWidth = 15
unitHeight = 15
#bigger pattern
totalWidth = unitWidth * 3
totalHeight = unitHeight * 3
onBed = ["f"] * totalWidth

def castOn(totalWidth):
	for i in range (totalWidth-1,-1,-2):
		file.write("tuck -" + " f" + str(i) + " " + Carriers + "\n")
	for i in range(1,totalWidth,2):
		file.write("tuck +" + " f" + str(i) + " " + Carriers + "\n")

	file.write("releasehook 6\n")

#draw sigle tile
def tilePtr(unitWidth, unitHeight):

	f = "f"
	b = "b"
	unitPtr = [ ([b] * unitWidth) for row in range(unitHeight) ]

	for row in range (unitWidth):
		for col in range(unitHeight):
			if row <= col:
				unitPtr[row][col] = f

	return(unitPtr)
#draw final pattern
def fullPtr(unitPtr, totalWidth,totalHeight):

	#TODO setup new ptr based on newWidth, new Height
	f = "f"
	b = "b"
	fullPtr = [ ([b] * totalWidth) for row in range(totalHeight) ]

	for row in range(totalWidth):
		for col in range(totalHeight):
			#TODO figure out what ii and jj should be based on width, height, new width, new height
			subRow = row%unitWidth
			subCol = col%unitHeight
			#TODO update newPtr[i][j] = sqrPtr[ii][jj]
			fullPtr[row][col] = unitPtr[subRow][subCol]
	return (fullPtr)
			
def knitRow(frontOrBack, rowConut):
	f = "f"
	b = "b"

	# do the transfer
	for i in range (0,len(onBed)):
		if frontOrBack[i] == "f" and onBed[i] == "b":
			file.write("xfer b" + str(i) + " f" + str(i) + "\n")
			onBed[i] = "f"

		elif frontOrBack[i] == "b" and onBed[i] == "f":
			file.write("xfer f" + str(i) + " b" + str(i) + "\n")
			onBed[i] = "b"
	
	#do the knitting		
	if rowConut %2 ==0:
		for i in range(len(onBed)-1,-1,-1):
			if onBed[i] == b:
				file.write("knit - " + onBed[i] + str(i) + " " + Carriers + "\n")
			else:
				file.write("knit - " + onBed[i] + str(i) + " " + Carriers + "\n")

	else:
		for i in range(0,len(onBed)):
			if onBed[i] == b:
				file.write("knit + " + onBed[i] + str(i) + " " + Carriers + "\n")
			else:
				file.write("knit + " + onBed[i] + str(i) + " " + Carriers + "\n")

#main knit command
def knit(totalWidth):
	castOn(totalWidth)
	unitPtr = tilePtr(unitWidth, unitHeight)
	finalPtr = fullPtr(unitPtr, totalWidth,totalHeight)


	rowCount = 0
	for row in finalPtr:
		knitRow(row, rowCount)
		rowCount += 1


knit(totalWidth)
file.write("outhook 6")

