import matplotlib.pyplot as plt
import xml.etree.ElementTree
import numpy as np
import json
from tsp import *
import colorsys

class Shrine:
	def __init__(self, x, y, z, name):
		self.x = x
		self.y = y
		self.z = z
		self.name = name


def load_dungeons():
	with open('DungeonNames.json') as data:
		names = json.load(data)

	pos = []
	shrines = []
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
				shrines.append(Shrine(x, y, z, name))
	return shrines, pos

def load_koroks():
	koroks = []
	e = xml.etree.ElementTree.parse('KorokLocations.xml').getroot()
	for s in e.find('KorokLocation'):
		for child in s:
			if child.tag == "Translate":
				y, x, z = map(float, [x[:-1] for x in s[-1].attrib.values()])
				koroks.append([y, x, z])
	return koroks


def find_route(pos, koroks, recalc = False, start=67):
	if recalc:
		path = tsp(pos, koroks, pos[start])
		with open("route.json", 'wb') as outfile:
		    json.dump(path, outfile)
	else:
		with open('route.json') as data:
			path = json.load(data)
	return path


def plot_shrines(pos, shrines, show_names = False):
	ar = np.asarray(pos)
	xlist = [(x + 5000)/ 20 for x in ar[:,1].tolist()]
	zlist = [(x + 4000)/ 20 for x in ar[:,2].tolist()]
	if show_names:
		x = 0
		for shrine in shrines:
		    plt.annotate(shrine.name + " " + str(x), ((shrine.x + 5000)/ 20, (shrine.z + 4000)/ 20))
		    x += 1
	plt.scatter(x=xlist, y=zlist, c='r', s=40)

def plot_koroks(koroks):
	ar = np.asarray(koroks)
	xlist = [(x + 5000)/ 20 for x in ar[:,1].tolist()]
	zlist = [(x + 4000)/ 20 for x in ar[:,2].tolist()]
	plt.scatter(x=xlist, y=zlist, c='g', s=20)

def plot_path(path, interactive = False):
	for x in range(len(path) - 1):
		a = 1.0 if path[x + 1][0] == 'walk' else 0.4
		c = colorsys.hsv_to_rgb((x + 1) / float(len(path)),1,1)
		start_x = (path[x][1][1] + 5000)/ 20
		start_y = (path[x][1][2] + 4000)/ 20
		end_x = (path[x + 1][1][1] + 5000)/ 20
		end_y = (path[x + 1][1][2] + 4000)/ 20
		plt.arrow(start_x, start_y, end_x - start_x, end_y - start_y, head_width=2, head_length=4,length_includes_head=True, alpha=a, color=c)
		if interactive:
			plt.pause(0.01)

def main(interactive = False):
	shrines, pos = load_dungeons()
	koroks = load_koroks()
	path = find_route(pos, koroks)
	im = plt.imread("BotW-Map-Grid.jpg")
	implot = plt.imshow(im)
	plot_shrines(pos, shrines)
	plot_koroks(koroks)
	if interactive:
		plt.ion()
	plot_path(path, interactive)
	if not interactive:
		plt.show()

if __name__ == '__main__':
	main()