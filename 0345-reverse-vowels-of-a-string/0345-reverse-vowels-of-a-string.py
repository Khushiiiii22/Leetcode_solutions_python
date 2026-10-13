class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0 
        right = len(s) - 1
        char = list(s)
        vowels = "aeiouAEIOU"

        while left < right:
            if char[left]  not in  vowels:
                left += 1
            elif char[right] not in vowels:
                right -= 1

            else:
                char[left], char[right] = char[right] , char[left]
                left += 1
                right -= 1


            
        return "".join(char)
        