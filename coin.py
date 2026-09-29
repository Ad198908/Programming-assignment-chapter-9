"""
Program Name: Coin toss game
Author:Adhanet Gebretensay
Purpose:To create a class that represents a single coin
Starter Code: Python Library - random module
Date:09/29/2026
    
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