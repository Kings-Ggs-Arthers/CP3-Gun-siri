floorPyramid = int(input("Floor :"))
for x in range(floorPyramid):
    print(" "*(floorPyramid - x),"*"*((x*2)+1))

for y in range(floorPyramid):
    print(" "*(y+1), "*"*((floorPyramid*2) - ((y*2)+1)))