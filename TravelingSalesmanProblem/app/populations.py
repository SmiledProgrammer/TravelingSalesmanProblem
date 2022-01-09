from typing import List, Callable
from random import randrange

from .chromosomes import Chromosome
from .individuals import Individual

MAX_POPULATION_SIZE = 100

class Population:
    def __init__(self, routes: List[List[int]] = []):
        if len(routes) > MAX_POPULATION_SIZE:
            raise ValueError('Population size is too big (max: {}).'.format(MAX_POPULATION_SIZE))
        self.individuals = []
        for r in routes:
            ind = Individual(r)
            self.individuals.append(ind)

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

    @classmethod
    def random(cls, popsize: int) -> 'Population':
        chrlen = Chromosome.get_length()
        print(chrlen)
        routes = []
        for _ in range(popsize):
            cities = list(range(chrlen))
            route = []
            for i in range(chrlen):
                r = randrange(len(cities))
                route.append(cities.pop(r))
            routes.append(route)
        return cls(routes)
