from collections import deque

def person_is_seller(name):
      return name[-1] == 'm'

graph = {}
# added path dict
path = {"you" : ["you"]}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def search(name):

    search_queue = deque()
    new_names = graph[name]
    search_queue += new_names
    # getting path for newcomers
    for new_name in new_names:
        path[new_name] = path[name] + [new_name]
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                # printing path
                print(f"The path was: {' -> '.join(path[person])}")
                return True
            else:
                new_names = graph[person]
                search_queue += new_names
                # getting path for newcomers
                for new_name in new_names:
                    path[new_name] = path[person] + [new_name]
                searched.append(person)

    return False

search("you")
