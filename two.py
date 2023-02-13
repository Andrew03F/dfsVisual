import random

def initialize(x, y, land_prob):
    matrix= []
    new = []
    for i in range ( x):
        for j in range ( y):
            foo = random.randint(1,100)
            if (foo < land_prob):
                new.append(1)
            else:
                new.append(0)
            
        matrix.append(new)
        new = []
    return matrix

def print_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])
def is_edge(coordx, coordy, m):
    if (coordx == 0 or coordy == 0 or coordx ==(len(m) -1) or coordy == (len(m[0]) - 1)):
        return True
def is_land(coordx, coordy, m):
    if (m[coordy][coordx] == 1):
        return True
    else:
        return False
def is_safe(coordx, coordy, m, s):
    if (is_edge(coordx, coordy,m)):
        return True
    if (s[coordy][coordx] == True):
        return True
def get_nieghbors(coordx, coordy, m, v, s):
    result = []
    if (is_edge(coordx,coordy, m)):
        return result
    else:
        ###
        if (is_land(coordx, coordy +1, m) and not v[coordy + 1][coordx] ):
            result.append((coordx, coordy +1))
            v[coordy + 1][coordx] = True
        ###
        if (is_land(coordx, coordy - 1, m) and not v[coordy - 1][coordx] ):
            result.append((coordx, coordy - 1))
            v[coordy - 1][coordx] = True
        ###
        if (is_land(coordx + 1, coordy, m) and not v[coordy][coordx + 1]  ):
            result.append((coordx + 1, coordy))
            v[coordy][coordx + 1] = True
        ###
        if (is_land(coordx -1, coordy, m)and not v[coordy][coordx -1]  ):
            result.append((coordx - 1, coordy))
            v[coordy][coordx -1] = True
    return result
def is_island(coordx, coordy, m, s):
    if (not is_land(coordx, coordy, m)):
        return False
    if (is_safe(coordx,coordy,m,s)):
        return False
    visited = []
    for i in range(len(m)):
        visited.append(len(m[0]) * [False])
    visited[coordy][coordx] = True
    stack = []
    stack.append((coordx, coordy))
    while (len(stack) > 0):
        top = stack.pop()
        # print(top)
        if (is_safe(top[0], top[1], m,s)):
            # set all visited to safe
            s[top[1]][top[0]] == True
            return False
        top_nieghbors = get_nieghbors(top[0], top[1], m, visited, s)
        for e in top_nieghbors:
            stack.append(e)
    return True

def remove_islands(m):
    safe = []
    for i in range(len(m)):
        safe.append(len(m[0]) * [False])
    for i in range(len(m)):
        print(i)
        for j in range(len(m[0])):
                if (is_island(i,j,m,safe)):
                    m[j][i] = 0
                
                # print("called: " + str(i) + ", " +str(j))
                # print(is_island(i,j,m))
                # print()
    
            
    
