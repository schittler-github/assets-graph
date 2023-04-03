import random
import string
import numpy as np

class AssetNetwork:
    def __init__(self,number_nodes,connect_probability,name_length):
        print("number of nodes: ",number_nodes," probability per connection: ",connect_probability," names length: ",name_length)      
        self.N = number_nodes
        self.conProb = connect_probability
        self.nameLength = name_length
        self.assetlist = self.gen_random_asset_list(self.N,self.nameLength)
        print("List of assets(nodes): ",self.assetlist)
        self.edges = self.gen_edges(self.assetlist, self.conProb)
        print("List of connections(edges): ",self.edges)
        self.weights = [0]*len(self.edges)
        self.assetsValue = self.gen_edge_weights()
        print("Connections(edges) weights: ",self.weights)
         
    # code to generate a single random string
    def get_random_string(self,length):    # Only upper case
        letters = string.ascii_uppercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

    # code to generate a list of random strings. Return approx "N=length" elements because identical ones are dropped
    def gen_random_asset_list(self,length,name_length):
        my_asset_list = []
        for i in range(length):
            asset_name = self.get_random_string(name_length)
            my_asset_list.append(asset_name)
        #remove identical entries by passing the generated list into a set and back to a list.
        new_asset_list = list(set(my_asset_list))
        return new_asset_list
    
    # generate a list of probabilities to a edge to exists from each node:
    def gen_edges(self,lista,prob):
        edges_list = []
        for i in lista:
            for j in lista:
                if np.random.uniform(0,1) < prob and i!=j:
                    edges_list.append((i,j))    
        return edges_list
    
    #this will split the value in a given number of parts
    def split_num_random(self,value,num_parts):
        dividing_points = []
        parts = []
        if num_parts == 1:
            parts.append(value)
            
        elif num_parts > 1:
            for i in range(0, num_parts-1):
                dividing_points.append(np.random.uniform(0,value))
            dividing_points.sort()
            #print(dividing_points)
            old_value = 0
            for i in range(len(dividing_points)):
                parts.append(dividing_points[i]-old_value)
                old_value = dividing_points[i]
            parts.append(value-old_value)
            #print(parts)
        return parts
    
    def gen_edge_weights(self):
        # count number of connections for a node
        count = 0
        edges_index=[]
        for i in self.assetlist:
            node = i
            for j in range(len(self.edges)):
                if self.edges[j][1] == node:
                    edges_index.append(j)
                    count=count+1
    
            #print(count)
            parts_local = self.split_num_random(1,count)
            #print(parts_local)
    
            count = 0
            for j in edges_index:
                #print(j)
                # weights are changed directly over the external variable
                self.weights[j]=parts_local[count]
                count=count+1
                
        #print(self.weights)        
        return  self.weights
