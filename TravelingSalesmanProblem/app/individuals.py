from typing import Callable

from .chromosomes import Chromosome
from .chromosomes import value_to_chromosome
from .chromosomes import chromosome_to_value

class Individual:
    def __init__(self, chromosome: Chromosome, x: float, fitness_func: Callable):
        self.chromosome = value_to_chromosome(x)
        self.x = x
        self.fitness = max(0.0, fitness_func(self.x))
        
    def __repr__(self):
        return '({}, {:.2f}, {:.2f})'.format(self.chromosome, self.x, self.fitness)

    @classmethod
    def from_value(cls, x: float, fitness_func: Callable):
        return cls(value_to_chromosome(x), x, fitness_func)

    @classmethod
    def from_chromosome(cls, chromosome: Chromosome, fitness_func: Callable):
        return cls(chromosome, chromosome_to_value(chromosome), fitness_func)
