'Python Assignment 2'

#Question 1: 
print("\n\tQuestion 1\n")

string = "Python is a case sensitive language"
print("Given string is: ", string)

#PART (a) -
print("The length of the string is: ", len(string))

#PART(b)-
print("The string in reversed order is: ", string[::-1])

#PART(c)-
new_string = string[10:26]
print("The new string is: ", new_string)

#PART(d)-
print("The modified string is:", string.replace("a case sensitive", "object oriented"))

#PART(e)-
substring_index = string.find("a")
print('The index of the substring "a" is ', substring_index)

#PART(f)-
print("The string without the white spaces is: ", string.replace (" ", ""))
print()




#Question 2- 
print("\tQuestion 2\n")

name = input("Enter your name: ")
SID = int(input("Enter your SID: "))
Dept_Name = input("Enter your department name: ")
CGPA = float(input("Enter your CGPA: "))

print()

print("Hey {0} Here!\
    \nMy SID is {1}\
    \nI am from {2} department and my CGPA is {3}.".format(name, SID, Dept_Name, CGPA))
print()



#Question 3-  
print("\tQuestion 3\n")

a = 56
b = 10

print("Value of a: ", a)
print("Value of b: ", b)

#(a) part
print("a & b = ", a&b)

#(b) part
print("a | b = ", a|b)

#(c) part
print("a ^ b = ", a^b)

#(d) part
print("Left shifting both a and b with 2 bits = , a-{0},b-{1}".format(a<<2,b<<2))

#(e) part
print("Right shifting a by 2 and b with 4 bits: a-{0},b-{1}".format(a >> 2, b >> 4))
print()




#Question 4- 
print("\tQuestion 4\n")

Number1 = float(input("Enter the first number: "))
Number2 = float(input("Enter the second number: "))
Number3 = float(input("Enter the third number: "))

if (Number1 >= Number2) and (Number1 >= Number3):
    Greatest_num = Number1

elif (Number2 >= Number1) and (Number2 >= Number3):
    Greatest_num = Number2

else:
    Greatest_num = Number3

print("The greatest of the three numbers entered is: ", Greatest_num)
print()




#Question 5- print("\tQuestion 5\n")

input_string = input("Enter the string: ")

if ("name" in input_string):
    print("Yes")

else:
    print("No")
print()




#Question 6- 
print("\tQuestion 6\n")

side1 = input("Enter the Length of first side: ")
side2 = input("Enter the Length of second side: ")
side3 = input("Enter the Length of third side: ")

side1 = int(side1)
side2 = int(side2)
side3 = int(side3)

if (side3 >= side1 + side2) or (side2 >= side1 + side3) or (side1 >= side2 + side3):
    print("No")

else:
    print("Yes")
print()
print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
