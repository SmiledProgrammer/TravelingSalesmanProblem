from typing import List

from .cities import get_cities_amount, get_cities_symbols

class Chromosome:
    def __init__(self, genes: List[int] = range(get_cities_amount())):
        self.genes = genes

    def __repr__(self):
        symbols = get_cities_symbols()
        return '[' + ','.join([symbols[c] for c in self.genes]) + ']'

    def __setitem__(self, key, value):
        self.genes[key] = value

    def __getitem__(self, key):
        return self.genes[key]

    @staticmethod
    def get_length() -> int:
        return get_cities_amount()
