def find_pairs_with_given_difference(arr, k):
  
  """
  k = 1
  [0, -1, -2, 2, 1] 
  0       
  arr = [[1,0], [0, -1], [-1, -2], [2, 1]]
  {
     -1: 0,
     -2: -1,
     1: 2,
     0: 1
     
  }
  """
  
  # loop to create hashmap
  array_pairs = []
 
  matching_pairs = {}
  
  for num in arr:
    
    pair = num - k
    
    matching_pairs[pair] = num
 
  # loop to create pairs
  for num in arr:
    
    if matching_pairs.get(num) is not None:
      
      array_pairs.append([matching_pairs[num], num])
   
  return array_pairs