class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def dictrize(s: str):
            mydict = {}
            for char in s:
                if char in mydict:
                    mydict[char] += 1
                else:
                    mydict[char] = 1
            return mydict

        if len(s) != len(t):
            return False
        s_dict = dictrize(s)

        for char in t:
            if char not in s_dict or s_dict[char] == 0:
                return False
            else:
                s_dict[char] -= 1
        return True


sol = Solution()
print(sol.isAnagram("anagram", "nagaram"))
