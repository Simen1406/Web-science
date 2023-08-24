import networkx as nx
import matplotlib.pyplot as plt
import numpy

#TASK1
G = nx.Graph()
nodes = ["A", "B", "C", "D", "E", "F"]
G.add_nodes_from(nodes)
edges = [("A", "B"), ("A", "C"), ("B", "C"), ("A", "F"), ("C", "D"), ("C", "E"), ("F","E"), ("D", "E")]
G.add_edges_from(edges)
print(G.edges, G.nodes)

nx.draw(G, with_labels=True)
#plt.show()

#TASK2 print shortest path using djikstras algorithm
print(nx.dijkstra_path(G, "A", "D"))


#TASK3 opening csv file and writing as a graph
with open("name_of_file.csv") as infile:
    csv_reader = csv.reader(infile)
    G = nx.Graph(csv_reader)
    print(G.nodes)
