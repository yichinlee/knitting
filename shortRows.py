import string
import numpy as np

file = open("shortRows.k", "w")	

file.write(";!knitout-2\r\n")
file.write(";;Carriers: 3 6\r\n")
file.write("inhook 6 3\r\n")
file.write("x-stitch-number 96\r\n")

Carriers = "6"

knitSize = 30

def castOn(totalWidth):
	for i in range (totalWidth-1,-1,-2):
		file.write("tuck -" + " f" + str(i*2) + " " + CarriersA + "\r\n")
	for i in range(0,totalWidth,2):
		file.write("tuck +" + " f" + str(i*2) + " " + CarriersA + "\r\n")
	file.write("releasehook 6 3" + "\r\n")

def shortRows():
	while (a == )
		for i in range (a,b):


