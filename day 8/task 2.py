import numpy as np
import random

def calculate_total_distance(route, distance_matrix):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance_matrix[route[i]][route[i + 1]]
    total_distance += distance_matrix[route[-1]][route[0]]
    return total_distance

def create_route(n):
    route = list(range(n))
    random.shuffle(route)
    return route

def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child = [-1] * len(parent1)
    child[start:end+1] = parent1[start:end+1]

    current_position = end + 1
    for gene in parent2:
        if gene not in child:
            if current_position >= len(child):
                current_position = 0
            child[current_position] = gene
            current_position += 1
    return child

def mutate(route):
    a, b = random.sample(range(len(route)), 2)
    route[a], route[b] = route[b], route[a]

def genetic_algorithm(distance_matrix, population_size=100, generations=500, mutation_rate=0.1):
    n = len(distance_matrix)
    population = [create_route(n) for _ in range(population_size)]
    best_route = None
    best_distance = float('inf')
    best_generation = -1

    for generation in range(generations):
        population = sorted(population, key=lambda route: calculate_total_distance(route, distance_matrix))
        current_best_route = population[0]
        current_best_distance = calculate_total_distance(current_best_route, distance_matrix)
        
        if current_best_distance < best_distance:
            best_route = current_best_route
            best_distance = current_best_distance
            best_generation = generation

        new_population = population[:2]

        while len(new_population) < population_size:
            parent1, parent2 = random.choices(population[:50], k=2)
            child = crossover(parent1, parent2)
            if random.random() < mutation_rate:
                mutate(child)
            new_population.append(child)

        population = new_population

    return best_route, best_distance, best_generation

DISTANCE_MATRIX = [
    [0, 12, 30, 8],
    [12, 0, 25, 18],
    [30, 25, 0, 14],
    [8, 18, 14, 0]
]

best_route, best_distance, best_generation = genetic_algorithm(DISTANCE_MATRIX)
print(f"Best Route: {best_route}")
print(f"Best Distance: {best_distance}")
print(f"Found in Generation: {best_generation}")
