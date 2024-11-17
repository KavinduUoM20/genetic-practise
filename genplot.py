import random
import matplotlib.pyplot as plt

# Define the function to maximize
def fitness_function(x):
    return x ** 2

# Genetic Algorithm Parameters
POP_SIZE = 10       # Population size
GENE_LENGTH = 5     # Binary string length (for numbers 0 to 31)
MUTATION_RATE = 0.1 # Mutation probability
GENERATIONS = 20    # Number of generations

# Generate initial population (random binary strings)
def initialize_population(size, gene_length):
    return [''.join(random.choice('01') for _ in range(gene_length)) for _ in range(size)]

# Decode binary string to integer
def decode(individual):
    return int(individual, 2)

# Evaluate fitness for the population
def evaluate_population(population):
    return [fitness_function(decode(individual)) for individual in population]

# Select parents using tournament selection
def select_parents(population, fitness):
    parents = []
    for _ in range(len(population)):
        tournament = random.sample(list(zip(population, fitness)), k=3)
        parents.append(max(tournament, key=lambda x: x[1])[0])
    return parents

# Perform single-point crossover
def crossover(parent1, parent2):
    point = random.randint(1, GENE_LENGTH - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

# Perform mutation
def mutate(individual, mutation_rate):
    mutated = ''.join(
        bit if random.random() > mutation_rate else str(1 - int(bit)) for bit in individual
    )
    return mutated

# Genetic Algorithm Main Loop
def genetic_algorithm():
    # Step 1: Initialize population
    population = initialize_population(POP_SIZE, GENE_LENGTH)
    
    # For plotting
    best_fitness_per_generation = []
    avg_fitness_per_generation = []
    
    for generation in range(GENERATIONS):
        # Step 2: Evaluate fitness
        fitness = evaluate_population(population)
        best_fitness = max(fitness)
        avg_fitness = sum(fitness) / len(fitness)
        best_fitness_per_generation.append(best_fitness)
        avg_fitness_per_generation.append(avg_fitness)
        
        print(f"Generation {generation}: Best fitness = {best_fitness}, Avg fitness = {avg_fitness:.2f}")
        
        # Step 3: Select parents
        parents = select_parents(population, fitness)
        
        # Step 4: Perform crossover and mutation
        next_generation = []
        for i in range(0, len(parents), 2):
            parent1 = parents[i]
            parent2 = parents[(i + 1) % len(parents)]
            child1, child2 = crossover(parent1, parent2)
            next_generation.append(mutate(child1, MUTATION_RATE))
            next_generation.append(mutate(child2, MUTATION_RATE))
        
        # Step 5: Replace old population with new generation
        population = next_generation

    # Step 6: Return the best solution and the fitness history
    best_individual = max(population, key=lambda ind: fitness_function(decode(ind)))
    return decode(best_individual), fitness_function(decode(best_individual)), best_fitness_per_generation, avg_fitness_per_generation

# Run the genetic algorithm
best_solution, best_fitness, best_fitness_per_generation, avg_fitness_per_generation = genetic_algorithm()

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(best_fitness_per_generation, label="Best Fitness", marker='o')
plt.plot(avg_fitness_per_generation, label="Average Fitness", marker='s')
plt.title("Genetic Algorithm Progress")
plt.xlabel("Generation")
plt.ylabel("Fitness")
plt.legend()
plt.grid(True)
plt.show()

print(f"Best solution: x = {best_solution}, f(x) = {best_fitness}")
