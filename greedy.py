routes=   [["oradea"         , "zerind"         , 71],
           ["oradea"         , "sibiu"          , 151],
           ["zerind"         , "arad"           , 75],
           ["arad"           , "sibiu"          , 140],
           ["arad"           , "timisoara"      , 118],
           ["timisoara"      , "lugoj"          , 111],
           ["lugoj"          , "mehadia"        , 70],
           ["mehadia"        , "drobeta"        , 75],
           ["drobeta"        , "craiova"        , 120],
           ["craiova"        , "pitesti"        , 138],
           ["craiova"        , "rimnicu vilcea" , 146],
           ["sibiu"          , "rimnicu vilcea" , 80],
           ["rimnicu vilcea" , "pitesti"        , 97],
           ["sibiu"          , "fagaras"        , 99],
           ["fagaras"        , "bucharest"      , 211],
           ["pitesti"        , "bucharest"      , 101],
           ["bucharest"      , "giurgiu"        , 90],
           ["bucharest"      , "urziceni"       , 85],
           ["urziceni"       , "hirsova"        , 98],
           ["hirsova"        , "eforie"         , 86],
           ["urziceni"       , "vaslui"         , 142],
           ["vaslui"         , "iasi"           , 92],
           ["iasi"           , "neamt"          , 87]]

# Below given are heuristic costs for reaching bucharest from different cities

heuristicCosts = {
     "arad": 366,
     "bucharest": 0,
     "craiova": 160,
     "drobeta": 242,
     "eforie": 161,
     "fagaras": 178,
     "giurgiu": 77,
     "hirsova": 151,
     "iasi": 226,
     "lugoj": 244,
     "mehadia": 241,
     "neamt": 234,
     "oradea": 380,
     "pitesti": 98,
     "rimnicu vilcea": 193,
     "sibiu": 253,
     "timisoara": 329,
     "urziceni": 80,
     "vaslui": 199,
     "zerind": 374
}

def createAdjacencyLists (routes) :
    adjacencyLists = {}
    for i in range (0, len(routes)) :
        src = routes[i][0]
        dest = routes[i][1]
        cost = routes[i][2]
        if src not in adjacencyLists :
            adjacencyLists[src] = []
        adjacencyLists[src].append((dest, cost))
        if dest not in adjacencyLists :
            adjacencyLists[dest] = []
        adjacencyLists[dest].append((src, cost))
    return adjacencyLists

def greedy (src, dest, adjacencyLists) :
    try :
        import Queue as Q
    except ImportError :
        import queue as Q
    q = Q.PriorityQueue()
    goalPath = []
    goalPath.append(src)
    q.put((heuristicCosts[src], goalPath))
    goalReached = False
    while goalReached != True and not q.empty() :
        frontTuple = q.get()
        hcost = frontTuple[0]
        path = frontTuple[1]
        if path[len(path) - 1] == dest :
            goalReached = True
            return frontTuple
        else :
            endNode = path[len(path) - 1]
            adjacentNodes = adjacencyLists[endNode]
            for j in range(0, len(adjacentNodes)) :
                newPath = []
                for k in range(0, len(path)) :
                    newPath.append(path[k])
                newPath.append(adjacentNodes[j][0])
                newhcost = heuristicCosts[adjacentNodes[j][0]]
                q.put((newhcost, newPath))

def main () :
    adjacencyLists = createAdjacencyLists(routes)
    src = "arad"
    dest = "bucharest"
    minimumCostPath = greedy(src, dest, adjacencyLists)
    print("The path found using greedy informed search is : ")
    for i in range(0, len(minimumCostPath[1])) :
        print(minimumCostPath[1][i], end = ' ')
    print()

main()
