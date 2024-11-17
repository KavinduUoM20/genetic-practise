import random

# Define the objective function
def foo(x, y, z):
    return 6 * x**3 + 9 * y**2 + 90 * z - 25

# Define the fitness function
def fitness(x, y, z):
    ans = foo(x, y, z)
    if ans == 0:
        return 9999
    else:
        return abs(1 / ans)

# Initialize solutions with three random values (x, y, z)
solutions = []
for s in range(1000):
    solutions.append((
        random.uniform(0, 10000),  # x
        random.uniform(0, 10000),  # y
        random.uniform(0, 10000)   # z
    ))

# Main loop for genetic algorithm
for i in range(1000):
    rankedsolutions = []
    for s in solutions:
        rankedsolutions.append((fitness(s[0], s[1], s[2]), s))
    rankedsolutions.sort()  # Sort by fitness
    rankedsolutions.reverse()  # Highest fitness first

    # Print the best solution of the generation
    print(f"==== Gen {i}'s Best Solution ====")
    print(rankedsolutions[0])

    if rankedsolutions[0][0] > 999:
        break

    # Keep the top 100 solutions
    bestsolutions = rankedsolutions[:100]

    # Gather elements from the top solutions
    elements = []
    for s in bestsolutions:
        elements.append(s[1][0])  # x
        elements.append(s[1][1])  # y
        elements.append(s[1][2])  # z

    # Generate a new generation
    newgen = []
    for _ in range(1000):
        e1 = random.choice(elements) * random.uniform(0.99, 1.01)
        e2 = random.choice(elements) * random.uniform(0.99, 1.01)
        e3 = random.choice(elements) * random.uniform(0.99, 1.01)
        newgen.append((e1, e2, e3))

    # Update solutions with the new generation
    solutions = newgen
