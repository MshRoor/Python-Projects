import random
correctCount = 0 
computerNumber = random.randint(0,9) #Determines the range in which the random numbers are generated

def guessNumber(n, compNum): #Function takes the user number and the random computer number as parameters

    if(n > compNum):
        print("Whoops, guessed too high. Try a smaller number.")
        return
    elif(n < compNum):
        print("Try a larger number next time!")
        return
    elif(n == compNum):
        print("Correct!! Great Job")
        global correctCount
        correctCount += 1


while correctCount < 1: #The loop is basically a stop condition
    value = int(input("Guess a number between 0 and 9: "))

    guessNumber(value, computerNumber)


