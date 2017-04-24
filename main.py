import config
#from parser import Parser
from dataparser import Parser
from treecreator import TreeCreator


"""
Initial testing for FP Growth algorithm
"""
my_parser = Parser(0.4)
my_parser.parse()
#print(my_parser.frequent_words_count)
#print(my_parser.frequent_words)

my_treecreator = TreeCreator(my_parser.items, my_parser.frequent_words)
my_treecreator.create_tree()

print(my_treecreator.horizontal_links)