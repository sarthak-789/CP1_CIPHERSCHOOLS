# Is mIrror Inverse geek for geeks

def isMirrorInverse(arr, n) :  
  
    for i in range(n) : 
        if (arr[arr[i]] != i) : 
            return False  
    return true  
 
if __name__ == "__main__" : 
      
    arr = [ 1, 2, 3, 0 ]  
      
    n = len(arr)
    if (isMirrorInverse(arr,n)) : 
        print("Yes")  
    else : 
        print("No")  