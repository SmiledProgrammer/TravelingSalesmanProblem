from typing import Callable

from .chromosomes import Chromosome

class Individual:
    def __init__(self, chromosome: Chromosome, fitness_func: Callable):
        self.chromosome = chromosome
        self.fitness = fitness_func(self.chromosome)
        
    def __repr__(self):
        return '({}, {:.2f}, {:.2f})'.format(self.chromosome, self.x, self.fitness)
