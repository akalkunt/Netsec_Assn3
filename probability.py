import math

node_send_SYN = {}
node_recv_SYN = {}
prob_node_recv_SYN = {}
prob_node_send_SYN = {}


f1 = open("normal.tr","r")
for l in f1:
    objects = l.split()
    source_node = objects[1]
    dest_node = objects[2]
    if objects[3]=="TCP" and objects[7] == "SYN":
        if source_node in node_send_SYN:
            val = node_send_SYN.get(source_node)
            node_send_SYN[source_node] = val + 1
        else:
            node_send_SYN[source_node] = 1
        if dest_node in node_recv_SYN:
            val = node_recv_SYN.get(dest_node)
            node_recv_SYN[dest_node] = val+1
        else:
            node_recv_SYN[dest_node] = 1

total = 0

for v in node_send_SYN.values():
    total = total+v

for k in node_send_SYN.keys():
    prob_node_send_SYN[k] = node_send_SYN[k]/total

for k in node_recv_SYN.keys():
    prob_node_recv_SYN[k] = node_recv_SYN[k]/total

#prob_node_send_SYN --- probability of a node sending a SYN
#prob_node_recv_SYN --- probability of a node receiving a SYN.

# Calculating entropy:
send_entropy = 0.0
recv_entropy = 0.0
for value in prob_node_send_SYN.values():
    send_entropy += value*(math.log(value))
send_entropy = send_entropy* (-1)
print("Entropy measure for a node sending SYN:",send_entropy/math.log(50))

for value in prob_node_recv_SYN.values():
    recv_entropy += value*(math.log(value))
recv_entropy = recv_entropy*(-1)
print("Entropy measure for a node receiving a SYN:",recv_entropy/math.log(50))

