import random
from random import randint

POPULATION_SIZE = 100
LENGTH_SIZE = 150
P_CROSSOVER = 0.1
P_MUTATION = 0.9
MAX_GENERATIONS = 200


class Individual(list):
    def __init__(self, value):
        super().__init__(value)

    def fitness(self):
        if sum(self) == len(self):
            print('best fit')
        return sum(self)


def create_population(number: int, length: int):
    return [Individual([randint(0, 1) for _ in range(length)]) for _ in range(number)]


def training_population(populate: list[Individual]):
    populate.sort()
    return populate[-4:]


def mutation(individuals: [Individual]):
    rand = randint(-(LENGTH_SIZE // 3), LENGTH_SIZE // 3) + LENGTH_SIZE // 2
    return Individual(individuals[0][:rand] + individuals[1][rand:]), Individual(individuals[1][:rand] + individuals[0][rand:])


def crossover(individual: Individual):
    rand = randint(0, LENGTH_SIZE - 1)
    new_individual = Individual(individual.copy())
    new_individual[rand] = 1 - new_individual[rand]
    return new_individual


def create_new_population(populate: list[Individual]):
    new_population = []
    while len(new_population) < POPULATION_SIZE:
        if (random.choices([0, 1], [P_CROSSOVER, P_MUTATION])[0]) and (len(new_population) <= POPULATION_SIZE - 2):
            mutants = mutation(random.choices(populate, k=2))
            new_population.append(mutants[0])
            new_population.append(mutants[1])
        else:
            new_population.append(crossover(random.choice(populate)))
    return new_population


def generic_algorithm(population):
    stop = 0
    for i in range(MAX_GENERATIONS):
        print(i)
        population = create_new_population(training_population(population))
        print(f'best =  {max(population).fitness()}')
        print()
        for j in population:
            if j.fitness() == LENGTH_SIZE:
                stop = 1
                break
        if stop == 1:
            break


population = create_population(POPULATION_SIZE, LENGTH_SIZE)
generic_algorithm(population)
