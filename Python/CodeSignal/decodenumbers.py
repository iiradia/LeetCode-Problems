import sys
for line in sys.stdin:
    
    line = line.strip('\n')
    if line[0] == '0':

        print(0)
        break
    
    arr = [0 for i in range(len(line))]
    arr[0] = 1
    
    for i in range(1, len(line)):
        
        if line[i] != '0':
            arr[i] = arr[i - 1]
           
        
        if line[i - 1] != '0' and int(line[i-1:i+1]) < 27:
            
            if i - 2 >=0 :
                arr[i] += arr[i - 2]
            else:
                arr[i] += 1
       
    print(arr[-1])