from typing import Callable

from .chromosomes import Chromosome

class Individual:
    def __init__(self, value: str, fitness_func: Callable):
        self.chromosome = Chromosome(value)
        self.fitness = fitness_func(self.chromosome.alleles)
        
    def __repr__(self):
        return '({}, {:.2f}, {:.2f})'.format(self.chromosome, self.x, self.fitness)
