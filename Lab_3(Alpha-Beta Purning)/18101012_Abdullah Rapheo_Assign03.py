import sys
import random


turn = int(input("Please Enter number of turns for Riyad: "))
depth = (turn * 2)  # equal change for both so 2*

branch = int(input("Please Enter Number of notes: "))
min_leaf_value = int(
    input("Please Enter Minimum value for the range of notes: "))
max_leaf_value = int(
    input("Please Enter Maximum value for the range of notes: "))

leaf_nodes = branch ** depth   #b^d

MIN = -sys.maxsize - 1
MAX = sys.maxsize

def gen_tree():
    tree = []
    for i in range(leaf_nodes):
        node = random.randint(min_leaf_value, max_leaf_value)
        tree.append(node)
    return tree


def minimax(position, depth, maximizingPlayer, tree, count):

    if (depth == 0):
        count.append(tree[position])
        return(tree[position])

    if maximizingPlayer:
        max_eval = MIN
        for child in range(branch):
            eval = minimax(position*branch+child, depth-1, False, tree, count)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = MAX
        for child in range(branch):
            eval = minimax(position*branch+child, depth-1, True, tree, count)
            min_eval = min(min_eval, eval)
        return min_eval    

            
def alpha_beta_puning(position, depth, alpha, beta, maximizingPlayer, tree, count):
    if (depth == 0):
        count.append(tree[position])
        return(tree[position])

    if maximizingPlayer:
        max_eval = MIN
        for child in range(branch):
            eval = alpha_beta_puning(position*branch+child, depth-1, alpha, beta, False, tree, count)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if(beta <= alpha):
                break
        return max_eval
    else:
        min_eval = MAX
        for child in range(branch):
            eval = alpha_beta_puning(position*branch+child, depth-1, alpha, beta, True, tree, count)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if(beta <= alpha):
                break
        return min_eval 

tree = gen_tree()  #generating the leaf node values

count = [] #getting the top value and total count
print("Depth:",depth)
print("Branch:",branch)
print("Terminal States (Leaf Nodes):",leaf_nodes)
print ("Maximum amount: ", minimax(0, depth, True, tree, count))
print("Comparisons:",len(count)) # before prning
count = []
alpha_beta_puning(0, depth, MIN, MAX, True, tree, count)
print("Comperasions:", len(count)) # after puning