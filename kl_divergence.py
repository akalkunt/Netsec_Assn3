import math
from scipy.stats import entropy

def probabilities(f):
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
    for l in f:
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
            if objects[8] == "1":
                node_send_ENC[source_node] += 1
                node_recv_ENC[dest_node] += 1
                total_ENC += 1

    for i in range(52):
        prob_node_send_SYN.append(node_send_SYN[i]/total_SYN)
        prob_node_recv_SYN.append(node_recv_SYN[i]/total_SYN)
        prob_node_send_ENC.append(node_send_ENC[i]/total_ENC)
        prob_node_recv_ENC.append(node_recv_ENC[i]/total_ENC)

#prob_node_send_SYN --- probability of a node sending a SYN
#prob_node_recv_SYN --- probability of a node receiving a SYN.
#prob_node_send_ENC
#prob_node_recv_ENC

# Calculating entropy:
    return prob_node_send_SYN, prob_node_recv_SYN, prob_node_send_ENC, prob_node_recv_ENC


## Now, to calculate KL divergence, calculate the same probabilities as above for all test traces.

if __name__ == "__main__":
    f = open("normal.tr","r")
    p_send_SYN, p_recv_SYN, p_send_ENC, p_recv_ENC = probabilities(f)
    print("Entropies for normal trace file:\n")
    print("Send SYN:",entropy(p_send_SYN)/math.log(51))
    print("Send ENC:",entropy(p_send_ENC)/math.log(51))
    for i in range (1,4):
        fname = "trace"+str(i)+".tr"
        f1 = open(fname, "r")
        print("TEST trace: ",fname)
        t_send_SYN, t_recv_SYN, t_send_ENC, t_recv_ENC = probabilities(f1)
        print("KL divergence of send SYN:", entropy(p_send_SYN,t_send_SYN, base=10))
        print("KL divergence of send ENC:", entropy(p_send_ENC, t_send_ENC, base=10))
        
