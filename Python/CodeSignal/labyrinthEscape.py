def labyrinthEscape(n, m, obstacles, teleports):
    
    matrix = [[i for i in range(m)]] * n
    
    teleport_idx = []
    teleport_end = []
     
    for i in teleports:
        
        teleport_idx.append([i[0], i[1]])
        teleport_end.append([i[2], i[3]])
    
    
    possible = True
    i = 0 
    j = 0
    moves = 0
    max_moves = len(matrix) * len(matrix[0])
    
    past_i = -1
    past_j = -1
    
    while possible:
        
        if moves > max_moves: 
            return False
        
        if i == len(matrix)-1 and j == len(matrix[0])-1:
            return True
        
        if [i,j] in teleport_idx:
            
            idx = teleport_idx.index([i,j])
            i = teleport_end[idx][0]
            j = teleport_end[idx][1]
        
        if [i, j+1] in obstacles:
            return False
        
        j += 1
        moves += 1
        
        if past_i == i and past_j == j:
            return False
        
        past_i = i
        past_j = j
    
    return False
