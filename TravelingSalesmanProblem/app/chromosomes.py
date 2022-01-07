import string

CITIES_AMOUNT = 10
CITIES_SYMBOLS = string.ascii_uppercase

if CITIES_AMOUNT > len(CITIES_SYMBOLS):
    raise ValueError('Cities amount (chromosome length) is too big (max: {}).'.format(len(CITIES_SYMBOLS)))

class Chromosome:
    def __init__(self, value: str = CITIES_SYMBOLS[:CITIES_AMOUNT]):
        self.genes = value

    def __repr__(self):
        return self.genes

    def __setitem__(self, key, value):
        gstr = self.genes
        self.genes = gstr[:key] + value + gstr[key + 1:]

    def __getitem__(self, key):
        return self.genes[key]

    def set_genes(self, value: str):
        self.genes = value
    
    @classmethod
    def get_chromosome_length() -> int:
        global CITIES_AMOUNT
        return CITIES_AMOUNT
