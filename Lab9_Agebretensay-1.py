""" 
   Program name:
    Author:
    purpuse:
    satrter code:
    date:
"""
from player import Player
def main():
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    userinput = "y"
    while userinput == "y":
        player1.toss_coin()
        player2.toss_coin()
       
        side1 = player1.get_coin_side()
        side2 = player2.get_coin_side()
        print("player 1 tossed Heads")
        print("player 2 tossed Tails")
        if side1 == side2:
            player1.win_coin()
            player2.lose_coin()
            print("player 1 won the round")
        else:
            side1 != side2
            player2.win_coin()
            player1.lose_coin()
            print("Player 2 won the round")

            

        print(f"player 1 has {player1.get_wallet()} coin.") 
       
        print(f"player 2 has {player2.get_wallet()} coins.")
        userinput = input("do you want to play again? y/n:  ")

     

    if player1.get_wallet() > player2.get_wallet():
        print("player 1 has won the round")
    elif player1.get_wallet() < player2.get_wallet():
        print("player 2 has won the round")
    else:
        print("it's a draw")
    
if __name__== "__main__":
    main()




        




