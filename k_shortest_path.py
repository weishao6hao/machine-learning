#coding=utf8
from collections import defaultdict

def floyd(dismatrix):     #最短路径floyd算法
    '''
    input : list[list],距离矩阵
    out :   list[list],最小路径矩阵
    '''
    n=len(dismatrix)
    #initial
    result=[[i for i in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j]=dismatrix[i][j]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if result[j][k]>result[j][i]+result[i][k]:
                    result[j][k]=result[j][i]+result[i][k]
    return result
def k_shortest_path(dismatrix,s,t,k):
    '''
    :param dismatrix:list[list],图路径矩阵 
    :param s: int，起始点
    :param t: int,目标点
    :param k: int,第k短路径
    :return: result,第k短路径长度
    '''

    n=len(dismatrix)
    shortest_path_matrix=floyd(dismatrix)
    H={}
    #求每个点到目标点t的最短距离 H
    for i in range(n):
        H[i]=shortest_path_matrix[i][t]
    neighbor_index=defaultdict(list)
    # 每个点的邻居统计
    for i in range(n):
        for j in range(n):
            if i!=j and dismatrix[i][j]!=float('inf'):
                neighbor_index[i].append(j)
    que = []
    que.append([s,0])
    count=0
    node_list=list(range(n))
    while que:
        que=sorted(que,key=lambda a:a[1]+H[a[0]])
        Fir_que=que.pop(0)
        if Fir_que[0]==t:
            count+=1
            if count==k:   #第k次目标对象出列，输出此时路径长度
                print(Fir_que[1])
                break
        for i in neighbor_index[Fir_que[0]]:
            que.append([i,dismatrix[Fir_que[0]][i]+Fir_que[1]])
    return
def main():
    INFINITY = float('inf')
    D = [[0, 10, INFINITY, INFINITY, INFINITY, 11, INFINITY, INFINITY, INFINITY],  # 邻接矩阵
         [10, 0, 18, INFINITY, INFINITY, INFINITY, 16, INFINITY, 12],
         [INFINITY, 18, 0, 22, INFINITY, INFINITY, INFINITY, INFINITY, 8],
         [INFINITY, INFINITY, 22, 0, 20, INFINITY, INFINITY, 16, 21],
         [INFINITY, INFINITY, INFINITY, 20, 0, 26, INFINITY, 7, INFINITY],
         [11, INFINITY, INFINITY, INFINITY, 26, 0, 17, INFINITY, INFINITY],
         [INFINITY, 16, INFINITY, 24, INFINITY, 17, 0, 19, INFINITY],
         [INFINITY, INFINITY, INFINITY, 16, 7, INFINITY, 19, 0, INFINITY],
         [INFINITY, 12, 8, 21, INFINITY, INFINITY, INFINITY, INFINITY, 0]]
    k_shortest_path(D,0,7,4)

if __name__=='__main__':
    main()




