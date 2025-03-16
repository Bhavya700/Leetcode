from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visit=set()
        keys=deque()
        visit.add(0)
        keys.append(0)
        while keys:
            a=keys.popleft()
            for b in rooms[a]:
                if b not in visit and b>0:
                    keys.append(b)
                    visit.add(b)

        if len(visit) == len(rooms):
            return True

        else:
            return False
