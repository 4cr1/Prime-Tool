import math
from math import sqrt
import datetime
from datetime import datetime
import os
print("""
     ______   ______     __     __    __     ______   ______     ______     __        
    /\  == \ /\  == \   /\ \   /\ "-./  \   /\__  _\ /\  __ \   /\  __ \   /\ \       
    \ \  _-/ \ \  __<   \ \ \  \ \ \-./\ \  \/_/\ \/ \ \ \/\ \  \ \ \/\ \  \ \ \____  
     \ \_\    \ \_\ \_\  \ \_\  \ \_\ \ \_\    \ \_\  \ \_____\  \ \_____\  \ \_____\ 
      \/_/     \/_/ /_/   \/_/   \/_/  \/_/     \/_/   \/_____/   \/_____/   \/_____/ """)
while True:
    numCalculated = 0
    Q = 2
    primNumbers = []

    print("1) Calculate prime numbers")
    print("2) Check prime number")
    print("3) Write to file")
    print("4) Exit")
    selection = int(input("Enter Number: "))


    if selection == 1:

        higher = input("Calculate up to: ")

        startTime = datetime.now()
        for number in range(2, int(higher)):
            Q = 2

            while Q < math.sqrt(number):
                if number % Q == 0:
                    break

                elif number % Q != 0:
                    Q += 1
                    for primNumber in primNumbers:
                        if number % primNumber == 0:
                            break

                        elif primNumber > math.sqrt(number):
                            print(number)
                            numCalculated += 1
                            primNumbers.append(number)
                            break
                break

            if Q > math.sqrt(number) and number not in primNumbers:
                print(number)
                numCalculated += 1
                primNumbers.append(number)

        endTime = datetime.now()

        print(f"Found {numCalculated} prime numbers.")
        print("Duration: {}".format(endTime - startTime))

    elif selection == 2:
        numToCheck = int(input("Enter Number to check: "))
        Q = 2
        while Q < math.sqrt(numToCheck):
            if numToCheck % Q == 0:
                print(f"{numToCheck} is not a prime number.")
                break
            elif numToCheck % Q != 0:
                Q += 1
        if Q > math.sqrt(numToCheck):
            print(f"{numToCheck} is a prime number.")

    elif selection == 3:
        numCalculated = 0

        highEnd = int(input("Up to: "))
        while True:
            f = open(input("Enter Path to file: "), "a")
            if os.path.exists(str(f)):
                break
        startTime = datetime.now()
        for number in range(2, highEnd):
            Q = 2

            while Q < math.sqrt(number):
                if number % Q == 0:
                    break

                elif number % Q != 0:
                    Q += 1
                    for primNumber in primNumbers:
                        if number % primNumber == 0:
                            break

                        elif primNumber > math.sqrt(number):
                            print(number)
                            numCalculated += 1
                            primNumbers.append(number)
                            f.write(f"{number}\n")
                            break
                break

            if Q > math.sqrt(number) and number not in primNumbers:
                print(number)
                numCalculated += 1
                primNumbers.append(number)
                f.write(f"{number}\n")

        endTime = datetime.now()
        print(f"Found {numCalculated} prime numbers.")
        print("Duration: {}".format(endTime - startTime))
        f.close()
    elif selection == 4:
        print("""
      _______   ______     ______    _______  .______   ____    ____  _______ 
     /  _____| /  __  \   /  __  \  |       \ |   _  \  \   \  /   / |   ____|
    |  |  __  |  |  |  | |  |  |  | |  .--.  ||  |_)  |  \   \/   /  |  |__   
    |  | |_ | |  |  |  | |  |  |  | |  |  |  ||   _  <    \_    _/   |   __|  
    |  |__| | |  `--'  | |  `--'  | |  '--'  ||  |_)  |     |  |     |  |____ 
     \______|  \______/   \______/  |_______/ |______/      |__|     |_______|""")
        break
