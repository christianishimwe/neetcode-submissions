class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        - have a list of list, an index says a course, and its neigbors are course you 
        should take after this course
        - have another list where index is node, and element is its indegree
        - have a set to keep track of nodes we have seen before
        - have a deque to keep track of nodes with 0 incoming links
        - popleft on the deque, from this node, check its neigbors (if you saw this before, doom) and reduce their indegree
        - if the indegree becomes 0, append it to the deque

        """
        graph = [set() for _ in range(numCourses)]
        seen_counts = 0
        pivots = deque()
        indegrees = [0 for _ in range(numCourses)]
        for second, first in prerequisites:
            graph[first].add(second)
            indegrees[second] += 1
        # get all the zero indegrees
        for course in range(numCourses):
            if indegrees[course] == 0:
                pivots.append(course)
        while pivots:
            course = pivots.popleft()
            seen_counts += 1
            for neighbor in graph[course]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    pivots.append(neighbor)
        if seen_counts < numCourses:
            return False
        return True

