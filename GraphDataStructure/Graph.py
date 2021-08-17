from Vertices import Vertex


class Graph:
	def __init__(self):
		self.vert_dict = {}
		self.num_of_vertices = 0

	def __iter__(self):
		return iter(self.vert_dict.value())

	def add_vertex(self, node):
		self.num_of_vertices = self.num_of_vertices + 1
		self.vert_dict[node] = Vertex(node)
		return self.vert_dict[node]
	
	def get_vertex(self, n):
		return self.vert_dict[n] if n in self.vert_dict else None

	def add_edge(self, frm, to, cost = 0):
		if frm not in self.vert_dict:
			self.add_vertex(frm)
		if to not in self.vert_dict:
			self.add_vertex(to)

		self.vert_dict[frm].add_neighbour(self.vert_dict[to], cost)
		self.vert_dict[to].add_neighbour(self.vert_dict[frm], cost)

	def get_vertices(self):
		return self.vert_dict.keys()

	def depth_first_search(self, array=[]):
		pass

if __name__ == "__main__":
	G = Graph()
	[G.add_vertex(vertex) for vertex in "abcdef"]

	G.add_edge('a', 'b', 7)
	G.add_edge('a', 'c', 9)
	G.add_edge('a', 'f', 14)
	G.add_edge('b', 'c', 10)
	G.add_edge('b', 'd', 15)
	G.add_edge('c', 'd', 11)
	G.add_edge('c', 'f', 2)
	G.add_edge('d', 'e', 6)
	G.add_edge('e', 'f', 9)

	print(G.get_vertices())
	print(G.depth_first_search())
