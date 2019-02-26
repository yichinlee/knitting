import string
import numpy as np

file = open("tileKnitting_square.k", "w")
file.write(";!knitout-2\r\n")
file.write(";;Carriers: 3 6\r\n")
file.write("inhook 6 3\r\n")
file.write("x-stitch-number 96\r\n")

CarriersA = "6 3"
CarriersB = "3 6"

#unit pattern size
unitWidth = 10
unitHeight = 10
#bigger pattern
totalWidth = unitWidth*5
totalHeight = unitHeight * 5

onBed = [f] * totalWidth

def castOn(totalWidth):
	for i in range (totalWidth-1,-1,-2):
		file.write("tuck -" + " f" + str(i*2) + " " + CarriersA + "\r\n")
	for i in range(0,totalWidth,2):
		file.write("tuck +" + " f" + str(i*2) + " " + CarriersA + "\r\n")

	file.write("releasehook 6 3" + "\r\n")

#draw sigle tile
def tilePtr(unitWidth, unitHeight):

	f = "f"
	b = "b"
	unitPtr = [ ([f] * unitWidth) for row in range(unitHeight) ]

	for row in range (unitWidth):
		for col in range(unitHeight):
			if row < (unitWidth // 2) and col < (unitHeight // 2):
				unitPtr[row][col] = b
			elif row >= (unitWidth // 2) and col >= (unitHeight // 2):
				unitPtr[row][col] = b
	return(unitPtr)

#draw final pattern
def fullPtr(unitPtr, totalWidth,totalHeight):

	#TODO setup new ptr based on newWidth, new Height
	f = "f"
	b = "b"
	fullPtr = [ ([f] * totalWidth) for row in range(totalHeight) ]

	unitWidth = len(unitPtr)
	unitHeight = len(unitPtr[0])

	for row in range(totalWidth):
		for col in range(totalHeight):
			#TODO figure out what ii and jj should be based on width, height, new width, new height
			subRow = row%unitWidth
			subCol = col%unitHeight
			#TODO update newPtr[i][j] = sqrPtr[ii][jj]
			fullPtr[row][col] = unitPtr[subRow][subCol]
	return (fullPtr)
			
def knitRow(frontOrBack, rowConut):
	knitSize = len(frontOrBack)
	unitSize = 20
	f = "f"
	b = "b"
	# do the transfer
	for i in range (0,len(onBed)):
		if frontOrBack[i] == "f" and onBed[i] == "b":
			file.write("xfer b" + str(i*2) + " f" + str(i*2) + "\r\n")
			onBed[i] = "f"

		elif frontOrBack[i] == "b" and onBed[i] == "f":
			file.write("xfer f" + str(i*2) + " b" + str(i*2) + "\r\n")
			onBed[i] = "b"
	#do the knitting		
	if rowConut %2 ==0:
		for i in range(len(onBed)-1,-1,-1):
			if onBed[i] == b:
				file.write("knit - " + onBed[i] + str(i*2) + " " + CarriersA + "\r\n")
			else:
				file.write("knit - " + onBed[i] + str(i*2) + " " + CarriersB + "\r\n")
	else:
		for i in range(0,len(onBed)):
			if onBed[i] == b:
				file.write("knit + " + onBed[i] + str(i*2) + " " + CarriersA + "\r\n")
			else:
				file.write("knit + " + onBed[i] + str(i*2) + " " + CarriersB + "\r\n")

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
file.write("outhook 6 3")

