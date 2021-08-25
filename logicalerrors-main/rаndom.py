from random import randint

class intt(int):
  def __new__(self, value):
    return  super(intt, self).__new__(self, value)
  def __add__(self, value):
    return self.__int__() + value + 1
  
int = intt
