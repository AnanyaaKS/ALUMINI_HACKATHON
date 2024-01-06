import json
from sys import maxsize
from itertools import permutations
V= 21

def nearest_neighbor_algorithm_with_weight_limit(distance_matrix, weight_limit):
    num_cities = len(distance_matrix)
    visited = [False] * num_cities
    # Start from the first city
    current_city = 0
    visited[current_city] = True
    # List to store the order of visited cities
    tour = [current_city]
    current_weight = 0
    # Repeat until all cities are visited or weight limit is exceeded
    while len(tour) < num_cities and current_weight <= weight_limit:
        next_city = None
        min_distance = float('inf')
        # Find the nearest unvisited city that does not exceed the weight limit
        for city in range(num_cities):
            if not visited[city] and distance_matrix[current_city][city] < weight_limit - current_weight:
                next_city = city
                min_distance = distance_matrix[current_city][city]
        # Visit the nearest city
        if next_city is not None:
            current_city = next_city
            visited[current_city] = True
            tour.append(current_city)
            current_weight += distance_matrix[current_city][tour[-2]]
        else:
            break
    return tour


f = open('Input data\\level0.json')
data = json.load(f)
#print(data)
numNeighbourhoods = data['n_neighbourhoods']
numRestaurants=data['n_restaurants']
nbrhds=data['neighbourhoods']
restaurants=data['restaurants']
vehicles=data['vehicles']
max=vehicles['v0']['capacity']


nghNum=list(nbrhds.keys())
#print(nghNum)
nghDist=[]

r0=restaurants['r0']['neighbourhood_distance']
r0.insert(0,0)
#print(r0)
j=1
ordr=[]
nghDist.append(r0)
for i in nghNum:
    temp = nbrhds[i]['distances']
    temp1=nbrhds[i]['order_quantity']
    ordr.append(temp1)
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
mincost=nearest_neighbor_algorithm_with_weight_limit(nghDist,600)
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

with open('C:\\Alumini_Hackathon_ans\\levela_output.json', 'w') as fp:
    fp.write(json.dumps(vehicles1))


