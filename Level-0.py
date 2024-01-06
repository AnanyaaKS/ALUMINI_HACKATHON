import json
from sys import maxsize
from itertools import permutations
V= 21
'''
def tsp(graph,s):
    vertex=[]
    for i in nodes:
        if i!= s:
            vertex.append(i)
    min_path = maxsize 
    next_permutation=permutations(vertex)
    for i in next_permutation: 
        #store current Path weight(cost) 
        current_pathweight = 0
 
        # compute current path weight 
        k = nodes.index(s) 
        for j in i: 
            j1=i.index(j)
            current_pathweight += graph[k][j1] 
            k = j1
        current_pathweight += graph[k][nodes.index(s)] 
 
        # update minimum 
        min_path = min(min_path, current_pathweight) 
         
    return min_path 
'''    
def nearest_neighbor_algorithm(distance_matrix):
    num_cities = len(distance_matrix)
    visited = [False] * num_cities

    # Start from the first city
    current_city = 0
    visited[current_city] = True

    # List to store the order of visited cities
    tour = [current_city]

    # Repeat until all cities are visited
    while len(tour) < num_cities:
        next_city = None
        min_distance = float('inf')

        # Find the nearest unvisited city
        for city in range(num_cities):
            if not visited[city] and distance_matrix[current_city][city] < min_distance:
                next_city = city
                min_distance = distance_matrix[current_city][city]

        # Visit the nearest city
        current_city = next_city
        visited[current_city] = True
        tour.append(current_city)

    return tour

f = open('Input data\\level0.json')
data = json.load(f)
#print(data)
numNeighbourhoods = data['n_neighbourhoods']
numRestaurants=data['n_restaurants']
nbrhds=data['neighbourhoods']
restaurants=data['restaurants']
vehicles=data['vehicles']


nghNum=list(nbrhds.keys())
#print(nghNum)
nghDist=[]

r0=restaurants['r0']['neighbourhood_distance']
r0.insert(0,0)
#print(r0)
j=1
nghDist.append(r0)
for i in nghNum:
    temp = nbrhds[i]['distances']
    temp.insert(0,r0[j])
    nghDist.append(temp)
    j+=1


# the no of vertices 

nodes=nghNum
nodes.insert(0,vehicles['v0']['start_point'])
#nodes
#print(nodes)
# The list of distances for graph
#print(nghDist)
start_node=vehicles['v0']['start_point']
#print(len(nghDist))
mincost=nearest_neighbor_algorithm(nghDist)
mincost.append(0)
#print(nodes)
#print('Tour')
path=[]
for i in mincost:
    path.append(nodes[i])
#print(path)
vehicles1={}
vehicles1['v0']={}
vehicles1['v0']['path']=path

print(vehicles1)

with open('C:\\Alumini_Hackathon_ans\\level0_output.json', 'w') as fp:
    fp.write(json.dumps(vehicles1))


