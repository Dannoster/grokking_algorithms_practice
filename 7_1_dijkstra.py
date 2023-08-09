graph = {}
graph["start"] = {"a" : 5, "c" : 2}
graph["a"] = {"b" : 4, "d" : 2}
graph["c"] = {"a" : 8, "d" : 7}
graph["b"] = {"fin" : 3, "d" : 6}
graph["d"] = {"fin" : 1}
graph["fin"] = {}

costs = {"start" : 0}
parents = {"start" : None}
for key in graph:
    if key != "start":
        costs[key] = float("inf")
        parents[key] = None


checked = []

def find_min_node():
    global checked
    min_node = None
    min_node_cost = float("inf")
    for node in graph:
        if node not in checked and costs[node] < min_node_cost:
            min_node = node
            min_node_cost = costs[node]
    checked.append(min_node)
    return min_node

def find_min_path():
    while len(checked) != len(graph):
        min_node = find_min_node()
        for node in graph[min_node]:
            if costs[node] > costs[min_node] + graph[min_node][node]:
                costs[node] = costs[min_node] + graph[min_node][node]
                parents[node] = min_node
    curr_kid = "fin"
    path = str()
    while curr_kid != "start":
        path = curr_kid + " " + path
        curr_kid = parents[curr_kid]
    path = "start" + " " + path
    return path + "\nThe lenth is " + str(costs["fin"])

print(find_min_path())
