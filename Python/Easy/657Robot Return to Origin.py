class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        current_pos = [0, 0]
        for ch in moves:
            
            if ch == "U":
                current_pos[1]+=1
            elif ch == "D":
                current_pos[1]-=1
            elif ch == "L":
                current_pos[0]-=1
            elif ch == "R":
                current_pos[0]+=1
        
        if current_pos[0] == 0 and current_pos[1] == 0:
            return True
        
        return False
            