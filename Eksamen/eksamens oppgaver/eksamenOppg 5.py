import networkx as nx
from networkx import community
from networkx.algorithms.community import greedy_modularity_communities, label_propagation_communities

G = nx.karate_club_graph()
#Measuring centrality using degree centrality
degree_centrality = nx.degree_centrality(G)

#measuring modularity with louvain method and label propagation
#modularity first;
communities = greedy_modularity_communities(G)
partitions = {}
for i, comm in enumerate(communities):
    for node in comm:
        partitions[node] = i

#Measuring modularity:
louvain_modularity = nx.algorithms.community.modularity(G, communities)

"""the modularity score tells how strongly nodes are connected within the communities.
worse than 0 means that the network is highly fragmented, the closer the score is to 1 the more connected nodes within
communities are."""
#label propagation
propagation_communites = label_propagation_communities(G)
for i, comm in enumerate(propagation_communites):
    print("communities", i, comm, "\n")
    """This gives a list of the nodes that belong to the same score, and not a modularity score.
    but it gives a nice overview over the communities."""

print("centrality of the nodes", degree_centrality)
print("modularity using lovuain", louvain_modularity)

#changing size and color using degree centrality and modularity:
#layout:
pos = nx.spring_layout(G)

#changing colors:
node_colors = {}
for node in G.nodes:
    node_colors[node] = node

#changing node size:
node_sizes=[]
for node in G.nodes:
    node_sizes.append(degree_centrality[node] * 1500)

#drawing graph:
import matplotlib.pyplot as plt

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_color=list(node_colors.values()), node_size=node_sizes, cmap='cool')

# Draw edges
nx.draw_networkx_edges(G, pos)

# Draw labels (optional)
nx.draw_networkx_labels(G, pos)

# Show the graph
plt.axis('off')
plt.show()