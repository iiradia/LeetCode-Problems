import sys
for line in sys.stdin:
    
    """
    ULLRURDD
    
    assume (0,0) is base station
    
    I can use the count of U and match it with D
    I can use the count of R and match it with L
    """
    
    """
    Alternative solution, use python methods
    O(4N) = O(N) solution, each count() operation is O(N)
    
    print(line.count('U') == line.count('D') and line.count('R') == line.count('L'))
    """
    
    """
    O(N) solution, more efficient since only one pass through string
    """
    vertical_counts = [0, 0]
    horizontal_counts = [0, 0]
    
    for char in line:
        if char == 'U':
            vertical_counts[0] += 1
        elif char == 'D':
            vertical_counts[1] += 1
        elif char == 'R':
            horizontal_counts[0] += 1
        elif char == 'L':
            horizontal_counts[1] += 1
       
    print(vertical_counts[0] == vertical_counts[1] and horizontal_counts[0] == horizontal_counts[1])
   