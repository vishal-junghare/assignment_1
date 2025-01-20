# # Que 1 => write arthematic optration 
first_num = int(input("Enter the first number: "))
second_num  = int(input("Enter the second number: "))

# perform a arthmatical opration 
 # Addition 
print("Addition : ",first_num+second_num)
# subtraction
print("Subtraction : ",first_num-second_num)
# Product 
print("Product : ",first_num*second_num)
# Division 
print("Division : ",first_num/second_num)
#Modules 
print("Modules : ",first_num%second_num)
#Exponention 
print("Exponention : ",first_num**second_num)
#floor Division 
print("Floor Division : ",first_num//second_num)

#Que 2 => Circle Area and Circumference 
radius =int(input())
calculate_Area_circle = 3.14*(radius**2) 
circumference_circle = 2*3.14*(radius)
print(calculate_Area_circle)
print(circumference_circle)


#Que 3 => Rectangle Perimeter and Area 
length = int(input())
width = int(input())
perimeter_area_rectangle = 2*(length+width)
print(perimeter_area_rectangle)



#Que 4 => Average Number 
first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
third_num = int(input("Enter the third number: "))
calculte_average = (first_num +second_num+third_num)/3
print(calculte_average)



#Que 5 unit conversion Celsius to fahrenheit 
temp_celsius = int(input())
celsius_covert_fahrenheit = (temp_celsius*9/5)+32
print(celsius_covert_fahrenheit)