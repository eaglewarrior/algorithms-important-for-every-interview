def bubble_sort(alist):
    for passnum in range(len(alist)-1,0,-1):#here we sort from range lenth of list to 0 
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                
                alist[i], alist[i+1] = alist[i+1], alist[i]
                

alist = [54,26,93,17,77,31,44,55,20]
bubble_sort(alist)
print(alist)

