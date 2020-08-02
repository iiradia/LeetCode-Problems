class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        store_idxs = {}
        
        for i in range(len(nums)):
            curr=nums[i]
            
            if store_idxs.get(curr) is not None:
                if abs(store_idxs[curr]-i) <= k:
                    return True
            
            store_idxs[curr] = i
            
        return False