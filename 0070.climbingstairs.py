from functools import lru_cache


# Memoization
def climbStairs(n: int) -> int:
    @lru_cache(maxsize=None)
    def recClimbStairs(i):
        if i == n:
            return 1
        if i > n:
            return 0
        return recClimbStairs(i + 1) + recClimbStairs(i + 2)

    return recClimbStairs(0)


# DP
def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    dp = [0] * (n + 1)
    dp[n - 1] = 1
    dp[n - 2] = 2
    for i in reversed(range(n - 2)):
        dp[i] = dp[i + 1] + dp[i + 2]
    return dp[0]


# DP_v2
def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    n_1 = 1
    n_2 = 2
    for _ in reversed(range(n - 2)):
        n_2 = n_2 + n_1
        n_1 = n_2 - n_1
    return n_2


print(climbStairs(3))
