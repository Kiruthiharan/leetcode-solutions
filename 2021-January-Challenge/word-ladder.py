from collections import defaultdict
import collections
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        length = len(beginWord)
        all_combo = defaultdict(list)
        for item in wordList:
            for i in range(length):
                all_combo[item[:i] + "*" + item[i+1:]].append(item)
        
        
        queue = collections.deque([(beginWord, 1)])
        visited = {beginWord: True}
        while queue:
            current, level = queue.popleft()
            for i in range(length):
                intermediate = current[:i] + "*" + current[i+1:]
                for word in all_combo[intermediate]:
                    if(word == endWord):
                        return level + 1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                all_combo[intermediate] = []
        return 0
                    
            
        