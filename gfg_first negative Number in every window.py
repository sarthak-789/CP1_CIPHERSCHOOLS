# first negative Number in every window

def printFirstNegativeInteger(arr, n, k): 
    for i in range(0, (n - k + 1)): 
        flag = False
        for j in range(0, k): 
            if (arr[i + j] < 0): 
          
                print(arr[i + j], end = " ") 
                flag = True
                break
          
        if (not(flag)): 
            print("0", end = " ") 

arr = [12, -1, -7, 8, -15, 30, 16, 28] 
n = len(arr) 
k = 3
printFirstNegativeInteger(arr, n, k) 