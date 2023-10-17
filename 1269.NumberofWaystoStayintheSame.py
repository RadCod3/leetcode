from functools import cache


class Solution:
    # My initial solution always made all possible moves and
    # returned 0 when i < 0 i >= arrLen and steps == 0. Just
    # a basic bruteforce method with optimization.
    def numWaysOld(self, steps: int, arrLen: int) -> int:
        @cache
        def numWaysRec(i, steps):
            if i == 0 and steps == 0:
                return 1
            if i < 0 or i >= arrLen or steps == 0:
                return 0
            move_l = numWaysRec(i - 1, steps - 1)
            move_r = numWaysRec(i + 1, steps - 1)
            no_move = numWaysRec(i, steps - 1)

            return (move_l + move_r + no_move) % (10**9 + 7)

        return numWaysRec(0, steps)

    # Solution was optimized based on the observation that we only
    # find a possible set of moves only if i <= steps. Because if you
    # are in i=5 and you have 3 steps remaining there is no point
    # in moving to the left let alone right or staying still
    # as none of those moves will get you back to the initial
    # position before running out of steps. By checking those
    # conditions for each move we manage to optimize the function
    # a lot more.
    def numWays(self, steps: int, arrLen: int) -> int:
        @cache
        def numWaysRec(i, steps):
            if i == 0 and steps == 0:
                return 1

            res = 0

            # Only move to the left if you have i or more steps.
            # You need this amount of step in order to get to i=0
            # without running out of steps.
            if i > 0 and steps >= i:
                res += numWaysRec(i - 1, steps - 1)

            # Only move to the right if you have i+2 or more steps
            # Ex. You are in i = 4 and you have 5 steps. You move to
            # i = 5 and now you have only 4 steps. This means you
            # would never be able to reach i = 0. Hence we only move
            # to the right if we have enough steps to get back to  i = 0.
            if i + 1 < arrLen and steps >= i + 2:
                res += numWaysRec(i + 1, steps - 1)

            # Only stay still if you have steps to spare
            if steps - 1 >= i:
                res += numWaysRec(i, steps - 1)

            return res % (10**9 + 7)

        return numWaysRec(0, steps)


sol = Solution()
print(sol.numWays(4, 2))
