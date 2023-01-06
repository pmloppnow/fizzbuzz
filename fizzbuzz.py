# Takes an int(x) as input and prints "Fizz" if divisible by 3, "Buzz" if divisible by 5, and "Fizzbuzz" if divisible by 
# 15 for every number between 0 and x.
num = int(input("Enter a whole number: "))
list = []
sum = 0
fizz_count = 0
buzz_count = 0
fizzbuzz_count = 0

while num >= 0:
    if num % 15 == 0: list.append("Fizzbuzz")
    elif num % 5 == 0: list.append("Buzz")
    elif num % 3 == 0: list.append("Fizz")
    else: list.append(num)
    num -= 1

for i in list:
    if type(i) is int: sum += i
    elif i == "Fizz": fizz_count += 1
    elif i == "Buzz": buzz_count += 1
    elif i == "Fizzbuzz": fizzbuzz_count += 1

print("----------")
print(f"List: {list}")
print("----------")
print(f"Sum of all integers in list: {sum}")
print(f"Fizzes in list: {fizz_count}")
print(f"Buzzes in list: {buzz_count}")
print(f"Fizzbuzzes in list: {fizzbuzz_count}")