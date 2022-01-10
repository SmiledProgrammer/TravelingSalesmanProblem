import matplotlib.pyplot as plt
import numpy as np
from typing import Callable, List, Tuple

from .cities import get_cities_symbols

def display_single_fitness_plot(plot_type: str, plot_num: int, x: List[float], y: List[float]):
    name = plot_type + ' fitness'
    plt.subplot(1, 3, plot_num)
    plt.plot(x, y)
    plt.xlabel('Generation')
    plt.ylabel(name)
    plt.title(plot_type + ' fitness in each generation', y=1.05)

def display_fitness_plots(generations: int, max_fitness: List[float], min_fitness: List[float], avg_fitness: List[float]):
    plt.figure(figsize=(15, 4.5), num='Fitness plots')
    gennums = list(range(generations + 1))
    display_single_fitness_plot('Maximal', 1, gennums, max_fitness)
    display_single_fitness_plot('Minimal', 2, gennums, min_fitness)
    display_single_fitness_plot('Average', 3, gennums, avg_fitness)
    
def display_map(plot_type: str, route_color: str, cities_coordinates: Tuple[Tuple[float]], route: List[int], route_length: float):
    figname = plot_type + ' route'
    plotname = figname + ' (length: ' + '{:.5f}'.format(route_length) + ')'
    plt.figure(figsize=(5, 5), num=figname)
    plt.title(plotname)
    plt.grid()
    plt.xticks(range(1, 11))
    plt.yticks(range(1, 11))
    for i in range(len(route)):
        city1 = cities_coordinates[route[i - 1]]
        city2 = cities_coordinates[route[i]]
        plt.plot([city1[0], city2[0]], [city1[1], city2[1]], color=route_color)
    for index, coords in enumerate(cities_coordinates):
        cx = coords[0]
        cy = coords[1]
        csymbol = get_cities_symbols()[index]
        plt.plot(cx, cy, 'ko')
        plt.annotate('  {}({}, {})'.format(csymbol, cx, cy), (cx, cy))
    