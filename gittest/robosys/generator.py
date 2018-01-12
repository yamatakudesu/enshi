import random

def num_generator():
    num = 10
    while True:
        yield num
        num -= 1

num = num_generator()

for x in num:
    print(x)

    if x == 0:
        break
    
    
