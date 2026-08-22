class Solution:
    def checkDivisibility(self, n: int) -> bool:
        temp = n
        sum = 0 

        product = 1
        while n>0:
            ld = n % 10


            sum += ld
            product *= ld
            n //= 10

        if temp %(sum + product) == 0:
            return True
        else:
            return False

        