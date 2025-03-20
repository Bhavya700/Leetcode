class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit=set()
        hash_map={ i:[] for i in range(numCourses) }
        for course, pre in prerequisites:
            hash_map[course].append(pre)
        
        def dfs(course):
            if course in visit:
                return False
            
            if hash_map[course]==[]:
                return True
            visit.add(course)
            for pre in hash_map[course]:
                if not dfs(pre):
                    return False
            visit.remove(course)
            hash_map[course]=[]
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
