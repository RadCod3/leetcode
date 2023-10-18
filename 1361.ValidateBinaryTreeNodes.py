from typing import List


class SolutionOld:
    def validateBinaryTreeNodes(
        self, n: int, leftChild: List[int], rightChild: List[int]
    ) -> bool:
        class DSU:
            def __init__(self, arg_data, arg_rank):
                self.rank = arg_rank
                self.data = arg_data
                self.parent = self
                print("Created set : " + str(arg_data) + " Rank : " + str(arg_rank))

        # FindParent applies path compression to all the nodes in the search path of the parent
        # without changing their ranks.
        def FindParent(s: DSU):
            if s.data != s.parent.data:
                s.parent = FindParent((s.parent))
            return s.parent

        # Merge operation makes use of heuristic union-by-rank.
        def Merge(a: DSU, b: DSU):
            parent_of_a = FindParent(a)
            parent_of_b = FindParent(b)

            if parent_of_a.data != parent_of_b.data:
                if a.rank < b.rank:
                    a.parent = parent_of_b
                    b.rank += 1
                else:
                    b.parent = parent_of_a
                    a.rank += 1

        class Graph:
            def __init__(self, n):
                self.n = n
                self.edges = [set() for _ in range(n)]
                self.visited = [False] * n
                self.parents = [-1 for i in range(n)]
                self.sets = [DSU(i, 0) for i in range(n)]
                self.edge_n = 0

            def add_edge(self, u, v):
                if u in self.edges[v]:
                    return False
                if FindParent(self.sets[u]) == FindParent(self.sets[v]):
                    return False
                Merge(self.sets[u], self.sets[v])
                self.edges[u].add(v)
                if self.parents[v] != -1:
                    return False
                self.parents[v] = u
                self.edge_n += 1
                return True

        g = Graph(n)

        for i in range(n):
            if leftChild[i] != -1:
                no_error = g.add_edge(i, leftChild[i])
                if not no_error:
                    return False
            if rightChild[i] != -1:
                no_error = g.add_edge(i, rightChild[i])
                if not no_error:
                    return False
        if g.edge_n != n - 1:
            return False
        no_p = g.parents.count(-1)
        if no_p != 1:
            return False
        else:
            return True
        # found = False
        # for i in range(n):
        #     temp = g.dfs(i) and all(g.visited)
        #     if temp and found:
        #         return False
        #     if temp and not found:
        #         found = True
        #     g.visited = [False] * n
        # return found


class Solution:
    def validateBinaryTreeNodes(
        self, n: int, leftChild: List[int], rightChild: List[int]
    ) -> bool:
        class Graph:
            def __init__(self, n):
                self.n = n
                self.edges = [[] for _ in range(n)]
                self.visited = [False] * n
                self.indegree = [0 for i in range(n)]

            def add_edge(self, u, v):
                self.edges[u].append(v)
                self.indegree[v] += 1

            def dfs(self, u):
                if self.visited[u]:
                    return False
                self.visited[u] = True
                for v in self.edges[u]:
                    if not self.dfs(v):
                        return False
                return True

        g = Graph(n)

        for i in range(n):
            if leftChild[i] != -1:
                g.add_edge(i, leftChild[i])
            if rightChild[i] != -1:
                g.add_edge(i, rightChild[i])

        root_candidates = [node for node in range(n) if g.indegree[node] == 0]
        if len(root_candidates) != 1:
            return False
        root = root_candidates[0]
        if not g.dfs(root):
            return False
        return all(g.visited)


sol = Solution()
print(
    sol.validateBinaryTreeNodes(
        n=4, leftChild=[1, 0, 3, -1], rightChild=[-1, -1, -1, -1]
    )
)
