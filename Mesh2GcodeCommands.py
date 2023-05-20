#!/bin/python3
# converts PrintBed Mesh values to Gcode commands 


sizeXY = 0
with open("goodMesh.txt", "r") as f:
	sizeXY = f.read().count("\n")

	# Creates a list containing 5 lists, each of 8 items, all set to 0
	Matrix = [[0 for x in range(sizeXY)] for y in range(sizeXY)]
	f.seek(0)
	for y in range(9,-1,-1):	#2D Array füllen
		Matrix[y] = f.readline().removesuffix("\n").split("\t")
	
for y in range(sizeXY-1,-1,-1):
	#print( str(y) + ":", end="")
	for x in range(sizeXY):
		#print(str(x) + " ", end="")
		#M421 I3 J3 Z0.0000
		print("M421", "I" + str(x), "J" + str(y), "Z" + str(Matrix[y][x]))
	#print()
