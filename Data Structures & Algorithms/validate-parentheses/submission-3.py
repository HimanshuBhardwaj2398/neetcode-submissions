class Solution:
    def isValid(self, s: str) -> bool:
        pairs=["[]","{}","()"]

        while True: 
            for i in range(len(s)-1):
                if s[i:i+2] in pairs:
                    s=s[:i]+s[i+2:]
                    break
            else:
                return s==""
        