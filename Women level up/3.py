def FindMinMax(ls=[ ]):
    i=0
    maximum=0
    while (i<len(ls)):
        
        if ls[i]>maximum:
            maximum=ls[i]
        i+=1
    MinMax=[maximum]
    
    
    
    minimum=ls[0]
    while (i<len(ls)): 
        if ls[i]<minimum:
            minimum=ls[i]
        i+=1   
    
    MinMax.append(minimum)
    print (MinMax)
    
       
FindMinMax(ls=[1,5,3,7,66])
