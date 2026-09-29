"""
Program Name: 
Author:
Purpose:
Starter Code: Python Library - random module
Date
    
"""

import random

class Coin: #class
    #constructor
    def ___init___(self):
        self.__sideUp= 'Heads'

    def toss(self):
        result = random.randint(0,1)

        if result == 0:
            self.__sideUp = 'Heads'
        else:
            self.__sideUp = 'Tails'


    def get_sideUp(self):
        return self.__sideUp
    
    
    #getters
    #setters