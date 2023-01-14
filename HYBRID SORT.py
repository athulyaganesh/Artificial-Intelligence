# ARTIFICIAL INTELLIGENCE 
#HOMEWORK 2 
#AUTHORS: ROBERT SCHAD, HANEESHA DUSHARA, NISHANTH CHIDAMBARAM, ATHULYA GANESH 
import time 

map = {} #initializing maps that give us the cost. 
map['ORADEA'] = {}
map['ZERIND'] = {}
map['ARAD'] = {}
map['TIMISOARA'] = {}
map['LUGOJ'] = {}
map['MEHADIA'] = {}
map['DROBETA'] = {}
map['CRAIOVA'] = {}
map['RIMNICU_VILCEA'] = {}
map['SIBIU'] = {}
map['FAGARAS'] = {}
map['PITESTI'] = {}
map['BUCHAREST'] = {}
map['GIURGIU'] = {}
map['URZICENI'] = {}
map['VASLUI'] = {}
map['IASI'] = {}
map['NEAMT'] = {}
map['HIRSOVA'] = {}
map['EFORIE'] = {}

map['ORADEA']['ZERIND'] = 71 #the costs to go from each place to the other; given in question 
map['ORADEA']['SIBIU'] = 151
map['ZERIND']['ORADEA'] = 71
map['ZERIND']['ARAD'] = 75
map['ARAD']['ZERIND'] = 75
map['ARAD']['SIBIU'] = 140
map['ARAD']['TIMISOARA'] = 118
map['TIMISOARA']['ARAD'] = 118
map['TIMISOARA']['LUGOJ'] = 111
map['LUGOJ']['TIMISOARA'] = 111
map['LUGOJ']['MEHADIA'] = 70
map['MEHADIA']['LUGOJ'] = 70
map['MEHADIA']['DROBETA'] = 75
map['DROBETA']['MEHADIA'] = 75
map['DROBETA']['CRAIOVA'] = 120
map['CRAIOVA']['RIMNICU_VILCEA'] = 146
map['CRAIOVA']['DROBETA'] = 120
map['CRAIOVA']['PITESTI'] = 138
map['RIMNICU_VILCEA']['SIBIU'] = 80
map['RIMNICU_VILCEA']['PITESTI'] = 97
map['RIMNICU_VILCEA']['CRAIOVA'] = 146
map['SIBIU']['ORADEA'] = 151
map['SIBIU']['ARAD'] = 140
map['SIBIU']['FAGARAS'] = 99
map['SIBIU']['RIMNICU_VILCEA'] = 80
map['FAGARAS']['SIBIU'] = 99
map['FAGARAS']['BUCHAREST'] = 211
map['PITESTI']['RIMNICU_VILCEA'] = 87
map['PITESTI']['CRAIOVA'] = 138
map['PITESTI']['BUCHAREST'] = 101
map['BUCHAREST']['PITESTI'] = 101
map['BUCHAREST']['FAGARAS'] = 211
map['BUCHAREST']['GIURGIU'] = 90
map['BUCHAREST']['URZICENI'] = 85
map['GIURGIU']['BUCHAREST'] = 90
map['URZICENI']['BUCHAREST'] = 85
map['URZICENI']['VASLUI'] = 142
map['URZICENI']['HIRSOVA'] = 98
map['VASLUI']['IASI'] = 92
map['VASLUI']['URZICENI'] = 142
map['IASI']['NEAMT'] = 87
map['IASI']['VASLUI'] = 92
map['NEAMT']['IASI'] = 87
map['HIRSOVA']['URZICENI'] = 98
map['HIRSOVA']['EFORIE'] = 86
map['EFORIE']['HIRSOVA'] = 86

SLDs = { #shortest paths to bucharest, as given in the question 
'ARAD': 366,
'BUCHAREST': 0,
'CRAIOVA': 160,
'DROBETA': 242,
'EFORIE': 161,
'FAGARAS': 176,
'GIURGIU': 77,
'HIRSOVA': 151,
'IASI': 226,
'LUGOJ': 244,
'MEHADIA': 241, 
'NEAMT': 234, 
'ORADEA': 380, 
'PITESTI': 100, 
'RIMNICU_VILCEA': 193, 
'SIBIU': 253, 
'TIMISOARA': 329, 
'URZICENI': 80, 
'VASLUI': 199, 
'ZERIND': 374
}

