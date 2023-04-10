For this projec to work, we need to install some programs and modules first. Here I will describe all steps necessary to run this demo, in particular on windows. On linux most of the packages and programs can be downloaded using the command line.

1) Download and Install Python 3 either from the official webpage or the windows-store;

2) Download and Install Anaconda Navigator from the official webpage
    a) from the navigator install Jupyter Lab on your computer
    
3) Download Gremlin Server from the offcial website. Unzip it on your favorite folder.
    a) now edit the following files to make in run from a Jupyter notebook: (as described in "https://github.com/aws/graph-notebook/blob/main/additional-databases/gremlin-server/README.md")
        i) on "\apache-tinkerpop-gremlin-server-3.6.2\conf\tinkergraph-empty.properties" change:
            "gremlin.tinkergraph.vertexIdManager=LONG" to "gremlin.tinkergraph.vertexIdManager=ANY"
            
        ii) on the same config file add:   
            "gremlin.tinkergraph.edgeIdManager=ANY"
            
        iii)on "\apache-tinkerpop-gremlin-server-3.6.2\conf\gremlin-server.yaml" change 
            "channelizer: org.apache.tinkerpop.gremlin.server.channel.WebSocketChannelizer" to "channelizer: org.apache.tinkerpop.gremlin.server.channel.WsAndHttpChannelizer"
            
4) Download and install Git from the official website
    a) clone this project
    
5) start the Gremlin server from your bin/gremlin-server.bat (windows) or bin/gremlin-server.sh (linux), let it running.

6) in another terminal open the root directory of this project and start jupyter but typiong "Jupyter lab"

7) on jupyter open another terminal and install the following packages and modultes.
    a) networkx
    b) gremlinpython
    c) pyvis

6) now you should be able to run the demo code, starting on the "main" file.

7) please explore and comment


PS: this is just a demo code for showcasing using gremling from Jupyter. The code is not optimized. In particular the algorithm will try to find all possible unique paths, there is no limit on time or iterations, so far. I will implement this option in the next iteration.