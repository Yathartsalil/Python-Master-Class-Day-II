# Basic arithmetic operations in Python
a = 15
b = 20

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)

print()

#Comparison operators
x = 10
y = 20

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x>=y)
print(x<=y)

print()

#Logic operators
age = 18
has_id = True

print(age >= 18 and has_id)
print(age >= 18 or has_id)
print(not has_id)

print()

#Assignment operators

num = 10 #Assignment
print(num)
num +=7 #Add and assign
print(num)
num -=7 #Add and assign
print(num)
num *=7 #Add and assign
print(num)
num /=7 #Add and assign
print(num)
num //=7 #Add and assign
print(num)
num %=7 #Add and assign
print(num)

print()

#Problem 1 :
# Practice Question 1

# Taking two numbers from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# 1. Sum
print("Sum:", num1 + num2)

# 2. Remainder
# (Remainder when num1 is divided by num2)
print("Remainder (num1 % num2):", num1 % num2)

# 3. Which number is larger
if num1 > num2:
    print(num1, "is larger.")
elif num2 > num1:
    print(num2, "is larger.")
else:
    print("Both numbers are equal.")
