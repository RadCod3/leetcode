from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        if m < n:
            return ""
        if m == n and m == 1:
            return s if s == t else ""

        def dictrize(s: str):
            s_dict = {}
            for char in s:
                if char in s_dict:
                    s_dict[char] += 1
                    continue
                s_dict[char] = 1
            return s_dict

        t_dict = dictrize(t)
        curr_min = float("inf")
        curr_min_idx = None
        c_counts = defaultdict(int)
        c_have = 0
        c_need = len(t_dict)
        l = 0

        while l < m and not s[l] in t_dict:
            l += 1
        r = l

        while r < m:
            c = s[r]
            if not c in t_dict:
                r += 1
                continue

            c_counts[c] += 1
            if t_dict[c] == c_counts[c]:
                c_have += 1

            while l <= r and c_have >= c_need:
                if r - l + 1 < curr_min:
                    curr_min = r - l + 1
                    curr_min_idx = l
                if s[l] in t_dict:
                    c_counts[s[l]] -= 1
                    if t_dict[s[l]] > c_counts[s[l]]:
                        c_have -= 1
                l += 1

            r += 1

        if curr_min_idx is None:
            return ""

        return s[curr_min_idx : curr_min_idx + curr_min]


sol = Solution()
print(sol.minWindow("ADOBECODEBANC", "ABC"))  # "BANC"
print(sol.minWindow("a", "aa"))  # ""
print(sol.minWindow("a", "a"))  # "a"
print(sol.minWindow("aa", "aa"))  # "aa"
print(sol.minWindow("ab", "A"))  # "b"
print(sol.minWindow("ANAGRAMSAREEASY", "AAS"))  # "AMSA"
