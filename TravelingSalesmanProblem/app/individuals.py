from typing import List, Callable

from .chromosomes import Chromosome
from .fitness import fitness

class Individual:
    def __init__(self, genes: List[int]):
        self.chromosome = Chromosome(genes)
        self.fitness = fitness(genes)
        
    def __repr__(self):
        return '({}, {:.2f}, {:.2f})'.format(self.chromosome.genes, self.fitness)
