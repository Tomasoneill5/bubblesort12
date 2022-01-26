def bubbleSort(L, boolean=False, dbg=False):
    L= [5, 7, 3, 6, 2, 4, 1]
    if dbg==True:
        print('open file')
        file1=open('Log4.txt','w')    
        file1.write("INPUT (initial list): "+ str(L))
    
    exchange = True
    n= len(L)
    i=0

    while (i< n) and  exchange:
        if dbg==True:
            file1.write('\n'+"BEFORE PASS:"+ str(i+1)+str(L))
        exchange = False
        
        for j in range(n-i-1):
            if dbg==True:
                file1.write('\n'+"%s "+str(L)+"-> ")
            if boolean== True:  
                if L[j] > L[j+1]:
                    L[j], L[j+1] = L[j+1], L[j]
                    exchange = True
            else:
                if L[j] < L[j+1]:
                    L[j], L[j+1] = L[j+1], L[j]
                    exchange = True
            if dbg==True:
                file1.write('\n'+"%s "+ str(L))
        if dbg==True:    
            file1.write('\n'+"AFTER PASS: "+str(i+1)+str(L))
        i=i+1
    if dbg==True:    
        file1.write('\n'+"OUTPUT (sorted list): "+str(L))
        file1.write('\n'+str(L)+'\n')
        file1.close()
W= [5, 7, 3, 6, 2, 4, 1]
bubbleSort(W, dbg=True)