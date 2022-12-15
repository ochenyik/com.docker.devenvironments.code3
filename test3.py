print("I am a super genious")
name = input("What is your name")
print(name)
num1 = int(input("Enter the first number"))

num2 = int(input("Enter the second number"))

print(num1 + num2)

numbers = [23,76,45,71,98,23,65,37,93,71,37,40,21]
above50 = 0
for counter in range(len(numbers)):
    if numbers[counter] > 50:
        above50 = above50 + 1
print("The has", above50, "numbers above 50