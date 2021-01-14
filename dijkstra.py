#!/usr/bin/env python

# this version of python code for Dijkstra's Algorithm returns the minimum dustance of all nodes from source node

import sys

class Graph:

	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for col in range(vertices)]for row in range(vertices)]
		
	def print_result(self, dist, src):
		for v in range(self.V):
			print('Distance of Node {0} from source node {1} is - {2}').format(v, src, dist[v])
		
	def minDistance(self, dist, visitedNodes):
		minimum = sys.maxsize
		for v in range(self.V):
			if dist[v] < minimum and visitedNodes[v] == False:
				minimum= dist[v]
				min_value_node = v
		return min_value_node
		
	def dijkstra(self, src):
		# initialise dist for distance of all nodes from source node, every distance is max ( infinite ), except for source node
		dist = [sys.maxsize]*self.V
		dist[src] = 0
		visitedNodes = [False]*self.V
		
		for node in range(self.V):
		
			# find the node with min distance from source and not visited yet
			# it will always start from source note as it has distance 0 initialised in dist
			u = self.minDistance(dist, visitedNodes)
			
			# mark the received node visited
			visitedNodes[u] = True
			
			# we have the minimum distance node from source, check every element in this row and update distance of other elements attached with this node if less distance is found
			for v in range(self.V):
				if self.graph[u][v] > 0 and dist[v] > self.graph[u][v] + dist[u] and visitedNodes[v] == False:
					# update distance of a node if smaller than current is found
					dist[v] = self.graph[u][v] + dist[u]
			
		self.print_result(dist, src)
			
			

g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
		[4, 0, 8, 0, 0, 0, 0, 11, 0], 
		[0, 8, 0, 7, 0, 4, 0, 0, 2], 
		[0, 0, 7, 0, 9, 14, 0, 0, 0], 
		[0, 0, 0, 9, 0, 10, 0, 0, 0], 
		[0, 0, 4, 14, 10, 0, 2, 0, 0], 
		[0, 0, 0, 0, 0, 2, 0, 1, 6], 
		[8, 11, 0, 0, 0, 0, 1, 0, 7], 
		[0, 0, 2, 0, 0, 0, 6, 7, 0] 
		]; 

g.dijkstra(0);
