from random import randint
score = int(300)

while True:
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
         else:
             print("Two number is the same!")
     if guess =="l":
         if number2 < number1:
             score = score + 100
             print("Your score is: ", score)
         if number2 > number1:
             score = score - 75
             print("Your score is: ", score)
         else:
             print("Two number is the same!")
         play_again = input("Play again? [y/n]")
         if play_again == "y":
                  continue
         else:
                 break