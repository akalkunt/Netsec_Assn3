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
for i in range (0,51):
    node_send_SYN.append(0)
    node_recv_SYN.append(0)
    node_send_ENC.append(0)
    node_recv_ENC.append(0)
f1 = open("normal.tr","r")
for l in f1:
    objects = l.split()
    source_node = objects[1]
    dest_node = objects[2]
    if objects[3]=="TCP" and objects[7] == "SYN":
        print("Dest node:",int(dest_node))
        if int(source_node) !=100 and int(dest_node) != 100:
            node_send_SYN[int(source_node)] += 1
            node_recv_SYN[int(dest_node)] += 1
            total_SYN += 1
    if objects[3] == "TCP" and objects[8] == "1":
        if int(source_node) != 100 and int(dest_node) != 100:
            node_send_ENC[int(source_node)] += 1
            node_recv_ENC[int(dest_node)] += 1
            total_ENC += 1

#for k in node_send_SYN.keys():
for i in range(0,51):
    prob_node_send_SYN.append(node_send_SYN[i]/total_SYN)
    prob_node_recv_SYN.append(node_recv_SYN[i]/total_SYN)
    prob_node_send_ENC.append(node_send_ENC[i]/total_ENC)
    prob_node_recv_ENC.append( node_recv_ENC[i]/total_ENC)

#prob_node_send_SYN --- probability of a node sending a SYN
#prob_node_recv_SYN --- probability of a node receiving a SYN.
#prob_node_send_ENC
#prob_node_recv_ENC

# Calculating entropy:
#send_entropy = 0.0
#recv_entropy = 0.0
#for value in prob_node_send_SYN.values():
#    send_entropy += value*(math.log(value))
#send_entropy = send_entropy* (-1)
print("Entropy measure for a node sending SYN:",entropy(prob_node_send_SYN)/math.log(50))
print("Entropy measure for a node recving SYN:", entropy(prob_node_recv_SYN)/math.log(50))
print("Entropy measure for a node sending ENC:", entropy(prob_node_send_ENC)/math.log(50))
print("Entropy measure for a node recving ENC:", entropy(prob_node_recv_ENC)/math.log(50))
#for value in prob_node_recv_SYN.values():
#    recv_entropy += value*(math.log(value))
#recv_entropy = recv_entropy*(-1)
#print("Entropy measure for a node receiving a SYN:",recv_entropy/math.log(50))

#send_ENC_entropy = 0.0
#recv_ENC_entropy = 0.0

#for value in prob_node_send_ENC.values():
#    send_ENC_entropy += value * (math.log(value))
#send_ENC_entropy = send_ENC_entropy*(-1)
#
#for value in prob_node_recv_ENC.values():
#    recv_ENC_entropy += value * (math.log(value))
#recv_ENC_entropy = recv_ENC_entropy*(-1)

#print ("Entropy measure for node sending ENC:", send_ENC_entropy/math.log(50))
#print("Entropy measure for node receiving ENC:", recv_ENC_entropy/math.log(50))



