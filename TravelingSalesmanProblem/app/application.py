import sys
import matplotlib.pyplot as plt
from typing import List, Tuple

from .cities import set_cities_amount, coordinates_to_distances, set_cities_distances
from .populations import Population
from .genetic_algorithm import GeneticAlgorithm
from .plots import display_fitness_plots, display_map

def run(population_size: int, iterations: int, crossover_probability: float, mutation_probability: float, cities_coordinates: Tuple[Tuple[float]]):
    print('Starting the optimization...')

    set_cities_amount(len(cities_coordinates))
    cities_distances = coordinates_to_distances(cities_coordinates)
    set_cities_distances(cities_distances)
    initpop = Population.random(population_size)

    ga = GeneticAlgorithm()
    ga.setup(initpop, crossover_probability, mutation_probability, iterations)
    [best_route, best_len, worst_route, worst_len, min_fitness, max_fitness, avg_fitness] = ga.find_route()
    print('Best: route = {}, length = {}'.format(best_route, best_len))
    print('Worst: route = {}, length = {}'.format(worst_route, worst_len))

    display_fitness_plots(iterations, max_fitness, min_fitness, avg_fitness)
    display_map('Longest', 'r', cities_coordinates, worst_route, worst_len)
    display_map('Shortest', 'g', cities_coordinates, best_route, best_len)
    plt.show()
