class Solution:
    def solve(self,index,subset,digits,result):
        char_map = {"2": "abc",
            "3": "def", 
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        if index >= len(digits):
            result.append("".join(subset))
            return
        for ch in char_map[digits[index]]:
            subset.append(ch)
            self.solve(index + 1 , subset,digits,result)
            subset.pop()
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        self.solve(0,[],digits,result)
        return result
        