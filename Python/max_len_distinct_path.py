# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from extratypes import Tree  # library with types used in the task

def solution(T):
    max_length_arr = [0]
    
    def find_all_paths(node, curr_path):
        
        if node is None or node.x is None:
            return
        
        curr_path = curr_path.copy()
        
        if curr_path.get(node.x) is not None:
            
            curr_max = len(curr_path.keys())
            
            if curr_max > max_length_arr[0]:
                max_length_arr[0] = curr_max
            return
        
        curr_path[node.x] = 1
        
        if node.l is None and node.r is None:
            
            curr_max = len(curr_path.keys())
            
            if curr_max > max_length_arr[0]:
                max_length_arr[0] = curr_max
            return
        
        find_all_paths(node.l, curr_path)
        find_all_paths(node.r, curr_path)
    
    
    find_all_paths(T, {})
    return max_length_arr[0]
