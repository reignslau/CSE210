from random import randint
score = int(10)

play = input("Let's start the game you have 300 points. [y/n]")
while play =="y":
     number1 = randint(1,13)
     number2 = randint(1,13)
     print("The card is: ",number1)
     guess = input("Higher or lower? [h/l]")
     print("Next card was: ",number2)
     if guess =="h":
         if number2 > number1:
             score = score + 100
             print("Your score is: ", score)
         if number2 < number1:
             score = score - 75
             print("Your score is: ", score)
     if guess =="l":
         if number2 < number1:
             score = score + 100
             print("Your score is: ", score)
         if number2 > number1:
             score = score - 75
             print("Your score is: ", score)
     if score > 0:
         play = input("Play again? [y/n]")
     if score < 0:
         play = input("You loss! Do want want to play again? [y/n]")
if play == "n":
    print("thanks for play!")   
