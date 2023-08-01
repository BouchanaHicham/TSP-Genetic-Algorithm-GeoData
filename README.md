# TSP-Genetic-Algorithm-GeoData  🌐 

This Python project presents an efficient solution to the Traveling Salesman Problem (TSP) using a Genetic Algorithm approach and real-life geographical data (longitude and latitude) for cities or locations.

## Problem Description

The Traveling Salesman Problem involves finding the shortest route for a salesman to visit a set of cities exactly once and return to the starting city, while minimizing the total distance traveled. The project utilizes Genetic Algorithm techniques, inspired by natural selection, to evolve generations of potential solutions and optimize the path taken by the traveling salesman.

## Functions
### GeneticAlgorithm.py
- `create_random_list(n_list)`: Creates a random solution (path) by shuffling the node list representing cities and adding the start and end points.
- `initialization(data, pop_size)`: Initializes the population with random solutions, creating a list of solutions with random paths.
- `selection(population)`: Performs tournament selection to choose the winner (solution) from a random subset of the population based on their fitness values (lower cost).
- `crossover(p_1, p_2)`: Performs one-point crossover between two parent solutions to create two child solutions with swapped subtours.
- `mutation(Solution)`: Performs a mutation operation by swapping two random nodes in the solution to introduce diversity.
- `find_best(generation)`: Finds and returns the best solution (lowest cost) from a given generation.
- `create_new_generation(previous_generation, mutation_rate)`: Creates a new generation of solutions based on the previous generation using elitism, crossover, and mutation operators.
  
### Solution.py

- `create_distance_matrix(node_list)`: Calculates the Euclidean distance between each pair of cities and creates a distance matrix for later use in the Genetic Algorithm.
- `Solution(node_list)`: Initializes a Solution object with a list of nodes representing a possible path. Calculates the total distance (cost) of the path and the fitness value based on the cost.

### Main.py
- `genetic_algorithm(num_of_generations, pop_size, mutation_rate, data_list)`: Implements the Genetic Algorithm to optimize the Traveling Salesman Problem (TSP). It initializes the population with random solutions and iteratively creates new generations using selection, crossover, and mutation operations. Returns the final generation and a list of costs over generations for plotting.
## Usage

1. Place the geographical data (longitude and latitude) for cities in the "data_set" file.
2. Run the main code "main.py" to execute the Genetic Algorithm and find the optimized path.
3. View the cost-generation graph and the best path visualization.

## Data

The "data_set" file should contain city information with each line in the format: `id longitude latitude`. Replace this data with your specific city data.

### Data Source
The geographical data (longitude and latitude) for the Algerian cities can be obtained from the following website:
[https://simplemaps.com/data/dz-cities](https://simplemaps.com/data/dz-cities)

### Default Set (Algeria with Algerian cities)

The default dataset corresponds to Algeria with algerian Cities.
`Number_Of_Cities` is set to `58`

## Results

The project provides visualizations of the cost-generation graph and the best path taken by the traveling salesman on a 2D plane. The optimized path ensures efficient coverage of cities and a minimized total distance.

## Example Images

![Plot Result - Algeria](example_images/plot_result_algeria.png)
![Cost per Generation](example_images/cost_per_generation.png)

## Contributing

Contributions to this project are welcome! If you find any issues or have improvements, feel free to create a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

The project's implementation utilizes Genetic Algorithms, a powerful optimization technique inspired by natural evolution. The script uses the Python random module for random operations.

## Author

**Bouchana Hicham**
