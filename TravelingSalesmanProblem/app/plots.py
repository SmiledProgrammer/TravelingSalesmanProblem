import matplotlib.pyplot as plt
import numpy as np
from typing import List
from typing import Callable

def display_function_plot(func: Callable, figname: str, foundpointx: float, foundpointy: float, startval: float, endval: float, dividepoints: int = 100):
    funcx = np.linspace(startval, endval, dividepoints)
    funcy = func(funcx)
    funcfig = plt.figure(num=figname)
    ax = funcfig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.xaxis.set_tick_params(bottom='on', top='off', direction='inout')
    ax.yaxis.set_tick_params(left='on', right='off', direction='inout')
    ax.plot(funcx, funcy)
    ax.plot(foundpointx, foundpointy, 'bo')
    ax.annotate('({:.4f}, {:.4f})'.format(foundpointx, foundpointy), (foundpointx, foundpointy))
    ax.set_ylim(bottom=0)

def display_single_fitness_plot(plottype: str, plotnum: int, x: List[float], y: List[float]):
    name = plottype + ' fitness'
    plt.subplot(1, 3, plotnum)
    plt.plot(x, y)
    plt.xlabel('Generation')
    plt.ylabel(name)
    plt.title(plottype + ' fitness in each generation', y=1.05)

def display_fitness_plots(generations: int, max_fitness: List[float], min_fitness: List[float], avg_fitness: List[float]):
    plt.figure(figsize=(15, 4.5), num='Fitness plots')
    gennums = list(range(generations + 1))
    display_single_fitness_plot('Maximal', 1, gennums, max_fitness)
    display_single_fitness_plot('Minimal', 2, gennums, min_fitness)
    display_single_fitness_plot('Average', 3, gennums, avg_fitness)
