# create countdown timer

import time

seconds = int(input("Enter the number of seconds for the countdown: "))

while seconds > 0:
    print(f"seconds remaining: {seconds} ", end="\r")  # overwrite the same line
    time.sleep(1)
    seconds -= 1

print("Time's up!")
