# link : https://www.geeksforgeeks.org/program-to-print-solid-and-hollow-rhombus-patterns/


def solidRhombus(rows): 
      
    for i in range (1,rows + 1): 
        for j in range (1,rows - i + 1): 
            print (end=" ") 
        for j in range (1,rows + 1): 
            print ("*",end="") 
              
        print() 
  
def hollowRhombus(rows): 
      
    for i in range (1, rows + 1): 
       
        for j in range (1, rows - i + 1): 
            print (end=" ") 
        if i == 1 or i == rows: 
            for j in range (1, rows + 1): 
                print ("*",end="")
        else: 
            for j in range (1,rows+1): 
                if (j == 1 or j == rows): 
                    print ("*",end="") 
                else: 
                    print (end=" ") 
        print() 
  
def printPattern(rows): 
      
    print ("Solid Rhombus:") 
    solidRhombus(rows) 
      
    print("\nHollow Rhombus:") 
    hollowRhombus(rows) 
    
if __name__ == "__main__": 
      
    rows = 5
    printPattern (rows) 