#coding=utf8

def floyd(dismatrix):
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
    result=floyd(D)
    print(result)

if __name__=='__main__':
    main()

