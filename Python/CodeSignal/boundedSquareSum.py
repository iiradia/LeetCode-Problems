def boundedSquareSum(a, b, lower, upper):
    ct=0
    
    for i in range(max(len(a),len(b))):
        print(i)
        try:
            sq = a[i]**2
            sq_2 = b[i]**2
        
            if lower < sq+sq_2 < upper:
                ct+=1
        except: pass    
    return ct