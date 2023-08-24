import networkx as nx
import matplotlib.pyplot as plt

#Task 1.1 and 1.2

graph = nx.karate_club_graph()

for n in graph.nodes():
    if graph.nodes[n]["club"] == "Mr. Hi":
        graph.add_node(n, color="green")
    elif graph.nodes[n]["club"] == "Officer":
        graph.add_node(n, color="blue")

node_colors = {"green":"g", "blue":"b"}
colors = []
for n in graph.nodes():
    color = graph.nodes[n]["color"]
    colors.append(node_colors[color])
print(graph.nodes(data=True))
nx.draw(graph, with_labels=True, node_color=colors)
plt.show()

#task 1.3
dijkstra = nx.dijkstra_path(graph, 24, 16)
print(dijkstra)

#Task 1.4
highlight_color = "red"
node_colors_highlighted = []

for n in graph.nodes():
    if n in dijkstra:
        node_colors_highlighted.append(highlight_color)
    else:
        node_colors_highlighted.append(colors[n])

nx.draw(graph, with_labels=True, node_color=node_colors_highlighted)
plt.show()