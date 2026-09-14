import random
int1 = int(input("Enter the first integer: "))
int2 = int(input("Enter the second integer: "))
randomnum = random.randint(int1, int2)
for i in range(5):
    print("Random number", i + 1, "between", int1, "and", int2, "is:", randomnum)
    randomnum = random.randint(int1, int2)