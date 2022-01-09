import sys
import matplotlib.pyplot as plt
from typing import List, Tuple

from .cities import set_cities_amount, coordinates_to_distances, set_cities_distances
from .populations import Population
from .genetic_algorithm import GeneticAlgorithm
from .plots import display_fitness_plots

def run(population_size: int, mutation_probability: float, iterations: int, cities_coordinates: Tuple[Tuple[float]]):
    print('Starting the optimization...')

    set_cities_amount(len(cities_coordinates))
    cities_distances = coordinates_to_distances(cities_coordinates)
    set_cities_distances(cities_distances)
    initpop = Population.random(population_size)
    crossprob = 0.5

    ga = GeneticAlgorithm()
    ga.setup(initpop, crossprob, mutation_probability, iterations)
    [max_x, max_value, max_fitness, min_fitness, avg_fitness] = ga.find_route()
    print('Best: route = {}, length = {}'.format(max_x, max_value))

    #display_map() # shortest
    #display_map() # longest
    display_fitness_plots(max_generations, max_fitness, min_fitness, avg_fitness)
    plt.show()
