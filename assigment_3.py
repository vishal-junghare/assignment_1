# This script prints numbers from 1 to 20 using a for loop

# Loop through numbers from 1 to 20
for number in range(1, 21):
    print(number)

# calculate the sum of odd numbers from 1 to 50 using a for loop
sum_of_odd_numbers = 0
for number in range(1, 51):
    if number % 2 != 0:
        sum_of_odd_numbers += number
print(sum_of_odd_numbers)

# Print the first 10 multiples of a given number using a for loop
given_number = int(input("enter ur number: "))  # You can change this to any number you want
for i in range(1, 11):
    print(given_number * i)

# Find the factorial of a given number using a for loop
factorial_number = int(input("Enter a number to find its factorial: "))
factorial = 1
for i in range(1, factorial_number + 1):
    factorial *= i
print(f"The factorial of {factorial_number} is {factorial}")

Reverse a string using a for loop
input_string = input("Enter a string to reverse: ")
reversed_string = ""
for char in input_string:
    reversed_string = char + reversed_string
if input_string == reversed_string:
    print(f"The string {input_string} is a palindrome")
else:
    print(f"The reversed string is: {reversed_string}")


#print the following right angle triangle using for loop
input_number = int(input("Enter a number: "))
print("Right angle triangle:")
for i in range(1, input_number + 1):
    print("* " * i)


Print the following inverted triangle pattern using a for loop:*
input_number = int(input("Enter a number: "))
print("Right angle triangle:")
for i in range(input_number, 0, -1):
    print("* " * i)


print the following pyramid pattern using for loop 
input_number = int(input("Enter a number: "))
print("Pyramid pattern:")
for  i in range(1, input_number + 1):
    print(" " * (input_number-i)+"* "*i)


#Print the following diamond pattern using a for loop
input_number = int(input("Enter a number: "))
print("Diamond pattern:")
for i in range(1, input_number + 1):
    print(" " * (input_number - i) + "* " * i)

for i in range(input_number - 1, 0, -1):
    print(" " * (input_number - i) + "* " * i)
    
print the following number pattern using for loop

#print the following right angle triangle using for loop
input_number = int(input("Enter a number: "))
print("Right angle triangle:")
string = ""
for i in range(1, input_number + 1):
    string+=str(i)+" "
    print(string)


print followoing number pathhern using for loop 
input_number = int(input("Enter a number: ")) 
for  i in range(1,input_number+1):
    string=""
    for j in range(1,i+1):
        string+=str(i)+" "
    print(string)
        
print the following hollow square pattern using for loop
input_number = int(input("Enter a number: "))
print("Hollow square pattern:")
for i in range(1,input_number+1):
    if (i == 1 or i == input_number):
        print("* " * input_number)
    else:
        print("* " + "  " * (input_number-2) + "* ")


print the following hollow triangle pattern using for loop
input_number = int(input("Enter a number: "))
print("Hollow tr5iangle pattern:")

for i in range(1,input_number+1):
   
    hollow_space = (input_number-i)
    if (i == 1 or i == input_number):
        print(" "*hollow_space+"* "*i)
    else:
        print(" "*hollow_space+"* "+"  "*(i-2)+"*")
        
    
print the following checkboard pattern using for loop
input_number = int(input("Enter a number: "))
print("Checkboard pattern:")
for i in range(1,input_number+1):
    if i%2==0:
        print(" *"*input_number)
    else:
        print("* "*input_number)


# *Print the following hourglass pattern using a for loop:
input_number = int(input("Enter a number: "))
print("Hourglass pattern:")
for i in range(input_number, 0, -1):
    if (i == input_number or i == 1):
        print(" " * (input_number - i) + "* " * i)
    else:
        print(" " * (input_number - i) + "* " + "  " * (i - 2) + "* ")
for i in range(2, input_number + 1):
    if (input_number == i):
        print(" " * (input_number - i) + "* " * i)
    else:
        print(" " * (input_number - i) + "* " + "  " * (i - 2) + "* ")  

