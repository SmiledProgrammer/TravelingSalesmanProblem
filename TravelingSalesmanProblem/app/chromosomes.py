CHROMOSOME_LENGTH = 32
CHROMOSOME_DECIMAL_PRECISION = 10**4
CHROMOSOME_VALUE_OFFSET = 2**(CHROMOSOME_LENGTH - 1)

two_powers = []
for p in range(CHROMOSOME_LENGTH):
    two_powers.append(2**p)

def setup_chromosomes(length: int, decimal_precision: int = CHROMOSOME_DECIMAL_PRECISION, value_offset: float = None):
    global CHROMOSOME_LENGTH
    global two_powers
    CHROMOSOME_LENGTH = length
    for p in range(CHROMOSOME_LENGTH):
        two_powers.append(2**p)

    global CHROMOSOME_DECIMAL_PRECISION
    CHROMOSOME_DECIMAL_PRECISION = decimal_precision
    
    global CHROMOSOME_VALUE_OFFSET
    if value_offset == None:
        CHROMOSOME_VALUE_OFFSET = two_powers[-1]
    else:
        CHROMOSOME_VALUE_OFFSET = two_powers[-1] - value_offset * CHROMOSOME_DECIMAL_PRECISION

def get_chromosome_length() -> int:
    global CHROMOSOME_LENGTH
    return CHROMOSOME_LENGTH


Allele = bool

class Chromosome:
    def __init__(self):
        self.alleles = []
        for _ in range(CHROMOSOME_LENGTH):
            self.alleles.append(False)

    def __repr__(self):
        s = ''
        for al in self.alleles:
            if al:
                s = s + '1'
            else:
                s = s + '0'
        return s

    def __setitem__(self, key, value):
        self.alleles[key] = value

    def __getitem__(self, key):
        return self.alleles[key]
    
def value_to_chromosome(value: float) -> Chromosome:
    chromosome = Chromosome()
    code_value = int(value * CHROMOSOME_DECIMAL_PRECISION) + CHROMOSOME_VALUE_OFFSET
    for p in reversed(range(CHROMOSOME_LENGTH)):
        power = two_powers[p]
        if code_value >= power:
            chromosome[p] = True
            code_value = code_value - power
        else:
            chromosome[p] = False
    return chromosome

def chromosome_to_value(chromosome: Chromosome) -> float:
    code_value = 0.0
    for p in range(CHROMOSOME_LENGTH):
        if chromosome[p]:
            code_value = code_value + two_powers[p]
    return (code_value - CHROMOSOME_VALUE_OFFSET) / CHROMOSOME_DECIMAL_PRECISION

def print_chromosome_value_range():
    minchr = Chromosome()
    maxchr = Chromosome()
    for i in range(CHROMOSOME_LENGTH):
        maxchr[i] = True
    print('Chromosome value range: <{}, {}>'.format(chromosome_to_value(minchr), chromosome_to_value(maxchr)))
