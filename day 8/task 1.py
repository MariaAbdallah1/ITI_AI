import random
N = 8
POPULATION_SIZE = 100
GENERATIONS = 100
MUTATION_RATE = 0.1

class Individual:
    def __init__(self, genome=None):
        self.genome = genome if genome is not None else list(range(N))
        random.shuffle(self.genome)
        self.fitness = self.calculate_fitness()

    def calculate_fitness(self):
        attacks = 0
        for row1, col1 in enumerate(self.genome):
            for row2, col2 in enumerate(self.genome):
                if row1 < row2:
                    if col1 == col2:
                        attacks += 1
                    elif abs(col1 - col2) == abs(row1 - row2):
                        attacks += 1
        return attacks

  
    def mutate(self):
        i1, i2 = random.sample(range(N), 2)
        self.genome[i1], self.genome[i2] = self.genome[i2], self.genome[i1]
        self.fitness = self.calculate_fitness()

    def crossover(self, other):
        start, end = sorted(random.sample(range(N), 2)) #[1, 3]
        child_genome = [-1] * N
        child_genome[start:end] = self.genome[start:end]
        current_pos = end
        for gene in other.genome:
            if gene not in child_genome:
                if current_pos >= N:
                    current_pos = 0
                child_genome[current_pos] = gene
                current_pos += 1
        return Individual(child_genome)

def main():
    population = [Individual() for _ in range(POPULATION_SIZE)]

    for generation in range(GENERATIONS):
        population.sort(key=lambda x: x.fitness)
        if population[0].fitness == 0:
            print(f"Solution found in generation {generation}: {population[0].genome}")
            return

        new_population = population[:10]

        while len(new_population) < POPULATION_SIZE:
            parent1, parent2 = random.sample(population[:50], 2)
            child = parent1.crossover(parent2)
            if random.random() < MUTATION_RATE:
                child.mutate()
            new_population.append(child)

        population = new_population

    print("No solution found.")

if __name__ == "__main__":
    main()
