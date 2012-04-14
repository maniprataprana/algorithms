#bfs print the shortest path

from collections import deque

def bfs_shortestPath(E, source, destination) :
	V = {}	
	Q = [source]
	path = []
	while Q :
		u = Q.pop(0)
		if u not in path :
			path = path + [u]
			if source == u :
				V[u] = '-'	
			for e in E[u] :
				if not V.has_key(e) :
					V[e] = u
			Q = Q + E[u]
	shortest_path = [destination]	
	#shortest path route tracing	
	for i in range(0, len(V)) :
		x = V[shortest_path[len(shortest_path)-1]]
		shortest_path.append(x)
		if x == source :
			break
		
	shortest_path.reverse()					
	return shortest_path
	
#input example taken from CLR
E = { 's' : ['r', 'w'],
 	  'r' : ['s', 'v'],
	  'w' : ['s', 't', 'x'],
      't' : ['w', 'x', 'u'],
	  'x' : ['w', 't', 'u', 'y'],
	  'u' : ['t', 'x', 'y'],
	  'y' : ['x', 'u'],
	  'v' : ['r']
}	

 
print bfs_shortestPath(E, 's', 'y')