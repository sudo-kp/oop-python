import re
import os


class TextStat:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError('Wrong file name.')
        if not os.path.isfile(name):
            raise ValueError('No file with such name.')
        self.filename = name
        self.__num_of_char = 0
        self.__num_of_sent = 0
        self.__num_of_words = 0

    def count_char(self):
        with open(self.filename) as file:
            for line in file:
                self.__num_of_char += len(line)
        return self.__num_of_char

    def count_words(self):
        with open(self.filename) as file:
            for line in file:
                words = line.split()
                self.__num_of_words += len(words)
        return self.__num_of_words

    def count_sent(self):
        with open(self.filename) as file:
            for line in file:
                sentences = re.split(r"^\\s+[A-Za-z,;'\"\\s]+[.?!]$", line)
                self.__num_of_sent += len(sentences)
        return self.__num_of_sent


try:
    ob = TextStat('1')
    print(ob.count_char())
    print(ob.count_words())
    print(ob.count_sent())
except TypeError as message:
    print('TypeError: ')
    print(message)
except ValueError as message:
    print('ValueError')
    print(message)
except:
    print('Error')
