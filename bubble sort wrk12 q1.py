L= [5, 7, 3, 6, 2, 4, 1]
file1=open('BubbleSort3.txt','w')
print("INPUT (initial list): ", L)

exchange = True
n= len(L)
i=0

while (i< n) and  exchange:
    print("BEFORE PASS %d: %s " %(i+1, L))
    exchange = False
    
    for j in range(n-i-1):
        print("%s " %L, end="-> ")
        if L[j] > L[j+1]:
            L[j], L[j+1] = L[j+1], L[j]
            exchange = True
            
        print("%s " %L)
        
    print("AFTER PASS %d: %s " %(i+1, L))
    i=i+1
    
print("OUTPUT (sorted list): ", L)
file1.write(str(L)+'\n')
file1.close()
    
            
        
        
        