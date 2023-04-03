from gremlin_python.process.graph_traversal import __
from gremlin_python.process.traversal import Barrier, Bindings, Cardinality, Column, Direction, Operator, Order, P, Pop, Scope, T, WithOptions

class Example1:
    def __init__(self,traverse,graph):
        self.g=traverse
        self.G=graph
        self.lista_firstIn = []
        self.lista_last_values = []
        self.lista_of_dict = []
        self.lista_paths = []
        self.lista_fraction_perPath = []
        self.lista_fractio_perAsset = []
        
    def runAnalysis(self):
        #print("num assets: ",len(self.G.assetlist))
        
        # for each node, step out backwards one time and save it
        self.lista_firstIn = self.findFirstIn()
        #print("\n",self.lista_firstIn)
        
        # let us also save the value of the connections to those other nodes
        self.lista_last_values = self.findFirstInValues()
        #print("\n",self.lista_last_values)
        #print("lista_last_values: ",len(self.lista_last_values))
        
        #create a dictionary for the incomming edges weights
        self.lista_of_dict = self.findListOfDict()
        #print("\n",self.lista_of_dict)
        #print("lista_of_dict: ",len(self.lista_of_dict))
        
        # now let us find all the unique ways, starting from a node, we can loop back to the original node. We basically iterate until the last vertix before the loop closes, or the loop would start and stop, returning the vertex itself.
        self.lista_paths = self.findListPaths()
        #print("\n",self.lista_paths)
        #print("lista_paths: ",len(self.lista_paths))
        
        # multiply the weights of connections trough the path
        self.lista_fraction_perPath = self.findPathFraction()
        #print("\n",self.lista_fraction_perPath)
        #print(len(self.lista_fraction_perPath))
        
        
        #sum all contribution of all paths for each asset
        self.lista_fractio_perAsset = self.sumResults()
        print(self.G.assetlist)
        print(self.lista_fractio_perAsset)
        
    def findFirstIn(self):
        lista_fi = []
        for i in self.G.assetlist:
            lista_fi.append(self.g.V(i).in_().id_().toList())
        return lista_fi
    
    def findFirstInValues(self):
        lista_lv = []
        for i in self.G.assetlist:
            lista_lv.append(self.g.V(i).inE().values("fraction").toList())
        return lista_lv
    
    def findListOfDict(self):
        lista_of_d = []
        for i in range(len(self.G.assetlist)):
            mydict = {}
            for j in range(len(self.lista_firstIn[i])):
                mydict[self.lista_firstIn[i][j]] = self.lista_last_values[i][j]
            lista_of_d.append(mydict)
        return(lista_of_d)
    def findListPaths(self):
        lista_p = []
        for i in range(len(self.G.assetlist)):
            lista_p.append(self.g.V(self.G.assetlist[i]).until(__.has(T.id,P.within(self.lista_firstIn[i]))).repeat(__.out().simplePath()).path().toList())
        return lista_p
    
    def findPathFraction(self):
        # multiply the weights of connections trough the path
        lista_cw = []
        for i in range(len(self.G.assetlist)):
            lista_cw.append(self.g.withSack(0).V(self.G.assetlist[i])\
                .outE().sack(Operator.sum_).by("fraction").inV()\
                .until(__.has(T.id,P.within(self.lista_firstIn[i]))).repeat(__.outE().sack(Operator.mult).by("fraction").inV().simplePath())\
                .sack().toList())
        #print(lista_cw)

        # extract the last step of each path to choose the right outcomming value into the original 
        lista_path_last_value = []
        empty_list = []

        count = 0
        for sub_lista in self.lista_paths:
            sub_last_nodes = []
            sub_last_value = []
            if( sub_lista ):
                for singlePath in sub_lista:
                    sub_last_nodes.append(singlePath[len(singlePath)-1])
                    val = self.g.V(singlePath[len(singlePath)-1]).id_().toList()
                    # val is a list with one string, not a string, so use val[0] to get a simple string
                    sub_last_value.append(self.lista_of_dict[count][val[0]])
            else:
                sub_last_nodes.append(sub_lista)
                sub_last_value.append(empty_list)

            lista_path_last_value.append(sub_last_value)
            count = count + 1   
        #print(lista_path_last_value)
        
        # multiply the results to calculate the complete loop
        lista_finalValues = []
        for i in range(len(self.G.assetlist)):
            complete_value = []
            for j in range(len(lista_path_last_value [i])):
                if(lista_path_last_value[i][j] and lista_cw[i][j]):
                    complete_value.append(lista_path_last_value [i][j]*lista_cw[i][j])
            lista_finalValues.append(complete_value)
            
        return(lista_finalValues)

    def sumResults(self):
        total_sums = []
        for i in range(len(self.G.assetlist)):
            total_sums.append(sum(self.lista_fraction_perPath[i]))

        return total_sums
    
class Example2:
    def __init__(self,traverse,graph):
        print("start example")