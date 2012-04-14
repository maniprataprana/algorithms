#dfs implementation
#0 univistied
#1 visited
#2 explored

color = {}
parent = {}
s_time = {}
e_time = {}

def dfs(G) :
	for node in G.keys() :
		color[node] = 0
		parent[node] = '-'
	global time_value
	time_value = 0
	for node in G.keys() :
		if color[node] == 0 :
			dfs_visit(G,node)	
	
def dfs_visit(G,node):
	global time_value
	time_value = time_value + 1
	s_time[node] = time_value
	color[node] = 1
	
	for e in G[node] :
		if color[e] == 0 :
			parent[e] = node
			dfs_visit(G,e)
	color[node] = 2
	time_value = time_value + 1
	e_time[node] = time_value		
	
	



#input example taken from CLR

G = { 'u' : ['v', 'x'],
	  'v' : ['y'],
  	  'x' : ['v'],
      'w' : ['y', 'z'],
	  'z' : ['z'],
	  'y' : ['x'],	  
}

dfs(G)
print e_time,s_time