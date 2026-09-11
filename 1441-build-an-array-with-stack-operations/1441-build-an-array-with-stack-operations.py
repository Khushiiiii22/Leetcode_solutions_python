class Solution:

    def buildArray(self, target: List[int], n: int) -> List[str]:
        result =[]
        target_ind = 0

        for i in range(1,n+1):
            if target_ind == len(target):
                break

            if i == target[target_ind]:
                result.append("Push")
                target_ind += 1
            else:
                result.append("Push")
                result.append("Pop")
        return result

        