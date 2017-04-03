'''https://codereview.stackexchange.com/questions/81865/travelling-salesman-using-brute-force-and-heuristics'''

import doctest
from itertools import permutations


def distance(point1, point2):
    dist = ((point1[1] - point2[1])**2 + (point1[2] - point2[2])**2) ** 0.5
    height_change = point1[0] - point2[0]
    dist = dist + (abs(height_change) * (0.2 if height_change < 0 else 3))
    return dist


def total_distance(points):
    return sum([distance(point, points[index + 1]) for index, point in enumerate(points[:-1])])

def tsp(shrines, koroks, start=None):
    if start is None:
        start = shrines[0]
    must_visit = shrines[:]
    must_visit.extend(koroks)
    # print must_visit
    path = [["walk", start]]
    visited_shrines = [start]
    must_visit.remove(start)
    while must_visit:
        minimum = None
        nearest = None
        warp_to = None
        for visited_shrine in visited_shrines:
            for place in must_visit:
                dist = distance(visited_shrine, place) + 600
                if minimum == None or dist < minimum:
                    minimum = dist
                    nearest = place
                    warp_to = visited_shrine
        for place in must_visit:
            dist = distance(path[-1][1], place)
            if minimum == None or dist < minimum:
                minimum = dist
                nearest = place
                warp_to = None
        if warp_to == None:
            path.append(["walk", nearest])
        else:
            path.append(["warp", warp_to])
            path.append(["walk", nearest])
    #     path.append(nearest)
        must_visit.remove(nearest)
        if nearest in shrines:
            visited_shrines.append(nearest)
        print nearest
    return path