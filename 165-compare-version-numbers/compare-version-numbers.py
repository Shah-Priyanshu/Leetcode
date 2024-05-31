class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Split the version strings by '.'
        v1_revisions = version1.split('.')
        v2_revisions = version2.split('.')
        
        # Determine the maximum length of the revisions lists
        max_length = max(len(v1_revisions), len(v2_revisions))
        
        # Compare corresponding revisions
        for i in range(max_length):
            # Get the current revision for each version, default to 0 if out of bounds
            v1_revision = int(v1_revisions[i]) if i < len(v1_revisions) else 0
            v2_revision = int(v2_revisions[i]) if i < len(v2_revisions) else 0
            
            # Compare the current revisions
            if v1_revision < v2_revision:
                return -1
            elif v1_revision > v2_revision:
                return 1
        
        # If all revisions are equal, return 0
        return 0
