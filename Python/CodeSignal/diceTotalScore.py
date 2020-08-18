def diceTotalScore(a, b, c):

    if a == b or a == c:
        if b == c:  
            return 1000 * a
        
        return 500 * a
            
    elif b == c:
        return 500 * b
    
    else:
        return 100 * min(a, b, c)