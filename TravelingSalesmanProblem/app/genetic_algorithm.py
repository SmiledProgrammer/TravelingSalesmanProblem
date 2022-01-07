from random import random, randrange
from typing import List
from statistics import median

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

    def selection_sum(self):
        fitsum = 0.0
        minfit = float("inf")
        for ind in self.population:
            fitsum = fitsum + ind.fitness
            if ind.fitness < minfit:
                minfit = ind.fitness
        cutsum = fitsum - minfit * self.population_size
        return [cutsum, minfit]

    def select(self):
        newpop = Population()
        [sum, minfit] = self.selection_sum()
        for _ in self.population:
            rnd = sum * random()
            partsum = 0.0
            j = -1
            while True:
                j = j + 1
                partsum = partsum + self.population[j].fitness - minfit
                if partsum >= rnd or j + 1 == self.population_size:
                    break
            newpop.append(self.population[j])
        self.population = newpop

    def mutate(self, allele: Allele) -> Allele:
        if flip(self.mutation_probability):
            return not allele
        else:
            return allele

    def crossover(self):
        newpop = Population()
        i = 0
        while i + 1 < self.population_size:
            if flip(self.crossover_probability):
                crosspoint = randrange(0, get_chromosome_length())
            else:
                crosspoint = get_chromosome_length()
            parent1 = self.population[i].chromosome
            parent2 = self.population[i + 1].chromosome
            child1 = Chromosome()
            child2 = Chromosome()
            for j in range(0, crosspoint):
                child1[j] = self.mutate(parent1[j])
                child2[j] = self.mutate(parent2[j])
            for j in range(crosspoint, get_chromosome_length()):
                    child1[j] = self.mutate(parent2[j])
                    child2[j] = self.mutate(parent1[j])
            individual1 = Individual.from_chromosome(child1, self.fitness_function)
            individual2 = Individual.from_chromosome(child2, self.fitness_function)
            newpop.append(individual1)
            newpop.append(individual2)
            i = i + 2
        self.population = newpop

    def save_statistics(self) -> float:
        max_x = -float("inf")
        maxfit = -float("inf")
        minfit = float("inf")
        sum = 0.0
        for ind in self.population:
            sum = sum + ind.fitness
            if ind.fitness < minfit:
                minfit = ind.fitness
            if ind.fitness > maxfit:
                maxfit = ind.fitness
                max_x = ind.x
        avgfit = sum / self.population_size
        self.max_fitness.append(maxfit)
        self.min_fitness.append(minfit)
        self.avg_fitness.append(avgfit)
        return max_x
    
    def find_max(self):
        best_x = self.save_statistics()
        best_fitness = self.max_fitness[0]
        while self.generations < self.max_generations:
            self.select()
            self.crossover()
            self.generations = self.generations + 1
            if self.generations % 10 == 0:
                print('Generation #{}...'.format(self.generations))
            gen_best_x = self.save_statistics()
            gen_best_fitness = self.max_fitness[self.generations]
            if gen_best_fitness > best_fitness:
                best_x = gen_best_x
                best_fitness = gen_best_fitness
        return [best_x, best_fitness, self.max_fitness, self.min_fitness, self.avg_fitness]
