import sys
import matplotlib.pyplot as plt
from typing import List, Tuple

from .chromosomes import setup_chromosomes
from .populations import Population
#from .genetic_algorithm import GeneticAlgorithm
from .plots import display_fitness_plots
from .utils import coordinates_to_distances

def fitness(route: List[int], distances: List[List[float]]) -> float:
    total = 0.0
    for i in range(len(route)):
        city1 = route[i - 1]
        city2 = route[i]
        total = total + distances[city1][city2]
    return total

def run(population_size: int, mutation_probability: float, iterations: int, cities_coordinates: Tuple[Tuple[float]]):
    print('Starting the optimization...')

    setup_chromosomes(len(cities_coordinates))
    cities_distances = coordinates_to_distances(cities_coordinates)
    initpop = Population.random(population_size, fitness, cities_distances)

    ga = GeneticAlgorithm()
    ga.setup(fitness, cities_distances, initpop, mutation_probability, iterations)
    [max_x, max_value, max_fitness, min_fitness, avg_fitness] = ga.find_max()
    print('Best: route = {}, length = {}'.format(max_x, max_value))

    #display_map() # shortest
    #display_map() # longest
    display_fitness_plots(max_generations, max_fitness, min_fitness, avg_fitness)
    plt.show()
