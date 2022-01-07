import string
import itertools
from math import pow, sqrt
from typing import Tuple, List

CITIES_AMOUNT = 5
CITIES_SYMBOLS = string.ascii_uppercase
CITIES_DISTANCES = []

def set_cities_amount(value: int):
    if value > len(CITIES_SYMBOLS):
        raise ValueError('Cities amount (chromosome length) is too big (max: {}).'.format(len(CITIES_SYMBOLS)))
    global CITIES_AMOUNT
    CITIES_AMOUNT = value
    
def get_cities_amount() -> int:
    global CITIES_AMOUNT
    return CITIES_AMOUNT

def set_cities_distances(distances: List[List[float]]):
    global CITIES_DISTANCES
    CITIES_DISTANCES = distances

def get_cities_distances() -> List[List[float]]:
    global CITIES_DISTANCES
    return CITIES_DISTANCES

def coordinates_to_distances(coordinates: Tuple[Tuple[float]]) -> List[List[float]]:
    count = len(coordinates)
    distances = [ [ 0.0 for i in range(count) ] for j in range(count) ]
    for idpair in itertools.combinations(range(count), 2):
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
