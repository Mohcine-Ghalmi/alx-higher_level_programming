#!/user/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of %d is " % number, end="")
if number  % 10 > 5:
    print("%d and is greater  than 5" % (number % 10))
elif number  % 10 > 6:
    print("%d and is less then 6 and not 0" % (number % 10))
else:
    print("%d and is 0" % (number % 10))
