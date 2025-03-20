class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        hash = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in hash:
              
                if st and st[-1] == hash[char]:
                    st.pop() 
                else:
                    return False
            else:
                st.append(char)
        
        
        return not st

            