class TreeNode:
    def __init__(self):
        self.children = {}
        self.is_word_end = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        n = len(word)
        
        node = self.root
        for i, ch in enumerate(word):    
            if ch in node.children:
                node = node.children[ch]
                if i == n - 1:
                    node.is_word_end = True
            else:
                newNode = TreeNode()
                node.children[ch] = newNode
                node = node.children[ch]
                if i == n - 1:
                    node.is_word_end = True
        node = None


    def search(self, word: str) -> bool:
        n = len(word)
        
        curr = self.root
        for i, ch in enumerate(word):
            if ch in curr.children:
                curr = curr.children[ch]
                if i == n - 1:
                    return curr.is_word_end
            else:
                return False

    def startsWith(self, prefix: str) -> bool:
        n = len(prefix)
        curr = self.root
        print(curr.children)
        for i, ch in enumerate(prefix):
            if ch in curr.children:
                curr = curr.children[ch]
                if i == n - 1:
                    return True
            else:
                return False
    
        