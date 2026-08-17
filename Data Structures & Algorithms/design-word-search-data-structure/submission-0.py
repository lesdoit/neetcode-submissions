class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

        
    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.word_end = True
        return None

    def search(self, word: str) -> bool:
        
        def mod_search(node, word):
            cur = node
            for i, ch in enumerate(word):
                if ch == '.':
                    res = False
                    for k, v in cur.children.items():
                        res = res or mod_search(cur.children[k], word[i+1:])
                    return res
                else:
                    if ch not in cur.children:
                        return False
                    cur = cur.children[ch]
            return cur.word_end
        
        return mod_search(self.root, word)
        

        
