# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]

def find_eulerian_tour(graph):
    # your code here
    tour = []
    g = {}
    for (x,y) in graph :
    	if x not in g :
    		g[x] = [y]
    	else :
    		g[x].append(y)

    	if y not in g :
    		g[y] = [x]
    	else :
    		g[y].append(x)	
    
    stack = [g.keys()[0]]
    while stack :
    	v = stack[-1]
    	if g[v] :
    		u = g[v][0]
    		stack.append(u)
    		del g[u][g[u].index(v)]
    		del g[v][0]
    	else :
	    	tour.append(stack.pop())	
    return tour


print find_eulerian_tour([(0, 1), (1, 5), (1, 7), (4, 5), (4, 8), (1, 6), (3, 7), (5, 9), (2, 4), (0, 4), (2, 5), (3, 6), (8, 9)])
