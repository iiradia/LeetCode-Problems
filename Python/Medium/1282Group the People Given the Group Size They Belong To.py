class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        num_groups = 0
        group_idx = []
        
        groups = [[i] * groupSizes.count(i) for i in set(groupSizes)]
        
        for num in groups:
            
            new_group = []
            
            if len(num) != num[0]:
                
                lg_factor = len(num) / num[0]
                
                while len(new_group) < num[0]:
                    for id in range(len(groupSizes)):
                         if groupSizes[id] == num[0]:
                            new_group.append(id)
                    
                for i in range(lg_factor):
                    b = new_group[i::lg_factor]
                    group_idx.append(b)
    
            
            else:
                for idx in range(len(groupSizes)):
                    if groupSizes[idx] == num[0]:
                        new_group.append(idx)
                group_idx.append(new_group)
            
        return group_idx