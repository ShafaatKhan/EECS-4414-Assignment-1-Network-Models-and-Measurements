import networkx as nx
from matplotlib import pyplot as plt
from collections import Counter

#number of nodes
num_of_nodes = 1000

#number of edges
num_of_edges = 10000

#calculating the maximum number of edges using (n * n-1)/2 formula
emax = (num_of_nodes*num_of_nodes-1)/2

#p = num of edges/max num of edges
p = num_of_edges/emax

fig, ax = plt.subplots(1, 3, figsize=(10,10), dpi=100, constrained_layout=True)
fig2, ax2 = plt.subplots(1, 3, figsize=(10,10), dpi=100, constrained_layout=True)

print("Erdos Renyi graph\n")

#generating graph 3 times
for i in range(3):
    #erdos renyi graph with 1000 nodes and probability p
    ER = nx.erdos_renyi_graph(num_of_nodes, p)
    
    #finding the giant connected component by calculating the maximum subgraph in the erdos renyi graph
    largest_cc_ER = max((ER.subgraph(c) for c in nx.connected_components(ER)), key=len)
    
    #prints number of nodes and edges in the giant connected component
    
    print(largest_cc_ER)
   
    #global clustering coefficient 
    print("Global clustering coefficient: ", nx.average_clustering(largest_cc_ER))

    #average shortest path length of the graph
    print("Average shortest path length: ", nx.average_shortest_path_length(largest_cc_ER))

    #diameter of graph
    print("Diameter: ", nx.diameter(largest_cc_ER))
    
    #calculating the degrees
    degrees = [largest_cc_ER.degree(n) for n in largest_cc_ER.nodes()]
    
    ax[i].hist(degrees)
    ax[i].set_xlabel('Degree')
    ax[i].set_ylabel('Number of nodes')

    #calculating the frequencies of each clustering coefficient (number of times it is repeated)
    frequencies = Counter(nx.clustering(largest_cc_ER).values())
    ax2[i].hist(frequencies.keys())
    ax2[i].set_xlabel('Clustering coefficient')
    ax2[i].set_ylabel('Frequency')
    print("\n")

fig.suptitle("Node degree distribution Erdos Renyi")
fig2.suptitle("Clustering coefficient distribution Erdos Renyi")
plt.show()

print("-------------------------------------")
print("Watts Strogatz graph\n")

#calculating k for the watts strogatz graph 
k = 2*num_of_edges//num_of_nodes

fig, ax = plt.subplots(1,3, figsize=(10,10), dpi=100, constrained_layout=True)
fig2, ax2 = plt.subplots(1, 3, figsize=(10,10), dpi=100, constrained_layout=True)

#arbitrary probability chosen for the watts strogatz graph 
p = 0.3

#generating graph 3 times
for i in range(3):
    #watts strogatz graph with 1000 nodes and probability p
    WS = nx.watts_strogatz_graph(num_of_nodes, k, p)
    
    #finding the giant connected component by calculating the maximum subgraph in the watts strogatz graph
    largest_cc_WS = max((WS.subgraph(c) for c in nx.connected_components(WS)), key=len)
    
    #prints number of nodes and edges in the giant connected component
    
    print(largest_cc_WS)

    #global clustering coefficient
    print("Global clustering coefficient: ",  nx.average_clustering(largest_cc_WS))

    #average shortest path length of the graph
    print("Average shortest path length: ",  nx.average_shortest_path_length(largest_cc_WS))

    #diameter of graph
    print("Diameter: ",  nx.diameter(largest_cc_WS))

    #calculating the degrees
    degrees = [largest_cc_WS.degree(n) for n in largest_cc_WS.nodes()]

    ax[i].hist(degrees)
    ax[i].set_xlabel('Degree')
    ax[i].set_ylabel('Number of nodes')
        
    #calculating the frequencies of each clustering coefficient (number of times it is repeated)    
    frequencies = Counter(nx.clustering(largest_cc_ER).values())
    ax2[i].hist(frequencies.keys())
    ax2[i].set_xlabel('Clustering coefficient')
    ax2[i].set_ylabel('Frequency')
    
    #updating probability
    p+=0.3
    print("\n")

fig.suptitle("Node degree distribution Watts Strogatz")
fig2.suptitle("Clustering coefficient distribution Watts Strogatz")
plt.show()

print("-------------------------------------")
print("Barabasi Albert graph\n")

#in order to get 10000 edges, each node should be connected to 10 nodes.
#so dividing number of edges by number of nodes gives 10 which is m
m = num_of_edges//num_of_nodes

fig, ax = plt.subplots(1,3, figsize=(10,10), dpi=100, constrained_layout=True)
fig2, ax2 = plt.subplots(1, 3, figsize=(10,10), dpi=100, constrained_layout=True)

#generating graph 3 times
for i in range(3):
    #Barabasi Albert graph with 1000 nodes and m number of connected nodes
    BA = nx.barabasi_albert_graph(num_of_nodes, m)
    #finding the giant connected component by calculating the maximum subgraph in the Barabasi Albert graph
    largest_cc_BA = max((BA.subgraph(c) for c in nx.connected_components(BA)), key=len)
    
    #prints number of nodes and edges in the giant connected component
    print(largest_cc_BA)
    
    #global clustering coefficient
    print("Global clustering coefficient: ",  nx.average_clustering(largest_cc_BA))

    #average shortest path length of the graph
    print("Average shortest path length: ",  nx.average_shortest_path_length(largest_cc_BA))

    #diameter of graph
    print("Diameter: ",  nx.diameter(largest_cc_BA))

    #calculating the degrees
    degrees = [largest_cc_BA.degree(n) for n in largest_cc_BA.nodes()]

    ax[i].hist(degrees)
    ax[i].set_xlabel('Degree')
    ax[i].set_ylabel('Number of nodes')
    #making it a log-log scale graph
    ax[i].set_yscale('log')
    ax[i].set_xscale('log')

    #calculating the frequencies of each clustering coefficient (number of times it is repeated)
    frequencies = Counter(nx.clustering(largest_cc_ER).values())
    ax2[i].hist(frequencies.keys())
    ax2[i].set_xlabel('Clustering coefficient')
    ax2[i].set_ylabel('Frequency')
    print("\n")

fig.suptitle("log-log scale Node degree distribution Barabasi Albert")
fig2.suptitle("Clustering coefficient distribution Barabasi Albert")
plt.show()

