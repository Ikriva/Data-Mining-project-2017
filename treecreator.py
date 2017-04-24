from treenode import TreeNode
import config


class TreeCreator(object):
    def __init__(self, data, frequent_words):
        self.data = data
        self.frequent_words = frequent_words
        self.root_node = TreeNode(0)
        self.horizontal_links = {word: {"last_node": None, "node_set": set()} for word in frequent_words}

    def create_tree(self):
        for word_set in self.data:
            current_node = self.root_node
            for word in word_set:
                if word in current_node.wordSet:
                    current_node = current_node.get_child(word)
                    current_node.increment_counter()
                else:
                    current_node = current_node.add_child(word)
                    link = self.horizontal_links[word]
                    if current_node not in link["node_set"]:
                        link["node_set"].add(current_node)
                        current_node.horizontal_link = link["last_node"]
                        link["last_node"] = current_node


if __name__ == "__main__":
    test = TreeCreator("data/stub.txt", "test")
    test.create_tree()


