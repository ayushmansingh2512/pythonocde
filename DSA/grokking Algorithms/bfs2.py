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

#lets maek sure name is there
def person_is_seller(name):
	return name[-1] == "y"

#bfs start now 
def search(name):
	search_queue = deque()
	search_queue += graph[name]
	searched = []

	while search_queue:
		person = search_queue.popleft()
		if person not in searched:
			if person_is_seller(person):
				print(f"{person} person is mango seller")
				return True
			else:
				search_queue += graph[person]
				searched.append(person)
	return False

search("you")



