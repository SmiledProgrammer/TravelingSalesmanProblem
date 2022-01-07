from typing import List, Callable

from .chromosomes import Chromosome

class Individual:
    def __init__(self, genes: List[int], fitness_func: Callable, cities_distances: List[List[float]]):
        self.chromosome = Chromosome(genes)
        self.fitness = fitness_func(genes, cities_distances)
        
    def __repr__(self):
        return '({}, {:.2f}, {:.2f})'.format(self.chromosome, self.x, self.fitness)
