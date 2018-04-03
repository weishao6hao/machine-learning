# Kruslal algorithm
import matplotlib.pyplot as plt
from functools import cmp_to_key
import networkx as nx #for visual
def compare(a,b):
    if(a[2] > b[2]):
        return 1
    elif(a[2] < b[2]):
        return -1
    else:
        return 0
def exchange(node):
    if node[0]>node[1]:
        node[0],node[1]=node[1],node[0]
    return node
def visual(graph):
    ls=[tuple(i) for i in graph]
    gh=nx.Graph()
    for i in range(4):
        gh.add_node(i+1)
    gh.add_weighted_edges_from(ls)
    # nx.draw_networkx(gh)
    # plt.show()
    return gh



def Kruslal(graph,num):
    '''
    input:   graph(list[list]): 无向图,example: [2,4,5] : 第2个点到第4个点距离为5
             num(int): 节点的数量
    	       
    output:  result(list[list]): Minimum spanning tree 
    '''
    graph=sorted(graph,key=cmp_to_key(compare))  #按边权重大小排列
    graph=[exchange(i) for i in graph]         #转变 [4,2,5] 为 [2,4,5]
    s=[[]]
    result=[]
    for i in range(num):
        s.append([i+1])
    for e in graph:
        if s[e[0]] != s[e[1]]:
            result.append(e)
            for i in s[e[1]]:
                if (i not in s[e[0]]):
                    s[e[0]].append(i)
                s[e[1]] = s[e[0]]
    print(result)
    return result

def main():
    graph=[[1,2,1],[1,3,2],[2,3,1],[2,4,4],[3,4,2],[4,5,3],[5,3,4]]
    gh=visual(graph)
    result=Kruslal(graph,5)
    # visual
    ls = [tuple(i) for i in result]
    gh.add_weighted_edges_from(ls)
    pos = nx.spring_layout(gh)
    nx.draw_networkx(gh,pos,weight='weight')
    a = [tuple(i) for i in graph]
    remove=set(a)-set(ls)
    gh.remove_edges_from(remove)
    nx.draw_networkx(gh,pos,edge_color = 'r')
    plt.show()

if __name__=='__main__':
    main()