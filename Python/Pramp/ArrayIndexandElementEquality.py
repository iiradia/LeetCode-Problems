def index_equals_value_search(arr):
  
  """
  [-8, 0, 2, 5]
          ^
   -8 == 0 -> False
   0 = 1 -> False
   2 = 2 -> True
   
   break
   
   [-8, 0, 1, 3, 5]
           ^
  
  [0, 1, 2, 3, 4]
    
    
  1. low, mid, high
  2. while low < high:
       if mid < index:
          low = mid
       elif mid > index:
           high = mid
           
       adjust midpoint
  """ 
  
  low = 0
  high = len(arr)-1
  mid = int((low + high)/2.0)
  answer = -1
  
  
  while low < high:
    
    value = arr[mid]
    if value < mid:
      low = mid
    elif value > mid:
      high = mid
    else:
      answer = mid
      high = mid
    
    mid = int((low + high)/2.0)
  
  return answer
  
  
print(index_equals_value_search([-1,0,3,6])) 
 