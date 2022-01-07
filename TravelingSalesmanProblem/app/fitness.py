from typing import List

from .cities import get_cities_distances

def fitness(route: List[int]) -> float:
    distances = get_cities_distances()
    total = 0.0
    for i in range(len(route)):
        city1 = route[i - 1]
        city2 = route[i]
        total = total + distances[city1][city2]
    return total
