class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        seen = set(wordList)
        if endWord not in seen:
            return 0 
        queue = deque()
        queue.append((beginWord,1))
        while len(queue) != 0:
            curr , level = queue.popleft()
            if curr == endWord:
                return level
            for i in range(0,len(curr)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    if ch == curr[i]:
                        continue
                    new_word = curr[:i] + ch + curr[i+1:]
                    if new_word in seen:
                        queue.append((new_word,level+1))
                        seen.remove(new_word)
        return 0                       
        