class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R=[]
        D=[]
        n=len(senate)
        for i in range(n):
            if senate[i]=="R":
                R.append(i)
            elif senate[i]=="D":
                D.append(i)
        while R and D:
            r=R.pop(0)
            d=D.pop(0)
            if r<d:
                R.append(n+d)
            else:
                D.append(n+d)

        return "Radiant" if R else "Dire"