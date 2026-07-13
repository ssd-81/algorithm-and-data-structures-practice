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
        def sub_search(word, node)->bool:
            for i in range(len(word)):
                if word[i] == '.':
                    for child in node.children:
                        if sub_search(word[i:], node.children[child]):
                            return True 
                else:
                    if word[i] in node.children:
                        node = node.children[word[i]]
                    else:
                        return False 
            return node.is_word
        return sub_search(word, self.root)