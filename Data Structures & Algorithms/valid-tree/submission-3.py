class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        - basically we are checking if there are no cycles
        - have a visited array, True or False
        - have the edges in a list of sets
        """
        

        seen = set()
        all_edges = [set() for _ in range(n)]
        for start, end in edges:
            all_edges[start].add(end)
            all_edges[end].add(start)
        def dfs(prev, start):
            if start in seen:
                return False
            seen.add(start)
            for neighbor in all_edges[start]:
                if neighbor == prev:
                    continue
                val = dfs(start, neighbor)
                if not val:
                    return False
            return True
        return dfs(0, 0) and len(seen) == n
        
        


        