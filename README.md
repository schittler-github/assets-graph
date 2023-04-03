
## Project details
The aim of this project is to showcase how graph-quary languages can be used to analyse a list of assets and their owners.
E.g. we can estimate how perturbations to the systems, i.e. problems with one node, will affect other nodes in the network in a natural way.

This project is divided into four main parts: 
1. first is the synthetic data generation;
2. second is the export the resulting list (data generated) into a graphml file;
3. is the preparation to connect the Jupyter notebook to the Gremlin server
4. is the analysis in itself. 

I will post a step-by-step setup in separate file called "CONFIG_README".

The data generation is done in python via a jupyter Lab project.
The analysis of the data is done via queries to a Gremlin server; 
The result presentation is generated via python.

**To run this project** you will need: **Jupyter Lab** and  **Gremlin server** on your machine. A variation of this project will be later ported to Azure, for demonstrating another workflow. 

### queries design and aims
The aim here is to showcase how simple the design of queries become, regardign the graph, when using a Graphic language framework, used in Gremlin.
After generating the graph, we will use Gremlin in two ways:
1. use the Gremlin console to prototype our queries
2. use python libraries to query the data directly from the Jupyter notbook, in order to have the data directly available to generate a visual report.

the questions we will implement are:
1. given a node, are there feedback loops? how many? What is the proportion of indirect self-ownership?
2. given a node, how strongly this node may affect other nodes? Which nodes are affected? in which depth? 