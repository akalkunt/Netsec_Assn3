from scipy.stats import entropy
import numpy as np
import math

normal_matrix = np.zeros(shape = (51,51))
total_per_node = np.zeros(shape = (51))
normal_AS_matrix = np.zeros(shape = (51,51))
normal_prob_matrix = np.zeros(shape = (51,51))
def calculate_matrix(f):
    for l in f:
        objects = l.split()
        source_node = int(objects[1])
        dest_node = int(objects[2])
        if source_node == 100:
            source_node = 51
        if dest_node == 100:
            dest_node = 51
        if objects[3]=="TCP" and objects[7] == "SYN" and objects[8] == "1":
            normal_matrix[source_node-1][dest_node -1]+= 1
            #node_recv_SYN[dest_node-1] += 1
            total_per_node[source_node-1] += 1

    for i in range(51):
        for j in range(51):
            normal_prob_matrix[i][j] = (normal_matrix[i][j]/total_per_node[i])
    normal_AS_matrix = -1 * np.log(normal_prob_matrix, out=np.zeros_like(normal_prob_matrix), where=(normal_prob_matrix!=0))
    #print(normal_AS_matrix)
    print("STARTTTTTTTTTT")
    for i in range(51):
        print(normal_prob_matrix[i][50], i)
    print("DONEEEEEEEEEEEE")
    return normal_AS_matrix


nodes = []
paths_from = {}

def unique(array):
    n = len(array)
    s = set()
    for i in range(0,n):
        s.add(array[i])
    return(len(s) == len(array))

if __name__ == "__main__":
    f = open("normal.tr","r")
    pairs = []
    triples = []
    quads = []
    penta = []
    hexa = []
    p_matrix = calculate_matrix(f)
    #for i in range(51):
       # for j in range(51):
       # print(p_matrix[i])
    test_file = open("trace3.tr","r")
    t_matrix = calculate_matrix(test_file)

    #for i in range(51):
        #print(t_matrix[i][50])
        #print("NOrmal:",p_matrix[i][50])
    for i in range(51):
        for j in range(51): 
            if t_matrix[i][j] > 2.77:
                if i not in nodes:
                    nodes.append(i)
                #print("Detected anamoly from host: ",i, "To:",j)
                if i in paths_from.keys():
                    paths_from[i].append(j)
                else:
                    paths_from[i] = [j,]
    #print("Nodes from:",nodes)
    #print("Paths:",paths_from)
    print("\n\nDONE")
    for k in paths_from.keys():
        for v in paths_from[k]:
            pairs.append((k,v))
    for i in range(len(pairs)):
        for j in range(len(pairs)):
            if pairs[j][0] == pairs[i][1]:
                if unique([pairs[i][0], pairs[i][1],pairs[j][1]]):
                    triples.append((pairs[i][0],pairs[i][1],pairs[j][1]))
    #print(len(triples))
    for i in range(len(triples)):
        for j in range(len(triples)):
            if triples[j][0] == triples[i][1] and triples[j][1] == triples[i][2]:
                if unique([triples[i][0],triples[i][1],triples[i][2],triples[j][2]]):
                    quads.append((triples[i][0],triples[i][1],triples[i][2],triples[j][2]))
    #print((quads))
    for i in range(len(quads)):
        for j in range(len(quads)):
            if quads[j][0] == quads[i][1] and quads[j][1] == quads[i][2] and quads[j][2] == quads[i][3]:
                if unique([quads[i][0],quads[i][1],quads[i][2],quads[i][3],quads[j][3]]):
                        penta.append((quads[i][0],quads[i][1],quads[i][2],quads[i][3],quads[j][3]))
    #print((penta))
    for i in range(len(penta)):
        for j in range(len(penta)):
            if penta[j][0] ==penta[i][1] and penta[j][1]==penta[i][2] and penta[j][2] == penta[i][3] and penta[j][3]==penta[i][4]:
                if unique([penta[i][0], penta[i][1], penta[i][2], penta[i][3], penta[i][4], penta[j][4]]):
                    hexa.append((penta[i][0], penta[i][1], penta[i][2], penta[i][3], penta[i][4], penta[j][4]))
    #print(len(hexa))
