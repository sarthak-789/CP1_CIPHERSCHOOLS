# link : Minimize the maximum difference between adjacent elements in an array


import sys 
  
INT_MAX = sys.maxsize; 
INT_MIN = -(sys.maxsize - 1)
def minimumAdjacentDifference(a, n, k) :
    minDiff = INT_MAX;
    for i in range( 1<<n) :
        cnt = bin(i).count('1') 
        if (cnt == n - k) : 
            temp = []
            for j in range(n) : 
                if ((i & (1 << j)) != 0) : 
                    temp.append(a[j])
            maxDiff = INT_MIN
              
            for j in range(len(temp) - 1) : 
                maxDiff = max(maxDiff, temp[j + 1] - temp[j])
            
            minDiff = min(minDiff, maxDiff)
       
    return minDiff 
 
if __name__ == "__main__" : 
  
    n = 5; 
    k = 2; 
  
    a = [ 3, 7, 8, 10, 14 ]; 
  
    print(minimumAdjacentDifference(a, n, k)); 