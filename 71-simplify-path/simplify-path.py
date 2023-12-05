class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        components = [comp for comp in path.split('/') if comp and comp != '.']

        stack = []
        for comp in components:
            if comp == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(comp)

        simplified_path = '/' + '/'.join(stack)
        return simplified_path