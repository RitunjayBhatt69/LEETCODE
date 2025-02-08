class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Get the lengths of the input string and pattern
        m, n = len(s), len(p)
        
        # Create a 2D DP table initialized with False
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Empty string matches with an empty pattern
        dp[0][0] = True
        
        # Handle cases where pattern contains '*' that can match zero preceding element
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]  # '*' can eliminate the preceding character
        
        # Fill the DP table
        for i in range(1, m + 1):  # Iterate over string
            for j in range(1, n + 1):  # Iterate over pattern
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    # If characters match or pattern has '.', take diagonal value
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # '*' can either:
                    # 1. Ignore the previous character (dp[i][j - 2])
                    # 2. Consider previous character if it matches current character (dp[i - 1][j])
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
        
        # Return whether the entire string matches the pattern
        return dp[m][n]

# Example test cases
sol = Solution()
print(sol.isMatch("aa", "a"))  # Output: False
print(sol.isMatch("aa", "a*")) # Output: True
print(sol.isMatch("ab", ".*")) # Output: True
