#Ask user to enter a number to see if it is a prime number
userNum = int(input("Please enter a number to check if it is a prime number: "))

#A Prime number is greater than 1
if userNum > 1:
    #Loop through between 2 and user number to see if it is divisible by anything to determine if it is a prime number
    for i in range(2, userNum):
        if (userNum % i) == 0:
            print(userNum, "isn't a prime number")
            print(i, "times", int(userNum/i), "is", userNum)
        else:
            print(userNum, "is a prime number!")
        break
else:
    print(userNum, "is not a prime number")
