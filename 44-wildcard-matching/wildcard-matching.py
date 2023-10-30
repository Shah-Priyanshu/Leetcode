class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s0 = 0
        p0 = 0
        s_star = 0  # Pointer to the position in 's' after the last '*'
        p_star = -1  # Pointer to the position in 'p' when encountering '*'
        
        while s0 < len(s):
            if p0 < len(p) and (p[p0] == s[s0] or p[p0] == '?'):
                s0 += 1
                p0 += 1
            elif p0 < len(p) and p[p0] == '*':
                s_star = s0
                p_star = p0
                p0 += 1
            elif p_star != -1:
                p0 = p_star + 1
                s_star += 1
                s0 = s_star
            else:
                return False
        
        while p0 < len(p) and p[p0] == '*':
            p0 += 1
        
        return p0 == len(p)