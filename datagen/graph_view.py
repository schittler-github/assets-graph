import networkx as nx
from pyvis.network import Network
import webbrowser

class GraphView():
    def __init__(self,graphData,fileName):
        self.G = nx.DiGraph()
        self.mountGraph(graphData)
        self.name = fileName
        
    def mountGraph(self,data):
        #G.add_edges_from(edges)
        for i in range(len(data.assetlist)):
            self.G.add_node(data.assetlist[i])    
        for i in range(len(data.edges)):
            self.G.add_edge(data.edges[i][0],data.edges[i][1], label=str(data.weights[i])[0:5])
            #print(data.edges[i][0]," ",data.edges[i][1]," ",str(data.weights[i]))

    def display(self):
        net = Network(height ='1200px', width ='100%', bgcolor='#ffffff', font_color='#000000',directed =True,notebook=True, cdn_resources='remote')
        # net.show_buttons(filter_=True)
        net.from_nx(self.G)
        net.repulsion()
        
        # this method would generate the html and display it directly on a jupter notebook. Calling from a function it does not display
        net.show(self.name)
        
        # this will open the html in a new tab
        webbrowser.open_new_tab(self.name)