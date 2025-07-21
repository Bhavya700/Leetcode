class Solution:
    def isValid(self, word: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        if len(word)<3:
            return False
        v=False
        c=False
        for i in word:    
            if i.isalnum():
                if c and v:
                    continue
                else:
                    if not i.isdigit():
                        if i not in vowels:
                            c=True
                        else:
                            v=True
            else:
                return False      

        if c and v:
            print("end")
            return True
        return False               
