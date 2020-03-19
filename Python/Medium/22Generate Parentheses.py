class Solution:
    def generateParenthesis(self, n):
        
        base_parentheses = "()" * n
        count_valid_swaps = 100
        all_valid = [base_parentheses]
      
        while count_valid_swaps > 0:
            
            count_valid_swaps = 0
            
            for base_parentheses in all_valid:
                for ch in range(len(base_parentheses)):
              
                    if (ch < len(base_parentheses)-1):
                        lst = list(base_parentheses)
                        lst[ch], lst[ch+1] = lst[ch+1], lst[ch]
                        new_parentheses =  ''.join(lst)
                       
                        len_new = len(new_parentheses)
                        condition1 = new_parentheses[len_new-1] != "("
                        condition2 = new_parentheses[0] != ")"
                        condition3 = len([i for i in range(ch) if new_parentheses[ch] == ")"]) <= len([i for i in range(ch) if new_parentheses[ch]=="("])

                        if (condition1 & condition2 & condition3 and not new_parentheses == base_parentheses):

                            count_valid_swaps += 1
                            all_valid.append(new_parentheses)
                            print(all_valid)
                    
                    if (len(all_valid) > 2): 
                        break
            if (count_valid_swaps == 0 or len(all_valid)>2):
                break
        return all_valid

s = Solution()
print(s.generateParenthesis(2)) 
        