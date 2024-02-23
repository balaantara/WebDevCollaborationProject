import numpy
import pandas as pd
import matplotlib.pyplot as plt

def matrict(n, m):
    matc= []
    for i in range(n):
        inp = list(map(str, input()))
        matc.append(inp)

    print(matc)
    
    for i in range(len(matc)):
        print(matc[i])

inp = list(map(int, input().split()))
matrict(inp[0], inp[1])