def DFS(startCity): #function that the user calls. 
    return dfs_Implementation([], [], 0, startCity)

def dfs_Implementation(visited, queue, currentCost, startCity = ''):
    if queue == [] and visited == []: 
        current = startCity # Base case for recursion 
    else: 
        current = queue[0] #Go to the top element of the queue 
        
    if current  !=  'BUCHAREST': 
        if current not in visited: #if we have not reached the goal (Bucharest), and we have 
            #not yet visited the Current city, check the current city off as visited 
            visited.append(current)
        for neighbor in map[current]:
            if neighbor not in visited: 
                queue.insert(0,neighbor) # Add all its neighbors into the queue (front of the queue). 
                currentCost = currentCost + map[current][neighbor]
                dfs_Implementation(visited, queue, currentCost) #Then call DFS on the city in the top of the     queue. 
        
    else:
        visited.append('BUCHAREST')
        print("PATH: ",visited) #if we reach the goal, print out the map. 
        print("TOTAL COST: ", currentCost) 
    
            
def BFS(startCity): 
 #Breadth-first search: the children of the current node are put in the at the back of the queue.
    return bfs([],[],{},[],startCity) 

def bfs(visited,city_queue,mapping,path,currentCity):
  if currentCity != 'BUCHAREST' and currentCity not in visited: #if we are not at the Goal, or we have not visited the current city, check it off as visited now, and append it to our queue. 
    visited.append(currentCity)
    city_queue.append(currentCity)
  for city in map[currentCity].keys():
    if city not in visited:
      visited.append(city)
      #currentCost += map[currentCity][city] 
      city_queue.append(city)
      mapping[city] = currentCity
      if city == 'BUCHAREST':
        path.append(city)
        while city != startCity:
          tempCity = mapping[city]
          path.insert(0,tempCity)
          city = tempCity
        print("PATH: ",path)
        total_distance = 0
        for i in range(len(path) - 1):
          source = path[i]
          destination = path[i+1]
          total_distance += map[source][destination]
        print('TOTAL COST: ', total_distance)
        return
  currentCity = city_queue.pop(0) #explore all the neighbors, calling BFS on those as well 
  if currentCity != 'BUCHAREST':
    bfs(visited, city_queue, mapping,path, currentCity)
  else: #once Bucharest is reached, print out the path. 
    print(visited)
   
# Best-first search: the queue is maintained in nondecreasing order of the SLD, h(n), of the children of 
# theStarcurrent : city to the goal city.  That is, the children of the current node with smallest h(n) are 
# put in the front of the queue.  Output the path generated and its cost. (obtained by modifying depth-first algorithm.)

# priority_queue: priority=SLD, value=city_name
'''
Best First Search psuedocode:

currentCity = front of queue (AKA top of stack)
if currentCity is not Bucharest:
    for each of currentCity's neighbors:
        if neighbor not in visited:
            add neighbor's SLD to bucharest to neighboringSLDs list
    sort(neighboringSLDs)
    add neighbors to front of queue in decreasing order of SLD
    recurse(visited, queue)

'''
def BEST(startCity):
    return bestFirstSearch([],[startCity])
    
def bestFirstSearch(visited, queue):
    if queue == []: # base case: no path to Bucharest, so return an empty list
        return []
    
    neighborSLDs = []

    # visit city in front of queue
    currentCity = queue.pop(0)
    visited += [currentCity]

    # check if we reached Bucharest
    if currentCity != 'BUCHAREST':
        for neighbor in map[currentCity].keys():
            if neighbor not in visited:
                # get the SLD of each of the neighbors
                neighborSLDs += [SLDs[neighbor]]
        
        neighborSLDs.sort() # sort in ascending order
        sorted_neighbors = []

        # get a list of the city names in ascending order of SLD
        for sld in neighborSLDs:
            sorted_neighbors += [city for city in map[currentCity].keys() if SLDs[city] == sld]
        
        # then add each city to the queue in ascending order of SLD
        queue = sorted_neighbors + queue
        bestFirstSearch(visited, queue)

    else:
        total_distance = 0
        # get the total distance of the path
        for i in range(len(visited) - 1):
            source = visited[i]
            destination = visited[i+1]
            total_distance += map[source][destination]
        
        print('PATH: ', visited)
        print('TOTAL COST: ', total_distance)
        
        return visited

