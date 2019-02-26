import string

print(";!knitout-2")
print(";;Carriers: 3 6")
print("inhook 6 3")
print("x-stitch-number 96")

CarriersA = "6 3"
CarriersB = "3 6"
knitSize = 30 

for i in range (knitSize-1,-1,-2):
	print ("tuck -" + " f" + str(i*2) + " " + CarriersA)
for i in range(0,knitSize,2):
	print ("tuck +" + " f" + str(i*2) + " " + CarriersA)


print("releasehook 6 3")

f = "f"
b = "b"
onBed = [f] * knitSize

knitPattern = [ ([f] * knitSize) for row in range(knitSize) ]


for row in range(0, knitSize/2):
	for col in range(row, knitSize/2):
		knitPattern[row][col] = b

for row in range(0, knitSize/2):
	for col in range(knitSize - row , knitSize):
		knitPattern[row][col] = b

for row in range(knitSize/2, knitSize):
	for col in range(0, knitSize - row):
		knitPattern[row][col] = b

for row in range(knitSize/2, knitSize):
	for col in range(knitSize/2, row):
		assert col >= 15, "else this wont be run"
		knitPattern[row][col] = b

def knitRow(frontOrBack, rowConut):

	for i in range (0,len(onBed)):
		if frontOrBack[i] == "f" and onBed[i] == "b":
			print("xfer b" + str(i*2) + " f" + str(i*2))
			onBed[i] = "f"

		elif frontOrBack[i] == "b" and onBed[i] == "f":
			print("xfer f" + str(i*2) + " b" + str(i*2))
			onBed[i] = "b"
	#do the knitting		
	if rowConut %2 ==0:
		for i in range(len(onBed)-1,-1,-1):
			if onBed[i] == b:
				print("knit - " + onBed[i] + str(i*2) + " " + CarriersA)
			else:
				print("knit - " + onBed[i] + str(i*2) + " " + CarriersB)

	else:
		for i in range(0,len(onBed)):
			if onBed[i] == b:
				print("knit + " + onBed[i] + str(i*2) + " " + CarriersA)
			else:
				print("knit + " + onBed[i] + str(i*2) + " " + CarriersB)


#print commend
rowCount = 0
for row in knitPattern:
	knitRow(row, rowCount)
	rowCount += 1

print("outhook 6 3")

