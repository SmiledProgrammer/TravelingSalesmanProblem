from random import random, randrange, sample
from typing import List, Tuple
from statistics import median
from copy import deepcopy
from itertools import chain

from .chromosomes import Chromosome
from .individuals import Individual
from .populations import Population

def flip(probability: float) -> float:
    return random() < probability

class GeneticAlgorithm:
    def setup(self, init_pop: Population, crossover_prob: float, mutation_prob: float, iterations: int):
        self.population = init_pop
        self.population_size = len(self.population)
        self.crossover_probability = crossover_prob
        self.mutation_probability = mutation_prob
        self.iterations = iterations
        self.generations = 0
        self.max_fitness = []
        self.min_fitness = []
        self.avg_fitness = []

    def selection_sum(self) -> Tuple[float, float]:
        fitsum = 0.0
        maxfit = -float("inf")
        for ind in self.population:
            fitsum = fitsum + ind.fitness
            if ind.fitness > maxfit:
                maxfit = ind.fitness
        cutsum = maxfit * self.population_size - fitsum
        return (cutsum, maxfit)

    def select(self):
        newpop = Population()
        [sum, maxfit] = self.selection_sum()
        for _ in self.population:
            rnd = sum * random()
            partsum = 0.0
            j = -1
            while True:
                j = j + 1
                partsum = partsum + maxfit - self.population[j].fitness
                if partsum >= rnd or j + 1 == self.population_size:
                    break
            newpop.append(self.population[j])
        self.population = newpop

    def mutate(self, chromosome: Chromosome):
        if flip(self.mutation_probability):
            m1, m2 = sample(range(Chromosome.get_length()), 2)
            mutval = chromosome[m1]
            chromosome[m1] = chromosome[m2]
            chromosome[m2] = mutval

    def crossover(self):
        newpop = Population()
        i = 0
        while i + 1 < self.population_size:
            ind1 = self.population[i]
            ind2 = self.population[i + 1]
            if flip(self.crossover_probability):
                child1, child2 = self.single_pmx_crossover(ind1.chromosome, ind2.chromosome)
                self.mutate(child1)
                self.mutate(child2)
                newind1 = Individual(child1.genes)
                newind2 = Individual(child2.genes)
                newpop.append(newind1)
                newpop.append(newind2)
            else:
                newpop.append(ind1)
                newpop.append(ind2)
            i = i + 2
        self.population = newpop

    def single_pmx_crossover(self, parent1: Chromosome, parent2: Chromosome) -> Tuple[Chromosome, Chromosome]:
        chrlen = Chromosome.get_length()
        leftx = randrange(0, chrlen)
        rightx = randrange(leftx + 1, chrlen + 1)
        child1 = Chromosome(deepcopy(parent1.genes))
        child2 = Chromosome(deepcopy(parent2.genes))
        chars1 = {}
        chars2 = {}
        for j in range(leftx, rightx):
            c1 = parent1[j]
            c2 = parent2[j]
            chars1[c2] = c1
            chars2[c1] = c2
            child1[j] = parent2[j]
            child2[j] = parent1[j]
        for i in chain(range(leftx), range(rightx, chrlen)):
            while child1[i] in chars1:
                child1[i] = chars1[child1[i]]
            while child2[i] in chars2:
                child2[i] = chars2[child2[i]]
        return (child1, child2)

    def save_statistics(self) -> Tuple[float, float]:
        minr = -float("inf")
        maxr = -float("inf")
        minfit = float("inf")
        maxfit = -float("inf")
        sum = 0.0
        for ind in self.population:
            sum = sum + ind.fitness
            if ind.fitness < minfit:
                minfit = ind.fitness
                minr = ind.chromosome.genes
            if ind.fitness > maxfit:
                maxfit = ind.fitness
                maxr = ind.chromosome.genes
        avgfit = sum / self.population_size
        self.min_fitness.append(minfit)
        self.max_fitness.append(maxfit)
        self.avg_fitness.append(avgfit)
        return (minr, maxr)
    
    def find_route(self):
        [shortest, longest] = self.save_statistics()
        best_fit = self.min_fitness[0]
        worst_fit = self.max_fitness[0]
        while self.generations < self.iterations:
            self.select()
            self.crossover()
            self.generations = self.generations + 1
            if self.generations % 10 == 0:
                print('Generation #{}...'.format(self.generations))
            [gen_shortest, gen_longest] = self.save_statistics()
            gen_best_fit = self.min_fitness[self.generations]
            gen_worst_fit = self.max_fitness[self.generations]
            if gen_best_fit < best_fit:
                shortest = gen_shortest
                best_fit = gen_best_fit
            if gen_worst_fit > worst_fit:
                longest = gen_longest
                worst_fit = gen_worst_fit
        return [shortest, best_fit, longest, worst_fit, self.min_fitness, self.max_fitness, self.avg_fitness]
