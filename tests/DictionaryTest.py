from PyDictionary import PyDictionary
# from bs4 import BeautifulSoup

dictionary = PyDictionary("indication")
# dictionary = PyDictionary()
# a = dictionary.meaning("indication")['Noun']
# a = dictionary.meaning("indication")
# print(len(dictionary.meaning("indication")['Noun']))
# print(a)

print(dictionary.printMeanings())
# soup = BeautifulSoup(a)
# print(soup)
# s = ""


# print(dictionary.printMeanings())

# for i in a:
#     s += i + " "

# print(s)