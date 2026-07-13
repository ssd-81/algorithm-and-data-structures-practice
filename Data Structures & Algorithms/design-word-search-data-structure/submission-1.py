class TrieNode:
    def __init__(self, val=0):
        self.val = val 
        self.is_word = False 
        self.children = {}


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root 

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode(c)
            node = node.children[c] 
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self.root 
        def sub_search(word, node)->bool:
            for c in word:
                if c == '.':
                    for child in node.children:
                        if sub_search(word[1:], node.children[child]):
                            return True 
                else:
                    if c in node.children:
                        node = node.children[c]
                    else:
                        return False 
            return True 
        return sub_search(word, node)