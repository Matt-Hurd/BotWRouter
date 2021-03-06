import matplotlib.pyplot as plt
import xml.etree.ElementTree
import numpy as np
import json
from tsp import *
import colorsys
import route_utils as botw

def main(interactive = False):
	shrines, pos = botw.load_dungeons()
	path = botw.find_route(pos, [], recalc=True)
	im = plt.imread("BotW-Map-Grid.jpg")
	implot = plt.imshow(im)
	botw.plot_shrines(pos, shrines)
	if interactive:
		plt.ion()
	botw.plot_path(path, interactive)
	if not interactive:
		plt.show()

if __name__ == '__main__':
	main()