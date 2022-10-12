# Use "import" to use 'random' function for the code.
import random

# In this project we need to values and need to check the score. And according to the rules player start with 300 points.
value1 = 0
value2 = 0
score = int(300)

# Ues the 'random.randint' to let the out put is random number for the project. 
value1 = random.randint(1,13)
value2 = random.randint(1,13)


while True:
         print("The card is: ",value1)

         x = input("Higher or lower? [h/l]")

         print("Next card was: ",value2)
         if x == 'h':
                 if value2 > value1:
                         print("Your score is: "+str(score+100))
                 if value2 < value1:
                         print("Your socre is: "+str(score-75))
         if x =="l":
                 if value2 < value1:
                         print("Your score is: "+str(score+100))
                 if value2 > value1:
                         print("Your socre is: "+str(score-75))
         play_again = input("Play again? [y/n]")
         if play_again == "y":
                  continue
         else:
                 break
        
         
                        
