import random
import Solution as sl


# create a random Solution --> shuffle node list randomly
def create_random_list(n_list):
    start = n_list[0]  # start and end points should be same, so keep the first point before shuffling

    temp = n_list[1:]
    temp = random.sample(temp, len(temp))  # shuffle the node list

    temp.insert(0, start)  # add start point to the beginning of the Solution
    temp.append(start)  # add start point to the end, because route should be ended where it started
    return temp


# initialization
def initialization(data, pop_size):
    initial_population = []
    for i in range(0, pop_size):  # create Solutions as much as population size
        temp = create_random_list(data) #creates random list of cities (possible solution) 
        new_sl = sl.Solution(temp) #Calc total dist
        initial_population.append(new_sl)
    return initial_population


# selection of parent Solutions to create child Solutions
def selection(population):  # tournament selection
    Lot_numbers_1, Lot_numbers_2, Lot_numbers_3, Lot_numbers_4 = random.sample(range(0, 99), 4)  # random 4 Lot_numbers       #fro 0 to 99 assuming the population is 100 

    # create candidate Solutions based on Lot_numbers
    candidate_1 = population[Lot_numbers_1]
    candidate_2 = population[Lot_numbers_2]
    candidate_3 = population[Lot_numbers_3]
    candidate_4 = population[Lot_numbers_4]

    # select the winner according to their costs
    if candidate_1.fitness_value > candidate_2.fitness_value:
        winner = candidate_1
    else:
        winner = candidate_2

    if candidate_3.fitness_value > winner.fitness_value:
        winner = candidate_3

    if candidate_4.fitness_value > winner.fitness_value:
        winner = candidate_4

    return winner  # winner = Solution



# 1 One point crossover
def crossover(p_1, p_2):
    one_point = random.randint(2, 16)  # Tried 58 bad results

    child_1 = p_1.Solution[1:one_point]
    child_2 = p_2.Solution[1:one_point]

    child_1_remain = [item for item in p_2.Solution[1:-1] if item not in child_1]
    child_2_remain = [item for item in p_1.Solution[1:-1] if item not in child_2]
    
    # that are not already in the child. This ensures that each node only appears once in each child, which is necessary because each solution represents a route that visits each node once.

    child_1 += child_1_remain
    child_2 += child_2_remain

    child_1.insert(0, p_1.Solution[0])
    child_1.append(p_1.Solution[0])

    child_2.insert(0, p_2.Solution[0])
    child_2.append(p_2.Solution[0])

    return child_1, child_2



# Mutation operation
def mutation(Solution):  # swap two nodes of the Solution
    mutation_index_1, mutation_index_2 = random.sample(range(1, 58), 2)
    Solution[mutation_index_1], Solution[mutation_index_2] = Solution[mutation_index_2], Solution[mutation_index_1]
    return Solution


# Find the best Solution of the generation based on the cost
def find_best(generation):
    best = generation[0]
    for n in range(1, len(generation)):
        if generation[n].cost < best.cost:
            best = generation[n]
    return best


# create a new generation based on a previous generation using elitism, crossover, mutation operators to 
def create_new_generation(previous_generation, mutation_rate):
    new_generation = [find_best(previous_generation)]  # This is for elitism. Keep the best of the previous generation.

    # Use two Solutions and create two Solutions. So, iteration size will be half of the population size!
    for a in range(0, int(len(previous_generation)/2)):
        parent_1 = selection(previous_generation)
        parent_2 = selection(previous_generation)

        child_1, child_2 = crossover(parent_1, parent_2)  # This will create node lists, we need Solution objects
        child_1 = sl.Solution(child_1)
        child_2 = sl.Solution(child_2)

        if random.random() < mutation_rate:
            mutated = mutation(child_1.Solution)
            child_1 = sl.Solution(mutated)

        new_generation.append(child_1)
        new_generation.append(child_2)

    return new_generation
