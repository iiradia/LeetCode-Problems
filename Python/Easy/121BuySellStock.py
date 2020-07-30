class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        """
        Algorithm idea
        
        Overcomplicated
        O(n) time complexity
        O(1) space
        """
        
        bought = float('inf')
        sold = float('-inf')
        max_profit = 0
        
        for price in prices:
            
            max_profit = max(sold-bought,max_profit)
            if price < bought:
                bought = price
                sold = float('-inf')
            elif price > sold:
                sold = price
                max_profit = max(sold-bought,max_profit)
        
        max_profit = max(sold-bought,max_profit)
        
        return max_profit
    
        """
        Shorter algorithm, same efficiency
        
        O(n) time complexity
        O(1) space
        """
        """
        max_profit = 0
        min_value = float('inf')
        
        for price in prices:
            
            if price < min_value:
                min_value = price
            
            else:
                max_profit = max(max_profit, price-min_value)
        
        return max_profit
        
        """