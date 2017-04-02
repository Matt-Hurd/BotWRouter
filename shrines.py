import matplotlib.pyplot as plt
import xml.etree.ElementTree
import numpy as np
import json
from tsp import *

class Shrine:
	def __init__(self, x, y, z, name):
		self.x = x
		self.y = y
		self.z = z
		self.name = name

with open('DungeonNames.json') as data:
	names = json.load(data)

pos = []
shrines = []
no_height = []
e = xml.etree.ElementTree.parse('DungeonPositions.xml').getroot()
e.findall('value')
for s in e:
	bad = False
	for child in s:
		if child.tag == "PosName":
			if "StartPos_CDungeon" not in child.text:
				bad = True
			else:
				name = names[child.text.split("StartPos_C")[1]]
		if not bad and child.tag == "Translate":
			y, x, z = map(float, [x[:-1] for x in s[-1].attrib.values()])
			pos.append([y, x, z])
			no_height.append([x, z])
			shrines.append(Shrine(x, y, z, name))


ar = np.asarray(pos)

del pos[56]
del pos[55]
del pos[54]
del pos[44]


koroks = []
e = xml.etree.ElementTree.parse('KorokLocations.xml').getroot()
for s in e.find('KorokLocation'):
	for child in s:
		if child.tag == "Translate":
			y, x, z = map(float, [x[:-1] for x in s[-1].attrib.values()])
			pos.append([y, x, z])
			koroks.append([y, x, z])

path = optimized_travelling_salesman(pos, pos[63])
print total_distance(path)

im = plt.imread("BotW-Map-Grid.png")
implot = plt.imshow(im)
plt.grid(False)


xlist = [(x + 5000) / 2 for x in ar[:,1].tolist()]
zlist = [(x + 4000) / 2 for x in ar[:,2].tolist()]

# x = 0
# for shrine in shrines:
#     plt.annotate(shrine.name + " " + str(x), ((shrine.x + 5000) / 2, (shrine.z + 4000) / 2))
#     x += 1

for x in range(len(path) - 1):
	plt.plot([(path[x][1] + 5000) / 2, (path[x + 1][1] + 5000) / 2], [(path[x][2] + 4000) / 2, (path[x + 1][2] + 4000) / 2], 'k-', lw=1)

plt.scatter(x=xlist, y=zlist, c='r', s=40)


ar = np.asarray(koroks)

xlist = [(x + 5000) / 2 for x in ar[:,1].tolist()]
zlist = [(x + 4000) / 2 for x in ar[:,2].tolist()]
plt.scatter(x=xlist, y=zlist, c='g', s=20)

plt.show()