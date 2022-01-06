import sys
import matplotlib.pyplot as plt
from typing import List

from .chromosomes import setup_chromosomes
from .genetic_algorithm import GeneticAlgorithm
from .plots import display_function_plot
from .plots import display_fitness_plots

def run(initial_population: List[float], mutation_probability: float, max_generations: int):
    print('Starting the optimization...')

    chrlen = 5
    chrprec = 1
    chroffset = 14.0
    setup_chromosomes(chrlen, chrprec, chroffset)

    ga = GeneticAlgorithm()
    ga.setup(fitness_function, initial_population, crossover_probability, mutation_probability, max_generations)
    [max_x, max_value, max_fitness, min_fitness, avg_fitness] = ga.find_max()
    print('Best: x = {}, f(x) = {}'.format(max_x, max_value))

    figname = 'f(x) = -0.2x^2 + 5.5x + 6'
    display_function_plot(fitness_function, figname, max_x, max_value, initial_population[0], initial_population[-1])
    display_fitness_plots(max_generations, max_fitness, min_fitness, avg_fitness)
    plt.show()
