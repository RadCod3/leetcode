class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        i = j = 0
        s_ = []
        t_ = []
        while i < n and j < m:
            if s[i] == "#":
                if len(s_) != 0:
                    s_.pop()
            else:
                s_.append(s[i])
            if t[j] == "#":
                if len(t_) != 0:
                    t_.pop()
            else:
                t_.append(t[j])
            i += 1
            j += 1

        while i < n:
            if s[i] == "#":
                if len(s_) != 0:
                    s_.pop()
            else:
                s_.append(s[i])
            i += 1
        while j < m:
            if t[j] == "#":
                if len(t_) != 0:
                    t_.pop()
            else:
                t_.append(t[j])
            j += 1

        return s_ == t_


sol = Solution()
s = "y#fo##f"
t = "y#f#o##f"
print(sol.backspaceCompare(s, t))
