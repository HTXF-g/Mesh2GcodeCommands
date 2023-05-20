#!/bin/python3
# converts PrintBed Mesh values to Gcode commands 



with open("goodMesh.txt", "r") as f:
	sizeXY = f.read().count("\n")

	# Creates a list containing 5 lists, each of 8 items, all set to 0
	Matrix = [[0 for x in range(sizeXY)] for y in range(sizeXY)]
	f.seek(0)
	for y in range(9,-1,-1):	#2D Array füllen
		Matrix[y] = f.readline().removesuffix("\n").split("\t")
		print(Matrix[y])
	
with open("OUTPUT_setUBL-Mesh.gcode", "w", encoding="utf-8") as f:
	for y in range(sizeXY-1,-1,-1):
		for x in range(sizeXY):
			#M421 I3 J3 Z0.0000
			line = "M421 I" + str(x) + " J" + str(y) + " Z" + str(Matrix[y][x]).replace(",", ".")
			print(line)
			f.write(line + "\n")
	