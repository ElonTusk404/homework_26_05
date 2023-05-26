#Program that generates and prints 50 random floating numbers, each between 3 and 6.
import random as r
result = []
for i in range(50):
    result.append(r.uniform(3, 6))
print(result)