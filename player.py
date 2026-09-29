"""
Program Name:Coin toss game
Author: Adhanet Gebretensy
Purpose: To make a player class that manaeges the player's name, wallet ,and coin object.
Starter Code / Resources: Coin class from coin.py
Date:09/29/2026
"""

from coin import Coin

class Player:
     def __init__(self, name):
          self.__name = name
          self.__wallet = 20
          self.__coin = Coin()

     def toss_coin(self):
          self.__coin.toss()

     def get_coin_side(self):
          return self.__coin.get_sideUp()

     def lose_coin(self):
         self.__wallet = self.__wallet - 1

     def win_coin(self):
         self.__wallet = self.__wallet + 1

     def get_name(self):
          return self.__name

     def get_wallet(self):
          return self.__wallet

    
      


    