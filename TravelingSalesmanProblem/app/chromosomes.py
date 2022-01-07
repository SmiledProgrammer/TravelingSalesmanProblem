import string
from typing import List

CITIES_AMOUNT = 5
CITIES_SYMBOLS = string.ascii_uppercase

def setup_chromosomes(citiesamount: int):
    if citiesamount > len(CITIES_SYMBOLS):
        raise ValueError('Cities amount (chromosome length) is too big (max: {}).'.format(len(CITIES_SYMBOLS)))
    else:
        global CITIES_AMOUNT
        CITIES_AMOUNT = citiesamount

class Chromosome:
    def __init__(self, genes: List[int] = range(CITIES_AMOUNT)):
        self.genes = genes

    def __repr__(self):
        return str(self.genes)

    def __setitem__(self, key, value):
        self.genes[key] = value

    def __getitem__(self, key):
        return self.genes[key]

    @staticmethod
    def get_chromosome_length() -> int:
        global CITIES_AMOUNT
        return CITIES_AMOUNT