# increasing order of SLD's 
# Current City --> Children Cities(Connected Cities) --> SLD's[City]
# 


# A* search: the queue is maintained in nondecreasing order of the SLD, f(n)=g(n)+h(n), of the children 
# of the current city to the goal city. In this search the algorithm may need to backtrack to a 
# previous node when the value of f(n) is smaller than at the current node. Output the path 
# generated and its cost. (obtained by modifying the breadth first algorithm.)
'''

RAS:
  

A* pseudocode
currentCity = city at the endpoint of path with min f(n)
if currentCity is Bucharest:
  print path and its f(n)
  return
else:
  for each neighbor of currentCity:
      create new path from currentCity's path + neighbor
      compute f(neighbor) 
      initialize new path object
    add all new paths to queue_of_paths
    sort queue_of_paths by f(n)

  pop old path to currentCity from queue_of_paths (since we can only travel to its neighbors)
  sort paths by f(n)s
  recurse 



'''
class Path():
  def __init__(self, cities, distance):
    self.cities = cities
    self.distance = distance # f(n) distance
  
def ASTAR(startCity):
    queue = [Path([startCity], SLDs[startCity])]
    AStarSearch(queue)

def AStarSearch(queue_of_paths):
    new_paths = []
    # expand city at the endpoint of the path at front of queue (AKA path with minimum f(n))
    currentCity = queue_of_paths[0].cities[-1]

    # check if we've reached Bucharest
    if currentCity == 'BUCHAREST':
        print('PATH: ', queue_of_paths[0].cities)
        print('TOTAL COST: ', queue_of_paths[0].distance)
        return

    else:
        # get new paths for each of currentCity's neighbors
        for neighbor in map[currentCity].keys():
            # get list of cities (just the cities to reach currentCity then append neighbor)
            new_city_list = queue_of_paths[0].cities + [neighbor]
            # compute f(neighbor) 
            g_n = queue_of_paths[0].distance - SLDs[currentCity] + map[currentCity][neighbor] # g(n) = f(n-1) - g(n-1) + dist(n-1, n) 
            h_n = SLDs[neighbor]
            new_distance = g_n + h_n # new_distance is f(neighbor)
            
            new_paths += [Path(new_city_list, new_distance)]

        # no longer need path with just the currentCity - since it will be replaced by the paths to its neighbors
        queue_of_paths.pop(0)
        # add new_paths to paths queue
        queue_of_paths += new_paths
        # sort paths queue by f(n)
        queue_of_paths.sort(key=lambda path : path.distance)

        # recurse with our new, sorted, queue of paths
        AStarSearch(queue_of_paths)

#MAIN USER INTERFACE 
startCity = input("Enter start city here in all capitals: ") 

#WE ARE ASSUMING THAT THE USER ENTERS A START CITY THAT IS IN THE KNOWLEDGE BASE, SPELT CORRECTLY, AND IN ALL CAPS. IF THERE IS SOME SORT OF ERROR, THEN THE CODE WILL NOT BE ABLE TO RUN.
print("\nDFS")
start = time.time() 
DFS(startCity) 
end = time.time() 
print("Execution time for DFS: ", end - start, " seconds")
print("\nBFS")
start = time.time() 
BFS(startCity)
end = time.time() 
print("Execution time for BFS: ", end - start, " seconds")
print("\nBest First")
start = time.time() 
BEST(startCity)
end = time.time() 
print("Execution time for Best First: ", end - start, " seconds")
print("\nA star") 
start = time.time() 
ASTAR(startCity)
end = time.time() 
print("Execution time for A*: ", end - start, " seconds")


