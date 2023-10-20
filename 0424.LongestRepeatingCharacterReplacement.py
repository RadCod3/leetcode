class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def max_occuring_char(count: dict):
            max_count = 0
            for c in count:
                if count[c] > max_count:
                    max_count = count[c]
            return max_count

        counts = {}
        n = len(s)
        l = 0
        r = 0
        curr_max = 0
        r_changed = True
        while r < n:
            if r_changed:
                counts[s[r]] = 1 + counts.get([s[r]], 0)
            max_char_count = max_occuring_char(counts)
            if r - l + 1 - max_char_count <= k:
                curr_max = max(r - l + 1, curr_max)
                r += 1
                r_changed = True
            else:
                counts[s[l]] -= 1
                l += 1
                r_changed = False
        return curr_max


sol = Solution()
# print(sol.characterReplacement("ABAB", 2))
print(sol.characterReplacement("AABABBA", 1))
