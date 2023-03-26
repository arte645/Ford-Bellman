import math as m
from pprint import pprint
def FindMin(temp, matrix, k) :
    minimum = [0, 0, 0, 0, 0, 0]
    for a in range(6):
        minimum[a] = temp[a]+matrix[a][k]
    minimum.sort()
    return minimum[0]

def Negative(matrix,temp,result):
    test=result[:]
    for k in range(6):
        if k == j:
            test[k] = 0
        else:
            test[k]=FindMin(temp,matrix,k)
    if(result!=test):
        print("Имеется цикл отрицательного веса")


i = m.inf
matrix = [[0, 7, 9, i, 11, i],
         [i, 0, 6, 6, i, 13],
         [i, i, 0, 5, 6, i],
         [i, i, i, 0, i, i],
         [i,  4, i, 6, 0, 8],
         [i, i, i, 7, i, 0]]
result = [0,
          0,
          0,
          0,
          0,
          0]
temp = [i,
        i,
        i,
        i,
        i,
        i]
print("Введите номер вершины:", end = " ")
j = int(input())-1
temp[j]=0
for m in range(len(result)):
    for k in range(len(result)):
        if k == j:
            result[k] = 0
        else:
            result[k]=FindMin(temp,matrix,k)
    bup = temp[:]
    temp = result[:]
    if(temp == bup):
        break
Negative(matrix,temp,result)
pprint(result)