class Solution(object):

    map = {}

    def isScramble(self, s1, s2):
        n = len(s1)

        if s1 == s2:
            return True

        a = defaultdict(int)
        b = defaultdict(int)
        c = defaultdict(int)

        if (s1 + s2) in self.map:
            return self.map[s1 + s2]

        for i in range(1, n):
            j = n - i

            a[s1[i - 1]] += 1
            b[s2[i - 1]] += 1
            c[s2[j]] += 1

            if a == b and self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                self.map[s1 + s2] = True
                return True

            if a == c and self.isScramble(s1[:i], s2[j:]) and self.isScramble(s1[i:], s2[:j]):
                self.map[s1 + s2] = True
                return True

        self.map[s1 + s2] = False

        return False 