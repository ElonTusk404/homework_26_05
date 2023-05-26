#Program that generates and prints 50 random numbers, each between 3 and 6.
import random as r
result = []
for i in range(50):
    result.append(r.randint(3, 6))
print(result)