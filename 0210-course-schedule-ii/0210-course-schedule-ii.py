class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        hash_map = defaultdict(list)
        for course, pre in prerequisites:
            hash_map[course].append(pre)

        
        unvisited, visiting, visited = 0, 1, 2
        states= [unvisited]*numCourses

        def dfs(i):
            if states[i]==visiting:
                return False
            if states[i]==visited:
                return True

            states[i]=visiting

            for pre in hash_map[i]:
                if not dfs(pre):
                    return False
            
            states[i]=visited
            order.append(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return order