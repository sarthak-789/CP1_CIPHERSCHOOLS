# Queue based approach for first non-repeating character in a stream

from queue import Queue 
def firstnonrepeating(Str): 
    global MAX_CHAR 
    q = Queue() 
    charCount = [0] * MAX_CHAR 
    for i in range(len(Str)):
        q.put(Str[i])   
        charCount[ord(Str[i]) - 
                  ord('a')] += 1
        while (not q.empty()):  
            if (charCount[ord(q.queue[0]) - 
                          ord('a')] > 1):  
                q.get()  
            else: 
                print(q.queue[0], end = " ")  
                break
  
        if (q.empty()):  
            print(-1, end = " ") 
    print() 

MAX_CHAR = 26
Str = "aabc"
firstnonrepeating(Str) 