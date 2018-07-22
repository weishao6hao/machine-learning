#coding=utf8

def insert_sort(lists):
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            j -= 1
    return lists

def SelectPivotMedianOfThree(arr,low,high):
    mid = low + ((high - low) >> 1)  #计算数组中间的元素的下标
    #使用三数取中法选择枢轴
    if (arr[mid] > arr[high]):   #目标: arr[mid] <= arr[high]
        arr[high],arr[mid] = arr[mid],arr[high]
    if (arr[low] > arr[high]):  #目标: arr[low] <= arr[high]
        arr[high],arr[low] = arr[low],arr[high]
    if (arr[mid] > arr[low]):   #目标: arr[low] >= arr[mid]
        arr[low],arr[mid] = arr[mid],arr[low]
    #此时，arr[mid] <= arr[low] <= arr[high]
    return arr[low]
    #low的位置上保存这三个位置中间的值
    #分割时可以直接使用low位置的元素作为枢轴，而不用改变分割函数了

def QSort(arr, low, high):
    #三数取中选择枢轴+插排+聚集相等元素
    first = low
    last = high

    left = low
    right = high
    leftLen = 0
    rightLen = 0

    if (high - low + 1 < 10):
        return arr[:low]+insert_sort(arr[low:high+1])+arr[high+1:]
    key = SelectPivotMedianOfThree(arr,low,high)   #使用三数取中法选择枢轴

    while(low < high):
        while(high > low and arr[high] >= key):
            if (arr[high] == key):  #处理相等元素
                arr[high],arr[right] = arr[right],arr[high]
                right-=1
                rightLen+=1
            high-=1
        arr[low] = arr[high]
        while(high > low and arr[low] <= key):
            if (arr[low] == key):
                arr[low],arr[left] = arr[left],arr[low]
                left+=1
                leftLen+=1
            low+=1
        arr[high] = arr[low]
    arr[low] = key

    #一次快排结束
    #把与枢轴key相同的元素移到枢轴最终位置周围
    i = low - 1
    j = first
    while(j < left and arr[i] != key):
        arr[j],arr[i] = arr[i],arr[j]
        i-=1
        j+=1
    i = low + 1
    j = last
    while(j > right and arr[i] != key):
        arr[j],arr[i] = arr[i],arr[j]
        i+=1
        j-=1
    QSort(arr,first,low - 1 - leftLen)
    QSort(arr,low + 1 + rightLen,last)
print(QSort([3,5,7,4,1,4],0,5))