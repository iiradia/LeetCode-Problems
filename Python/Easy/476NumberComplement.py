class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        bin_rep = bin(num)
        act_bin = str(bin_rep[bin_rep.index('b')+1:])
        new = [int(2**(len(act_bin)-n-1)) for n in range(len(act_bin)) if act_bin[n] == '0']
        if len(new) == 0:
            return 0
        else:
            return sum(new)