import string

CITIES_AMOUNT = 10 # MAX: 26
CITIES_SYMBOLS = string.ascii_uppercase

def get_chromosome_length() -> int:
    global CITIES_AMOUNT
    return CITIES_AMOUNT

class Chromosome:
    def __init__(self, value: str = CITIES_SYMBOLS[:CITIES_AMOUNT]):
        self.alleles = value

    def __repr__(self):
        return self.alleles

    def __setitem__(self, key, value):
        alstr = self.alleles
        self.alleles = alstr[:key] + value + alstr[key + 1:]

    def __getitem__(self, key):
        return self.alleles[key]
    