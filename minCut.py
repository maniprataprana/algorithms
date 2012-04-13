#The file contains the adjacency list representation of a simple undirected graph.
#There are 40 vertices labeled 1 to 40. The first column in the file represents the vertex label,
#and the particular row other entries except the first column tells all the vertices that the vertex is adjacent to.
#So for example, the 6th row looks liks : "6 29 32 37 27 16".
#This just means that the vertex with label 6 is adjacent to (i.e., shares an edge with) the vertices with labels 29, 32, 37, 27 and 16.

#Your task is to code up and run the randomized contraction algorithm for the min cut problem and use it on the above graph to compute the min cut.
#Note that you'll have to figure out an implementation of edge contractions.
#Initially, you might want to do this naively, creating a new graph from the old every time there's an edge contraction.
# please make sure to run the algorithm many times with different random seeds, and remember the smallest cut that you ever find
#Output -  numeric answer. e.g., if your answer is 5, prints 5

#this is a graph min-cut problem
#implementation of Kargers algorithm
#probabilty of success is order 1 by sqr n
#by Monte Carlo sampling, repeating this experiment over again gets the min value

from sys import argv
import random
import copy

#select a random edge from adjacency list given as hash map
def randomEdge(graph_map) :
	vertex1 = graph_map.keys()[random.randint(0, len(graph_map)-1)]
	vertex2 = graph_map[vertex1][random.randint(0, len(graph_map[vertex1])-1)]
	return vertex1, vertex2

#min cut algorithm based on Krager's algorithm
def min_cut(graph_map):
	
	while len(graph_map) > 2 :
		vertex1, vertex2 = randomEdge(graph_map)
		
		#add list of vertex2 to vertex1
		graph_map[vertex1].extend(graph_map[vertex2])
		
		temp = []
		#remove vertex2 entry from hash map
		for entry in graph_map[vertex2] :
			temp = graph_map[entry]
			
			for i in range(0, len(temp)) :
				if temp[i] == vertex2 :
					temp[i] = vertex1
			graph_map[entry] = 	temp	
		
		#remove self loops
		while vertex1 in graph_map[vertex1] :
			graph_map[vertex1].remove(vertex1)
			
		#delete entry for second vertex	from hash map
		del graph_map[vertex2]
	#checks commented	
	#if len(graph_map[graph_map.keys()[1]]) < 5 :
	#	print graph_map[graph_map.keys()[0]]
	return len(graph_map[graph_map.keys()[1]])
		
# read from file		
script, filename = argv
graph_map = { }
for line in open(filename,'r').readlines():	
	inputstr = []
	inputstr = line.split()
	x = inputstr.pop(0)
	graph_map[x] = inputstr

#print graph_map

#min cut print
minimum_cut_value =  min_cut(copy.deepcopy(graph_map)) 
#looping for sample
for i in range(1, 100) : 	
	x = min_cut(copy.deepcopy(graph_map))	
	if x < minimum_cut_value :
		minimum_cut_value = x
		
print minimum_cut_value
#print len(graph_map)