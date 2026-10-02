# A number guessing game
print("Hello,")
print("Today we are going to play a number guessing game.") 
while True:
 import random
 number=random.randint(1,1000)
 attempts=10
 print("I have selected a number between 1 to 1000.")
 print("You have 10 chances or attempts to guess the number.")
 print("")
 print("After 10 atttempts the actual number will be displayed!")
 print("")
 while attempts >0:
   print("Attempts remaining:",attempts)
   guess=int(input("Enter your guess:"))
   if guess==number:
     print("WOW!!You actually guessed it right!!")
     print("")
     break
   elif guess>number:
      print("Too high!")
   else:
      print("Too low!")
   attempts-=1
   if attempts==0:
     print("OOPS!!!You have run out of attempts!!!")
     print("The number was",number)
     print("")
 again=input("Do you want to play another round? (yes/no):")
 print("")
 if again.lower()!="yes":
   print("Thank you for playing this game!")
   break
