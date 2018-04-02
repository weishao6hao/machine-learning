# kmeans algorithm
import numpy as np
import matplotlib.pyplot as plt
def kmeans(data,k):
    '''
    input:   data(mat): 训练数据
    	       k(int) : 类别个数
    output:  subCenters(mat) : 每个点所属的类别
    '''
    m,n = data.shape
    center=data[np.random.choice(m,k),:]
    label = np.zeros((m, 1))
    distance_matrix=np.zeros((m,k))
    change=True
    while change==True:
        change=False
        for i in range(m):
            distance_matrix[i,:]=list(map(lambda a : np.linalg.norm(a-data[i,:]),center))
        label_new=np.argmin(distance_matrix,axis=1)
        for i in range(k):
            center[i,:]=np.mean(data[label_new==i])
        if (label_new!=label).any():
            change=True
        label=label_new
    return label

def main():
    data1=np.random.normal(size=(20,2))
    data2=np.random.normal(size=(20,2))+3
    data=np.append(data1,data2,axis=0)
    label=kmeans(data,2)
    plt.scatter(data[:,0],data[:,1],c=label)
    plt.show()

if __name__=='__main__':
    main()


