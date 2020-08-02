class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        
        if k == 1:
            return max(arr[0],arr[1])
        if k > len(arr):
            return max(arr)
    
        consecutive_wins = 1
        winner = float('-inf')
        
        
        while consecutive_wins < k:
            past_winner = winner
            winner = max(arr[0],arr[1])
            arr.append(arr.pop(arr.index(min(arr[0],arr[1]))))
            if winner == past_winner:
                consecutive_wins += 1
            else:
                consecutive_wins = 1
                
        return winner
        