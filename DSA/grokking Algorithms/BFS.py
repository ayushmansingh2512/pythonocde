from collections import deque

# Define the graph
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

# Function to check if a person is a mango seller
def person_is_seller(name):
    return name[-1] == 'm'  # Let's say someone is a mango seller if their name ends with 'm'

# Breadth-first search
def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []  # Keep track of searched people to avoid infinite loops

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(f"{person} is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

# Run the search
search("you")
