from typing import List
from typing import Callable

from .individuals import Individual

MAX_POPULATION_SIZE = 100

class Population:
    def __init__(self):
        self.individuals = []
        
    def __repr__(self):
        s = '{\n'
        for i, ind in enumerate(self.individuals):
            s = s + '{}: [{}]\n'.format(i, ind)
        s = s + '}'
        return s

    def __setitem__(self, key, value):
        self.individuals[key] = value

    def __getitem__(self, key):
        return self.individuals[key]
    
    def __len__(self):
        return len(self.individuals)

    def append(self, value):
        self.individuals.append(value)

def create_population(values: List[float], fitness_func: Callable) -> Population:
    if len(values) > MAX_POPULATION_SIZE:
        raise ValueError('Population size is too big.')
    population = Population()
    for x in values:
        ind = Individual.from_value(x, fitness_func)
        population.append(ind)
    return population
