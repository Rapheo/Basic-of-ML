import numpy as np
from math import factorial
import copy

def finding_pair(n,r):
    return int(factorial(n)/((factorial(n-r))*factorial(r)))

def finding_probabily_fitness(fitness):
    probability_fitness = copy.deepcopy(fitness)
    for f in range(len(fitness)):
        probability_fitness[f] = round((fitness[f]/sum(fitness))*100)
    return probability_fitness    

def selection_parent(population, fitness):
    population = population.tolist()
    parent = []
    probability_fitness = finding_probabily_fitness(fitness)
    probability_fitness = np.unique(np.array(probability_fitness)).tolist()
    probability_fitness = sorted(zip(probability_fitness, population), reverse=True)[:3]
    probability_fitness = [i[1] for i in probability_fitness]
    for i in range(len(population)):
        random_index = np.random.randint(0, len(probability_fitness))
        parent.append(probability_fitness[random_index])
    return parent   

def crossover(parent):
    child = copy.deepcopy(parent)
    for i in range(0,len(parent),2):
        for j in range(3):
            child[i]
            child[i][j] = parent[i+1][j]
            child[i+1][j] = parent[i][j]
        for j in range(3,len(parent[i])-1):
            child[i][j] = parent[i+1][j]
            child[i+1][j] = parent[i][j]   
    return child

def mutation(child, mutation_threshold):
    for i in range(len(child)):
        if(np.random.uniform(0,1) < mutation_threshold):         
            random_index = np.random.randint(0, len(child)-2)
            random_value = np.random.randint(0, 7)
            child[i][random_index] = random_value
    return child        
    

def cal_fitness(population, max_nap):
    population_list = copy.deepcopy(population)
    population_list = population_list.tolist()
    fitness = [0]*len(population_list)

    for i in range(len(population_list)):
        done = []
        #horizontal pairs
        for j in population_list[i]:
            count = population_list[i].count(j)
            if(j not in done and count > 1):
                fitness[i] += finding_pair(count, 2)
                done.append(j)
        #diagonal pairs
        #top left and top right
        count_top_left = 0   #\
        count_top_right = 0  #/
        for j in range(len(population_list[i])):
            if(j > 0):
                reverse_top_left = j #index value for matrix
                for k in range(population_list[i][j]+1,len(population_list[i])): #the value of index for matrix
                    if(reverse_top_left >= 0):
                        reverse_top_left -= 1
                        if(population_list[i][reverse_top_left] == k):
                            count_top_left += 1
                    else:
                        break
            # top right
            if(j < 7):
                reverse_top_right = j #index value for matrix
                for k in range(population_list[i][j]+1,len(population_list[i])): #the value of index for matrix
                    reverse_top_right += 1
                    if(reverse_top_right <= (len(population_list[i])-1)):
                        if(population_list[i][reverse_top_right] == k):
                            count_top_right += 1
                    else:
                        break        


        total_count = count_top_left+count_top_right
        fitness[i] += total_count
    for f in range(len(fitness)):
        fitness[f] = (max_nap - fitness[f])
    return fitness           




def genetic_algo(population, total_queens, mutation_threshold = 0.3):
    max_loop = 10000
    loop = max_loop
    max_nap = finding_pair(total_queens,2)
    while loop > 0:
        fitness = []
        fitness = cal_fitness(population, max_nap)
        parent = selection_parent(population, fitness)
        child = crossover(parent)
        child = mutation(child, mutation_threshold)
        child = np.array(child)
        fitness = cal_fitness(child , max_nap)
        child = child.tolist()
        if(max_nap in fitness):
            print("....done")
            print("result ",child[fitness.index[max_nap]]," found in ", max_loop - loop , "generations")
        population = child
        population = np.array(population)
        loop -= 1
    print("no solution found in ",max_loop,"generation, please try again.")


##### driver code
total_queens = 8

start_population = 10

mutation_threshold = 0.3

population = np.random.randint(0,total_queens,(start_population,total_queens))


genetic_algo(population, total_queens, mutation_threshold)
