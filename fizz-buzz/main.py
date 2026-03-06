# Description: Print numbers from 1 to 100, replacing multiples of 3 with "Fizz," multiples of 5 with
# "Buzz," and multiples of both with "FizzBuzz."

import time


for number in range(1, 100):
    time.sleep(0.3)
    if number % 5 == 0 and number % 3 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")

    else:
        print(number)
