import random
class Card():
    def __innit__ (self, value):
        self.__value = 0
        
    def deal(self):
        self.__value = random.randint(1,13)
        
    def set_value (self, card_value):
        self.__value = card_value
        
    def get_value (self):
        return self.__value
    
    def find_face_value(self):
        face = [ "Ace", "Two", "Three", "Four", "Five", "Six",\
                 "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

        face = face[self.__value - 1]
        return face
          
        
    def __str__(self):
        str(self.__value)