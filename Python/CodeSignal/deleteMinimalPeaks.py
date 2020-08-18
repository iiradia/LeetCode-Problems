def deleteMinimalPeaks(numbers):

    """
    [2, 7, 8, 5, 1, 6, 3, 9, 4]
    
    find_peaks
    while peaks exist, remove minimal peaks

    TODO:
        - finish implementation
    """
    
    def find_peaks(numbers):
        peaks=[]
        for idx, num in enumerate(numbers):
            peak = True
            if idx > 0:
                if num < numbers[idx-1]:
                    peak = False
            
            if idx < len(numbers)-1:
                if num < numbers[idx+1]:
                    peak = False 
            
            if peak:
                peaks.append(num)
            
        return peaks
    
    new_nums = numbers.copy()
    deleted = []
    
    while len(new_nums) > 0:
        
        peaks = sorted(find_peaks(new_nums))
        
        for num in peaks:
            new_nums.remove(num)
            peaks.remove(num)
            deleted.append(num)
            
            peaks = sorted(find_peaks(new_nums))
    
    return deleted
        
        
            