# create a variable that stores the guess number

count=0
# a while loop to keep asking the user to guess the number
while True:
  guess=int(input("Guess a number: "))
  
  # if user types a negative number exit program
  if guess<0:
    print("You have entered a negetive input, the program will now exit. Bye!")
    exit()
  elif guess==201:
    count+=1
    print("You win! 201 is the number")
    break
  # prompt when too high or too low
  elif guess<201:
    count+=1
    print("The guess is too low")
  elif guess>201:
    count+=1
    print("The guess is too high")
# count number of attempts 
print(f"It has taken you {count} attempts to get it right!")


