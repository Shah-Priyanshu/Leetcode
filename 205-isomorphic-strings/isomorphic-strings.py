class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # Two dictionaries to hold the mappings from s to t and t to s
        map_s_to_t = {}
        map_t_to_s = {}
        
        for char_s, char_t in zip(s, t):
            if char_s in map_s_to_t:
                # Check if current mapping is consistent with previous mappings
                if map_s_to_t[char_s] != char_t:
                    return False
            else:
                # Ensure no two characters map to the same character in 't'
                if char_t in map_t_to_s:
                    return False
                map_s_to_t[char_s] = char_t
                map_t_to_s[char_t] = char_s
                
        return True
