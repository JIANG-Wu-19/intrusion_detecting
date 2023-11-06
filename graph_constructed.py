# 根据ip packets lengths序列构造图

import json
import numpy as np
import pandas as pd

C = [60, -60, 52, 237, -52, -1500, 52, -652, 52, -868, 52, -1284, 52, -1284, 52, 178, -52, -103, 52, 1500, 968, -52,
     -52, -298, 52, 52, -52]
D = pd.Series(C, index=range(len(C)), name='ip_packets_length')
features = {}
for i in range(len(C)):
    features["{}".format(i)] = "{}".format(D[i])

print(features)

for i in range(len(C)):
    # if i == 0:
    #     if C[i] > 0:
    #         C[i] = 0.5
    #     else:
    #         C[i] = -0.5
    if C[i] < 0:
        C[i] = -i
    else:
        C[i] = i

print(C)

B = []
j = 0
tmp = [C[0]]
for i in range(len(C) - 1):
    if np.sign(C[i]) == np.sign(C[i + 1]):
        # print(C[i],C[i+1])
        tmp.append(C[i + 1])
        # print(tmp)
    else:
        B.append(tmp)
        tmp = [C[i + 1]]

print(B)

edges = []
edge = []
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

with open("graph.json", "w") as f:
    json.dump(res, f, indent=4,ensure_ascii=False)
