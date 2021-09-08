import numpy as np

def gen(limit):
    location = []

    for i in range(limit):
        (x,y) = ((round(np.random.uniform(0,1),2)),(round(np.random.uniform(0,1),2)))
        if((x,y) not in location):
            location.append((x,y))

    return location

print(gen(10))