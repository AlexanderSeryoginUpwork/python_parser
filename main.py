# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from classes.Parser_class import Parser


def run():
    parser = Parser('https://www.ua-football.com/sport', 'football.txt')
    parser.run()
    print(parser.results)


run()
