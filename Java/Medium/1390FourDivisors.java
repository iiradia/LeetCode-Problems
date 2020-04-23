class Solution {
    public int sumFourDivisors(int[] nums) {
        int total = 0;
        for (int num : nums)
        {
            
            int summ = 0;
            int j = 0;
        
            for (int i = 1; i < (num/2 + 1); i++)
            {
                if (j > 3)
                {
                    break;
                }
                if (num % i == 0)
                {
                    
                    summ += i;
                    j++;
                }
            }
        
            if (j == 3)
            {
                summ += num;
                total += summ;
            }
            
        }
        
        return total;
            
    }
}