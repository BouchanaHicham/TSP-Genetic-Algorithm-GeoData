import math


class Node:  # Node = Location = Point
    def __init__(self, id, x, y):
        self.x = float(x)
        self.y = float(y)
        self.id = int(id)


# 1 Open a file and create a data list using the info in the file
file_name = "data_set"  # write path if the file is not in the same directory
dataset = []


with open(file_name, "r") as f:
    for line in f:  # check each line
        new_line = line.strip()  # remove spaces at the beginning and the end if they are available
        new_line = new_line.split(" ")  # split a string into a list
        id, y, x = new_line[0], new_line[1], new_line[2]  # check dataset file to see why id,y,x = 0,1,2
        dataset.append(Node(id=id, x=x, y=y))  # Create a Node object with id, x, y and add to the data list

N = 58  # Total number of Cities


# This function will be run once at the beginning of the program to create a distance matrix
def create_distance_matrix(node_list):
    matrix = [[0 for _ in range(N)] for _ in range(N)]
    # classical matrix creation with two for loops
    for i in range(0, len(matrix)-1):
        for j in range(0, len(matrix[0])-1):
            # calculate euclidean distance between each points and add to the matrix
            # a^2 = b^2 + c^2
            # in other words distance =sqrt[ (Xa - Xb)^2 + (Ya - Yb)^2 ]
            matrix[node_list[i].id][node_list[j].id] = math.sqrt(pow((node_list[i].x - node_list[j].x), 2) + pow((node_list[i].y - node_list[j].y), 2))
           
    print(matrix)
    return matrix
    

matrix = create_distance_matrix(dataset)  # calculate all distances among all points and create a matrix




class Solution:
    def __init__(self, node_list):
        self.Solution = node_list

        slt_representation = []           #the list in numbers ( later on cities )
        for i in range(0, len(node_list)):
            slt_representation.append(self.Solution[i].id)
        self.slt_representation = slt_representation

        #calc the total distance is this possible solution
        distance = 0
        for j in range(1, len(self.slt_representation) - 1):  # get distances from the matrix
            distance += matrix[self.slt_representation[j]-1][self.slt_representation[j + 1]-1]
        self.cost = distance

        self.fitness_value = 1 / self.cost






