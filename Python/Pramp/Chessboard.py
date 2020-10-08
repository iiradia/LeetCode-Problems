import sys
for line in sys.stdin:
    
    if len(line.strip()) != 2:
        print('Error')
        break
    
    """
    a1 -> Black
    a2 -> White
    b1 -> White
    b2 -> Black
    """
    
    # if column character has even ascii, use 1st strategy
    if ord(line[0]) % 2 == 0:
        
        # if row is even, print black
        if int(line[1]) % 2 == 0:
            print('Black')
        else:
            print('White')
            
    # if column character has odd ascii, use opposite strategy
    else:
        
        # if row is even, print white
        if int(line[1]) % 2 == 0:
            print('White')
        else:
            print('Black')