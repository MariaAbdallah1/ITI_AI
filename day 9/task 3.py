import numpy as np
import random

class GA_ShiftScheduling:
    def __init__(self, no_employees, no_shifts, available, preferences, max_generations, population_size, mutation_rate):
        self.no_employees = no_employees
        self.no_shifts = no_shifts
        self.available = available
        self.preferences = preferences
        self.max_generations = max_generations
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.population = self.initial_population()

    def initial_population(self):
        population = []
        for _ in range(self.population_size):
            schedule = np.random.randint(0, self.no_employees, size=self.no_shifts)
            population.append(schedule)
        return population

    def cost(self, schedule):
        cost = 0
        for shift in range(self.no_shifts):
            emp = schedule[shift]
            if emp not in self.available[shift]:
                cost += 1
            if self.preferences[shift][emp] > 1:
                cost += 1
        return cost

    def crossover(self, parent1, parent2):
        point = np.random.randint(1, self.no_shifts - 1)
        child = np.concatenate((parent1[:point], parent2[point:]))
        return child

    def mutate(self, schedule):
        if np.random.rand() < self.mutation_rate:
            i = np.random.randint(self.no_shifts)
            schedule[i] = np.random.randint(self.no_employees)
        return schedule

    def run(self):
        for generation in range(self.max_generations):
            selected_population = sorted(self.population, key=self.cost)[:self.population_size // 2] 
            new_population = []
            while len(new_population) < self.population_size:
                parent1, parent2 = random.sample(selected_population, 2)
                child = self.crossover(parent1, parent2)
                child = self.mutate(child)
                new_population.append(child)
            self.population = new_population
            best_schedule = min(self.population, key=self.cost)
            print(f"Generation {generation}: Best Cost = {self.cost(best_schedule)}")

        return min(self.population, key=self.cost)

if __name__ == "__main__":
    no_employees = 10
    no_shifts = 20
    available = [list(range(no_employees)) for _ in range(no_shifts)]
    preferences = [np.random.randint(0, 10, no_employees) for _ in range(no_shifts)]

    schedule = GA_ShiftScheduling(no_employees, no_shifts, available, preferences, 100, 50, 0.1)
    best_schedule = schedule.run()
    print("Best schedule:", best_schedule)
    print("Cost of best schedule:", schedule.cost(best_schedule))
