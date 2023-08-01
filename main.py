import GeneticAlgorithm as GA
import Solution as Ch

# following libraries for graphs
import numpy as np
import matplotlib.pyplot as plt


# parameters
numbers_of_generations = 200  
population_size = 100  
mut_rate = 0.2  
dataset = Ch.dataset  


def genetic_algorithm(num_of_generations, pop_size, mutation_rate, data_list):
    new_gen = GA.initialization(data_list, pop_size)  # first generation is created with initialization function

    costs_for_plot = []  # this list is only for Cost-Generations graph. it will constitute y-axis of the graph

    for iteration in range(0, num_of_generations):
        new_gen = GA.create_new_generation(new_gen, mutation_rate)  # create a new generation in each iteration

        costs_for_plot.append(GA.find_best(new_gen).cost)  # append the best Solution's cost of each new generation to the list to plot in the graph
        best_solution = GA.find_best(new_gen)
        print(f"                                      Generation {iteration}:")
        print(f"Best route = {[node.id for node in best_solution.Solution]}")
        print(f"Cost:[{best_solution.cost}]")
    return new_gen, costs_for_plot

# --------------------------------------------------------------- [ Plot ] ---------------------------------------------------------------
def draw_cost_generation(y_list):
    x_list = np.arange(1, len(y_list)+1)  # create a numpy list from 1 to the numbers of generations

    plt.plot(x_list, y_list)

    plt.title("Cost / Gen")
    plt.xlabel("Generations")
    plt.ylabel("Cost")

    plt.show()


def draw_path(solution):
    x_list = []
    y_list = []

    for m in range(0, len(solution.Solution)):
        x_list.append(solution.Solution[m].x)
        y_list.append(solution.Solution[m].y)

    fig, ax = plt.subplots()
    plt.scatter(x_list, y_list)  # alpha=0.5

    ax.plot(x_list, y_list, '--', lw=0.1, color='black', ms=10)
    ax.set_xlim(-10, 12)
    ax.set_ylim(15, 40)

    plt.show()


# --------------------------------------------------- Init ---------------------------------------------------
last_generation, y_axis = genetic_algorithm(numbers_of_generations, population_size, mut_rate, dataset)

best_solution = GA.find_best(last_generation)


draw_cost_generation(y_axis)
draw_path(best_solution)

# ------------------------------------------------------------------------------------------------------------


cities = ["Algiers", "Oran", "Constantine", "Blida", "Batna", "Sétif", "Djelfa", "Annaba", "Sidi Bel Abbès", "Biskra",
"Tébessa", "Tiaret", "Bejaïa", "Tlemcen", "Bordj Bou Arreridj", "Béchar", "Skikda", "Souk Ahras", "Chlef",
"M’Sila", "Mostaganem", "Médéa", "Tizi Ouzou", "El Oued", "Laghouat", "Ouargla", "Jijel", "Relizane", "Saïda",
"Guelma", "Ghardaïa", "Mascara", "Khenchela", "Oum el Bouaghi", "El Bayadh", "Tamanrasset", "Aïn Temouchent",
"Tissemsilt", "Bouira", "Adrar", "Tindouf", "Boumerdes", "El Golea", "Touggourt", "Timimoun", "I-n-Salah",
"El Tarf", "Tipasa", "Illizi", "Bordj Mokhtar", "Naama", "Djanet", "Beni Abbès", "In Guezzam", "Aïn Defla",
"Mila", "Ouled Djellal", "El Meghaïer"]

city_array = [node.id for node in best_solution.Solution]

Shortest_city_path_list = []
#this means that each index (id) in our training_data_set corresponds to the city we have in our array
Number_Of_Cities = 58 #Set the number of cities corresponding to the country (Algeria Has 58 Cities as of 2023)
for i in range(Number_Of_Cities):
    #since our data_set id starts with 1 and our cities start with an index of 0 , we substract 1 from the index of cities to be synced
    Shortest_city_path_list.append(cities[city_array[i]-1])
    #print(Shortest_city_path_list)   #Our Best Path in our country

#this script just fixes the city placement   so it starts with our picked start city
Start_City = "Biskra"
start_city_index = Shortest_city_path_list.index(Start_City)

print(Shortest_city_path_list[start_city_index:] + Shortest_city_path_list[:start_city_index])













