# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    
    """
    [
        [1], -> iteration 1
        [3], -> iteration 2
        [5], -> iteration 3
        [7], -> iteration 4
        [9], -> iteration 5
        [1,3], -> iteration 2
        [1,5], -> iteration 3
        [1,7], -> iteration 4
        [1,9], -> iteration 5
        [3,5], -> iteration 3
        [3,7], -> iteration 4
        [1,3,5], -> iteration 3
        [1,3,7] -> iteration 4
        
        [1], [3], [1,3], [5], [1,5], [1,3,5], [7], [1,7], [1,3,7], [1,3,5,7]
    ]
    """
    decomps = []
    rem = []
    
    # only iterate through odd
    for i in range(1,N,2):

        # append the number itself
        decomps.append([i, 1, [i]])
        
        # go through each decom
        for idx, comp in enumerate(decomps):
            
            # if it is possible to add the decomp to the current number that was just added, add it
            if N - comp[0] - i >= 0 and comp[0] != i and i not in comp[2]:
                
                new_comp = comp[2] + [i]
                
                # [1] + [7] = [1,7], [3] + [7] = [3,7], [1,3] + [7] = [1,3,7], [5] 
                decomps.append([comp[0]+i, comp[1]+1, new_comp])
    
    ret = [N] 
    
    for comp in decomps:
        
        # verify that this is the longest one and has proper sum
        if comp[0] == N and comp[1] > len(ret):
            ret = comp[2]
    
    return ret

