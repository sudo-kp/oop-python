import re

class TextStat:
	def __init__(self, name):
		self.file = open(name, 'r')

	def count_char(self):
		self.file.seek(0, 0)
		text = self.file.read()
		self.__num_of_char = len(text)
		return self.__num_of_char

	def count_words(self):
		self.file.seek(0, 0)
		text = self.file.read()
		words = text.split()
		self.__num_of_words = len(words)
		return self.__num_of_words

	def count_sent(self):
		self.file.seek(0, 0)
		text = self.file.read()
		sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)
		self.__num_of_sent = len(sentences)
		return self.__num_of_sent

ob = TextStat('1')
print(ob.count_char())
print(ob.count_words())
print(ob.count_sent())