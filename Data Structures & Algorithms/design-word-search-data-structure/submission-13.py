class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False 

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()    

    def addWord(self, word: str) -> None:
        node = self.root 

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isWord = True 

    def search(self, word: str) -> bool:
        
        def search_in(node, idx):
            if idx == len(word):
                return node.isWord
            
            for i in range(idx, len(word)):
                if word[i] == '.':
                    for n in node.children:
                        if(search_in(node.children[n], i+1)):
                            return True 
                else:
                    if word[i] not in node.children:
                        return False
                    node = node.children[word[i]] 
            return node.isWord
        return search_in(self.root, 0)


            
