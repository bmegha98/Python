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
        
