#why use function 

#syntax:
#def_function_name(parameters):
#(code)

#ex
def great():
    print("hello")
    
great() #calling the function

#function with parameters
#used to pass value

#example:
def great(name):
    print("hello"+name) #def great(name="student"): to set default value
                        #print("f"hello{name}") to use f string
                        #great()
                        #great("bushra") to call the function with argument
                        
great("bushra") # calling the function with argument

#function with return value
#useng when we want to send result back.

#ex:
def add(a, b):
    return a+b
result = add (2,3)
print(result) #print 5

#task 1:creat a function to calculate and return the result
#use return statment

#task 2: creat a function to check if  a number is even or odd.
#use modules operator


def even_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"
    
    print(even_odd(4)) #print even    
    
#task 3: create a function to find the factorial of a number.

number=int(input("enter a number:"))
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
result = factorial(number)
print(f"the factorial of {number} is {result}.")

#task 4: creat a function to find maximum of three numbers

num1=int(input("enter a number: "))
num2=int(input("enter a number: "))
num3=int(input("enter a number: ")) 

def maximum(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num3 and num2 > num3:
        return num2
    else:
        return num3
print(maximum(num1,num2,num3))
    
#task 5: create a function to check if a string is palindrome

text = input("enter a string: ")

def palindrome(text):
    if text == text [::-1]:
        return "palindrome"
    else:
        return "not a palindrome"

print(palindrome(text))  

#task 6: create a function to calculate the area of circle.
radius=int(input("enter the radius: "))

def area(radius):
    return 3.14 * radius * radius

print(area(radius))


      