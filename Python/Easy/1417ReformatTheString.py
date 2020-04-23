from itertools import zip_longest
class Solution(object):
    def reformat(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s
        digits = 0
        lets  = 0
        list_fix = []
        str_fix = []
        for ch in s:
            if str.isdigit(str(ch)):
                digits+=1
                list_fix.append(str(ch))
            else:
                lets+=1
                str_fix.append(str(ch))
        
        if lets == digits or abs(lets-digits) < 2:
            ret_list = []
            i=0
            for a,b in zip_longest(list_fix,str_fix):
                if a != None and b != None:
                    ret_list.append(str(b) + str(a))
                elif a == None:
                    if str.isdigit(str(b)) == str.isdigit(''.join(ret_list)[len(''.join(ret_list))-1]):
                        ret_list.insert(0, str(b))
                    else:
                        ret_list.append(str(b))
                elif b == None:
                    if str.isdigit(str(a)) == str.isdigit(''.join(ret_list)[len(''.join(ret_list))-1]):
                        print(''.join(ret_list)[i-1])
                        ret_list.insert(0, str(a))
                    else:
                        ret_list.append(str(a))
                i+=1
            return (''.join(ret_list))
        else:
            return ''