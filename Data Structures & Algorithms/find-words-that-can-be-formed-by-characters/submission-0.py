class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        char_count = Counter(chars)
        total_len = 0 
        for word in words:
            check = True 
            curr = Counter(word)
            for c in curr:
                if char_count[c] < curr[c]:
                    check = False 
                    break 
                
            if check:
                total_len += len(word)
        return total_len