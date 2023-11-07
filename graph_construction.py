import json
import numpy as np
import pandas as pd
import os


def read_csv(num):
    ip_packets_length = pd.read_csv("./csv/{}.csv".format(num))
    return ip_packets_length


# print(read_csv(0))

def graph_constructed(ip_packets_length):
    features = {}
    edges = []
    edge = []

    C = ip_packets_length['ip_packets_length'].tolist()
    # print(C)

    for i in range(len(C)):
        features["{}".format(i)] = "{}".format(C[i])

    for i in range(len(C)):
        if C[i] < 0:
            C[i] = -i
        else:
            C[i] = i

    # print(C)

    B = []
    j = 0
    tmp = [C[0]]

    for i in range(len(C) - 1):
        if np.sign(C[i]) == np.sign(C[i + 1]):
            tmp.append(C[i + 1])
        else:
            B.append(tmp)
            tmp = [C[i + 1]]

    B.append(tmp)

    # print(B)

    for i in range(len(B) - 1):
        if len(B[i]) == 1 and len(B[i + 1]) == 1:
            edge = [abs(B[i][0]), abs(B[i + 1][0])]
            edges.append(edge)
            edge = []
        else:
            edge = [abs(B[i][0]), abs(B[i + 1][0])]
            edges.append(edge)

            edge = [abs(B[i][len(B[i]) - 1]), abs(B[i + 1][len(B[i + 1]) - 1])]
            edges.append(edge)
            edge = []

    for i in range(len(B)):
        if len(B[i]) > 1:
            for j in range(len(B[i]) - 1):
                edge = [abs(B[i][j]), abs(B[i][j + 1])]
                edges.append(edge)
                edge = []

    res = {"edges": edges, "features": features}

    return res


# with open("./json/{}.json".format(num), "w") as f:
# print(graph_constructed(read_csv(0)))

path = './csv'
files = os.listdir(path)

for i in range(len(files)):
    j = graph_constructed(read_csv(i))
    with open("./json/{}.json".format(i), "w") as f:
        json.dump(j, f, indent=4, ensure_ascii=False)

# for j in range(len(files)):
#     graph_constructed(j)

# graph_constructed(0)
