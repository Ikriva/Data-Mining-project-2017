class TreeNode(object):
    def __init__(self, word, parent=None):
        self.word = word
        self.parent = parent
        self.children = []
        self.wordSet = set()
        self.wordSet.add(word)
        self.counter = 1
        self.horizontal_link = None

    def add_child(self, word):
        self.wordSet.add(word)
        node = TreeNode(word, self)
        self.children.append(node)
        return node

    def increment_counter(self):
        self.counter += 1

    def decrease_counter(self):
        self.counter -= 1

    def get_child(self, word):
        for item in self.children:
            if item.word == word:
                return item


