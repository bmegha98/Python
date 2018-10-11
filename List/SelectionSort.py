def IndexOfLargest(l,pos=0,index=-1):
    '''
  Objective        : To determine the index of largest element in list.
  Input parameters :
                  l-> List of numbers
                pos-> Temporary position to access elements of list. 
              index-> Position of element to be compared with elements of list.
  Output           : A positive integer representing index of largest element in l.

    '''
 #Approach : Compare l[index] with each element l[pos] and store position of largest element in index.
    if index==-1:
       index=pos
    if l[pos:]==[]:
       return index
    else:
       if l[index]<= l[pos]:
          index=pos
       return IndexOfLargest(l,pos+1,index)
        
def SelectionSort(l,p=0):
    '''
  Objective        : To sort elements of a list in descending order.
  Input parameters :
                  l-> List of numbers
                  p-> position of element that has to be swapped with maximum element of list.
  Output           : List in which elements are sorted in descending order.

    '''
  #Approach : Find maximum element using IndexOfLargest() function from unsorted array and put it at beginning.
    if l==[]:
        return
    elif l[p:]==[]:
        return l
    else:
        MaxIndex=IndexOfLargest(l,p)
        print('Max element ',l[MaxIndex])
        temp=l[MaxIndex]
        l[MaxIndex]=l[p]
        l[p]=temp
        SelectionSort(l,p+1)
    
  
