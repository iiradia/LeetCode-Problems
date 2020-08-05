def isToeplitz(arr):
  """
  [[1,2,3,4],
  [5,1,2,3],
  [6,5,1,2]]
  
  I have to go through the first row 
  and the first column
  
  go through each element
    - check its diagonal for validity
  
  arr[0][0] = 1 -> first row
  
  arr[1][1] = 1 good
  arr[2][2] = 1 good
  
  arr[0][1] = 2 -> first row
  
  arr[1][2] = 2 good
  arr[2][3] = 2 good
  
  In matrices, it's often O(m*n) where m is #rows and n is #columns
  """
  
  def check_diagonal_validity(arr, row, col):
    
    while row<len(arr)-1 and col<len(arr[row])-1:
      element_value = arr[row][col]
      row+=1
      col+=1 
      if element_value != arr[row][col]:
        return False
    
    return True
  
  if len(arr) < 1:
    return True
  
  for index in range(len(arr[0])):
    
    if not check_diagonal_validity(arr, 0, index):
      return False
  
  for row in range(1,len(arr)):
    
    if not check_diagonal_validity(arr, row, 0):
      return False
    
  return True
  
	#your code goes here

print(isToeplitz([[1,2,3,4,5],
                  [5,1,2,3,5],
                  [6,5,1,2,1]]))