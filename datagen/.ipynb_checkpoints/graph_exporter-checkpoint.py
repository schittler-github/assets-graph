import os
import networkx as nx

def to_graphmlFile(theGraph,location):
    assets = theGraph.assetlist
    edges = theGraph.edges
    
    #here we have the opportunity to chage the formation, the attributes of each node and edge.
    #for now, let us just pass our original data
    G=nx.DiGraph()
    for i in range(len(assets)):
        G.add_node(assets[i])
    
    for i in range(len(edges)):
        G.add_edge(edges[i][0],edges[i][1],fraction=theGraph.weights[i])
    
    output_file = open(location,"w")
    nx.write_graphml_lxml(G,location)
    output_file.close()