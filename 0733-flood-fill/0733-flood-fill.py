

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        r = len(image)
        c = len(image[0])
        i_c = image[sr][sc]
        queue = deque()
        queue.append((sr,sc))

        while len(queue)!= 0:
            i,j = queue.popleft()
            image[i][j] = color
            for x,y in [(0,1),(1,0),(-1,0),(0,-1)]:
                new_i = i+x
                new_j = j+y
                if new_i < 0 or new_i >= r or new_j < 0 or new_j >= c:
                    continue
                if image[new_i][new_j] != i_c:
                    continue
                image[new_i][new_j] = color
                queue.append((new_i,new_j))
        return image
        