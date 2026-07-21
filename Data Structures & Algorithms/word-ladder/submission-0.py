class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dictionary = wordList
        dictionary_set = set(dictionary)
        start, end = beginWord, endWord
        if end not in dictionary_set:
            return 0 

        if start == end:
            return 1
        
        lower_case_alphabet = 'abcedfghijklmnopqrstuvwxyz'
        queue = deque([start])
        visited = set([start])
        dist = 0 

        while queue:
            for _ in range(len(queue)):
                curr_word = queue.popleft()

                if curr_word == end:
                    return dist + 1
                
                for i in range(len(curr_word)):
                    for c in lower_case_alphabet:
                        next_word = curr_word[:i] + c + curr_word[i+1:]

                        if(next_word in dictionary_set and next_word not in visited):
                            visited.add(next_word)
                            queue.append(next_word)
            dist += 1
        return 0 