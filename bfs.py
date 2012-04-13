#bfs implementation 
#discovers every vertex that is reachable from source s
# returns path of bfs from source to every other node
#iterative approach

from collections import deque

def bfs(G,source) :	
	Q = [source]
	path = []
	while Q :
		u = Q.pop(0)
		if u not in path :
			path = path + [u]
			Q = Q + G[u]			
	return path
	
#input example taken from CLR
G = { 's' : ['r', 'w'],
 	  'r' : ['s', 'v'],
	  'w' : ['s', 't', 'x'],
      't' : ['w', 'x', 'u'],
	  'x' : ['w', 't', 'u', 'y'],
	  'u' : ['t', 'x', 'y'],
	  'y' : ['x', 'u'],
	  'v' : ['r']
}	

e = 'v' 
print bfs(G,e)