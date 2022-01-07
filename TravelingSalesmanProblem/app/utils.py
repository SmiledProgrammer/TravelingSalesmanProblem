from itertools import combinations
from math import pow, sqrt
from typing import Tuple, List

def coordinates_to_distances(coordinates: Tuple[Tuple[float]]) -> List[List[float]]:
    count = len(coordinates)
    distances = [ [ 0.0 for i in range(count) ] for j in range(count) ]
    for idpair in combinations(range(count), 2):
        city1 = coordinates[idpair[0]]
        city2 = coordinates[idpair[1]]
        x1 = city1[0]
        y1 = city1[1]
        x2 = city2[0]
        y2 = city2[1]
        d = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
        distances[idpair[0]][idpair[1]] = d
        distances[idpair[1]][idpair[0]] = d
    return distances
