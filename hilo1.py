# Use "import" to use 'random' function for the code.
from random import randint
# In this projectwe need to check the score, and according to the rules player start with 300 points.
score = int(300)

play = input("Let's start the game you have 300 points. [y/n]")
# Use 'While' to set up the loop, so player can paly as many as they want. 
while play =="y":
    # Ues the 'random.randint' to let the out put is random number for the project. 
    # We need two number that show randomly for the project. 
     number1 = randint(1,13)
     number2 = randint(1,13)
     # Show the first card. 
     print("The card is: ",number1)
     # Ask player what he think the next card will be. 
     guess = input("Higher or lower? [h/l]")
     # Show the second card. 
     print("Next card was: ",number2)
     # For the player that think the next card will be higher than the first one. 
     if guess =="h":
         # If the player guess is right, then he will get 100 point.
         if number2 > number1:
             score = score + 100
             print("Your score is: ", score)
         # if the player guess is wrong, then he will lost 75 point. 
         if number2 < number1:
             score = score - 75
             print("Your score is: ", score)
     # For the player that think the next card will be lower than the first one. 
     if guess =="l":
         # If the player guess is right, then he will get 100 point.
         if number2 < number1:
             score = score + 100
             print("Your score is: ", score)
         # if the player guess is wrong, then he will lost 75 point. 
         if number2 > number1:
             score = score - 75
             print("Your score is: ", score)
     # For the score if player have more than 0, the player can choice keep playing or not.
     if score > 0:
         play = input("Play again? [y/n]")
     # If the score are equal or less than 0, then the game is over. Player can start over. 
     if score < 0:
         play = input("You loss! Do want want to play again? [y/n]")
# Player can stop the game by using 'n' for the answer. 
if play == "n":
    print("thanks for play!")   