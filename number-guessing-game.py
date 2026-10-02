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
      break
    elif guess>number:
      print("Too high!")
    elif guess<number:
      print("Too low!")
    else:
      print("Well i think i said a number between 1to 1000!")
    attempts-=1
  if attempts==0:
    print("OOPS!!!You have run out of attempts!!!")
    print("The number was",number)
    break
