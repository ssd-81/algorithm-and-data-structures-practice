class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word)->None:
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c] 
        node.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        rows, cols = len(board), len(board[0])

        for word in words:
            root.addWord(word)
        
        res = set()
        visit = set()
        
        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in visit or board[r][c] not in node.children):
                return 
            
            word += board[r][c] 
            node = node.children[board[r][c]]
            if node.isWord:
                res.add(word)
            
            visit.add((r,c))

            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)

            visit.remove((r,c))
        for r in range(rows):
            for c in range(cols):
                dfs(r,c, root, "")
        return list(res) 