from typing import List

from .cities import get_cities_amount

class Chromosome:
    def __init__(self, genes: List[int] = range(get_cities_amount())):
        self.genes = genes

    def __repr__(self):
        return str(self.genes)

    def __setitem__(self, key, value):
        self.genes[key] = value

    def __getitem__(self, key):
        return self.genes[key]

    @staticmethod
    def get_length() -> int:
        return get_cities_amount()
