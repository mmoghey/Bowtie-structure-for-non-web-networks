import snap
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import mlab

#find the type of component
def findComponent(G, NId):
    BfsTreeOut = snap.GetBfsTree(G, NId, True, False)
    BfsTreeIn = snap.GetBfsTree(G, NId, False, True)
    #print (BfsTreeOut.GetNodes(), BfsTreeIn.GetNodes())

    if ((BfsTreeOut.GetNodes() < BfsTreeIn.GetNodes()) & (BfsTreeOut.GetNodes() == 1)):
        print (NId, " : OUT")
    elif ((BfsTreeOut.GetNodes() > BfsTreeIn.GetNodes()) & (BfsTreeIn.GetNodes() == 1)):
        print (NId, " : IN")
    else:
        print (NId, " : SCC")

#############################################################################
#Problem 2.1   
#############################################################################
#Load the Email Graph
G1 = snap.LoadEdgeList(snap.PNGraph, "C:\Users\manas\Documents\eBooks\Advanced Databases\HomeWork2\email-EuAll\Email-EuAll.txt", 0, 1)
NId = 189587
findComponent(G1, NId)
NId = 675
findComponent(G1, NId)


#Load the Epinions Graph
G2 = snap.LoadEdgeList(snap.PNGraph, "C:\Users\manas\Documents\eBooks\Advanced Databases\HomeWork2\soc-Epinions1\soc-Epinions1.txt", 0, 1)
NId = 9809
findComponent(G2, NId)
NId = 1952
findComponent(G2, NId)

###############################################################################
#Problem 2.2
###############################################################################
#Draw the cumulative distribution for email graph	
numNodes = G1.GetNodes()
num = 100
count = 0
nodesIn = np.zeros(num)
nodesOut = np.zeros(num)
cnt = range(0,num)
for i in range (0,num):
    cnt[i] = cnt[i]/(1.0 * 100)
while (count < num):
    nodeId = random.randint(0,numNodes)
    BfsTreeOut = snap.GetBfsTree(G1, nodeId, True, False)
    BfsTreeIn = snap.GetBfsTree(G1, nodeId, False, True)
    if (count == 0):
        nodesIn[count] = 0
    else : 
        nodesIn[count] = nodesIn[count - 1] + BfsTreeIn.GetNodes()
    #nodesIn [count] = 	{count, BfsTreeIn.GetNodes()}
    if (count == 0):
        nodesOut[count] = 0
    else : 
        nodesOut[count] = nodesOut[count - 1] + BfsTreeOut.GetNodes()
	
    print "Node Id:", nodeId, "     Nodes Traversed inward : ", BfsTreeIn.GetNodes(), "          Nodes traversed outwards :", BfsTreeOut.GetNodes()
    count = count + 1
	
	
#Draw the cumulative distribution for email graph	
X = cnt
Y = nodesIn
plt.subplot(221)
plt.semilogy(X,Y, drawstyle = 'steps')
plt.xlabel('Frac. of Starting Nodes')
plt.ylabel('number of nodes reached (log)')
plt.title('Email: Reachability using In-links')
plt.grid(True)


X = cnt
Y = nodesOut
plt.subplot(222)
plt.semilogy(X,Y, drawstyle = 'steps')
plt.xlabel('Frac. of Starting Nodes')
plt.ylabel('number of nodes reached (log)')
plt.title('Email: Reachability using Out-links')
plt.grid(True)
plt.show()

#draw the cumulative distribution for Epinion Graph
numNodes = G2.GetNodes()
num = 100
count = 0
nodesIn = np.zeros(num)
nodesOut = np.zeros(num)
cnt = range(0,num)
for i in range (0,num):
    cnt[i] = cnt[i]/(1.0 * 100)
while (count < num):
    nodeId = random.randint(0,numNodes)
    BfsTreeOut = snap.GetBfsTree(G2, nodeId, True, False)
    BfsTreeIn = snap.GetBfsTree(G2, nodeId, False, True)
    if (count == 0):
        nodesIn[count] = 0
    else : 
        nodesIn[count] = nodesIn[count - 1] + BfsTreeIn.GetNodes()
    #nodesIn [count] = 	{count, BfsTreeIn.GetNodes()}
    if (count == 0):
        nodesOut[count] = 0
    else : 
        nodesOut[count] = nodesOut[count - 1] + BfsTreeOut.GetNodes()
	
    print "Node Id:", nodeId, "     Nodes Traversed inward : ", BfsTreeIn.GetNodes(), "          Nodes traversed outwards :", BfsTreeOut.GetNodes()
    count = count + 1

	
X = cnt
Y = nodesIn
plt.subplot(221)
plt.semilogy(X,Y, drawstyle = 'steps')
plt.xlabel('Frac. of Starting Nodes')
plt.ylabel('number of nodes reached (log)')
plt.title('Epinions: Reachability using In-links')
plt.grid(True)


X = cnt
Y = nodesOut
plt.subplot(222)
plt.semilogy(X,Y, drawstyle = 'steps')
plt.xlabel('Frac. of Starting Nodes')
plt.ylabel('number of nodes reached (log)')
plt.title('Epinions: Reachability using Out-links')
plt.grid(True)
plt.show()


###################################################################
#2.3
###################################################################

#Calculate the values for email graph
total_nodes = G1.GetNodes()
largest_scc = snap.GetMxScc(G1)
SCC = largest_scc.GetNodes()
random_nid_in_scc = largest_scc.GetRndNId()

##Find the out − and in −components
outcomp = snap.GetBfsTree(G1, random_nid_in_scc, True, False)
incomp = snap.GetBfsTree(G1, random_nid_in_scc, False, True)

sz_outcomp = outcomp.GetNodes()
sz_incomp = incomp.GetNodes()

G_WCC = snap.GetMxWcc(G1)
WCC = G_WCC.GetNodes()
disconnected = total_nodes  - WCC
IN = sz_incomp − SCC
OUT = sz_outcomp − SCC
tendrills = WCC - SCC - IN - OUT

print "Size of Disconnected: ", disconnected
print "Size of largest SCC:", SCC
print "Size of out−component: ", OUT
print "Size of in−component: ", IN
print "Size of tendrills: ", tendrills 


#Calculate the values for epinion graph
total_nodes = G2.GetNodes()
largest_scc = snap.GetMxScc(G2)
SCC = largest_scc.GetNodes()
random_nid_in_scc = largest_scc.GetRndNId()

# Find the out− and in−components
outcomp = snap.GetBfsTree(G2, random_nid_in_scc, True, False)
incomp = snap.GetBfsTree(G2, random_nid_in_scc, False, True)

sz_outcomp = outcomp.GetNodes()
sz_incomp = incomp.GetNodes()

G_WCC = snap.GetMxWcc(G2)
WCC = G_WCC.GetNodes()
disconnected = total_nodes  - WCC
IN = sz_incomp − SCC
OUT = sz_outcomp − SCC
tendrills = WCC - SCC - IN - OUT

print "Size of Disconnected: ", disconnected
print "Size of largest SCC:", SCC
print "Size of out−component: ", OUT
print "Size of in−component: ", IN
print "Size of tendrills: ", tendrills 
