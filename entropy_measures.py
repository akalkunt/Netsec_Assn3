import math
from scipy.stats import entropy
node_send_SYN = []
node_recv_SYN = []
node_send_ENC = []
node_recv_ENC = []
total_SYN = 0
total_ENC = 0
prob_node_recv_SYN = []
prob_node_send_SYN = []
prob_node_send_ENC = []
prob_node_recv_ENC = []
for i in range (52):
    node_send_SYN.append(0)
    node_recv_SYN.append(0)
    node_send_ENC.append(0)
    node_recv_ENC.append(0)
f1 = open("normal.tr","r")
for l in f1:
    objects = l.split()
    source_node = int(objects[1])
    dest_node = int(objects[2])
    if source_node == 100:
        source_node = 51
    if dest_node == 100:
        dest_node = 51
    if objects[3]=="TCP" and objects[7] == "SYN":
            node_send_SYN[source_node] += 1
            node_recv_SYN[dest_node] += 1
            total_SYN += 1
    if objects[3] == "TCP" and objects[8] == "1":
            node_send_ENC[source_node] += 1
            node_recv_ENC[dest_node] += 1
            total_ENC += 1

for i in range(52):
    prob_node_send_SYN.append(node_send_SYN[i]/total_SYN)
    prob_node_recv_SYN.append(node_recv_SYN[i]/total_SYN)
    prob_node_send_ENC.append(node_send_ENC[i]/total_ENC)
    prob_node_recv_ENC.append( node_recv_ENC[i]/total_ENC)

#prob_node_send_SYN --- probability of a node sending a SYN
#prob_node_recv_SYN --- probability of a node receiving a SYN.
#prob_node_send_ENC
#prob_node_recv_ENC

# Calculating entropy:
print("Entropy measure for a node sending SYN:",entropy(prob_node_send_SYN)/math.log(51))
print("Entropy measure for a node recving SYN:", entropy(prob_node_recv_SYN)/math.log(51))
print("Entropy measure for a node sending ENC:", entropy(prob_node_send_ENC)/math.log(51))
print("Entropy measure for a node recving ENC:", entropy(prob_node_recv_ENC)/math.log(51))



