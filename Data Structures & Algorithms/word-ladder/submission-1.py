class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dictionary_set = set(wordList)
        if endWord not in dictionary_set:
            return 0 
        
        if beginWord == endWord:
            return 1
        
        start_queue = deque([beginWord])
        start_visited = {beginWord}
        end_queue = deque([endWord])
        end_visited = {endWord}
        level_start = level_end = 0 

        while start_queue and end_queue:
            level_start += 1
            if explore_level(start_queue, start_visited, end_visited, dictionary_set):
                return level_start + level_end + 1
            
            level_end += 1
            if explore_level(end_queue, end_visited, start_visited, dictionary_set):
                return level_start + level_end + 1 
        return  0 
    
def explore_level(queue, visited, other_visited, dictionary_set):
    lower_case = 'abcdefghijklmnopqrstuvwxyz'
    for _ in range(len(queue)):
        word = queue.popleft()
        for i in range(len(word)):
            for c in lower_case:
                new_word = word[:i] + c + word[i+1:]

                if new_word in other_visited:
                    return True 

                if new_word in dictionary_set and new_word not in visited:
                    queue.append(new_word)
                    visited.add(new_word)
    
    return False 