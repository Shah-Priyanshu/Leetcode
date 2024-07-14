from collections import defaultdict

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def parse():
            N = len(formula)
            stack = [defaultdict(int)]
            i = 0
            
            while i < N:
                if formula[i] == '(':
                    stack.append(defaultdict(int))
                    i += 1
                elif formula[i] == ')':
                    top = stack.pop()
                    i += 1
                    start = i
                    while i < N and formula[i].isdigit():
                        i += 1
                    multiplicity = int(formula[start:i] or 1)
                    for elem, count in top.items():
                        stack[-1][elem] += count * multiplicity
                else:
                    start = i
                    i += 1
                    while i < N and formula[i].islower():
                        i += 1
                    elem = formula[start:i]
                    start = i
                    while i < N and formula[i].isdigit():
                        i += 1
                    count = int(formula[start:i] or 1)
                    stack[-1][elem] += count
            
            return stack[0]
        
        count = parse()
        return ''.join(f"{elem}{(count[elem] if count[elem] > 1 else '')}" for elem in sorted(count))