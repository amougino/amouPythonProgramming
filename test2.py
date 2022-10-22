found = 0
number = 1024
while number < 16385:
    if number % 1024 == 0:
        print(number)
        found += 1
    number += 1
print(found)