import random
import numpy

def graf_gen(graf, size):
    for i in range(size):
        for j in range(size):
            rand = random.randint(0,5)

            if(i == j):
                graf[i][j] = -1
            elif(rand <= 1):
                graf[i][j] = j
            else:
                graf[i][j] = -1

    return graf