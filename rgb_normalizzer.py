import sys

r = int(sys.argv[1].strip(",")) / 256
g = int(sys.argv[2].strip(",")) / 256
b = int(sys.argv[3].strip(",")) / 256

print( str(r) + "f, " + str(g) + "f, " + str(b) + "f")

