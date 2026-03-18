#what is loop?
#a loop is used to repeat a blockof code multiple
#time until acondition is met.

#types of loops in python
#1. for loop
# used when we know how many time we want to repeat.

#syntax

#for varible in squance:
#code

#range() function is commonly used to generate a sequence of numbers.

#range com with a parameters:
#1.start
#2. stop


#while loop
#example
for i in range(1,6):
    print(i)

#key points:
#1. range(start,stop)generates number
#2.
i=1
while i <= 5:
    print(i)
    i+= 1
    
#1. break
#stops the loop immediately
#ex:
for i in range(1,6):
    if i == 3:
        break
    print(i)

#2. continue
#skips current interation

for i in range(1,6):
    if i == 3:
        continue
    print(i)
    
#pass

for i in range(1,5):
    if i == 3:
        pass
    print(i)
    
#task1
for i in range(1,11):
    print(i)
    
#task2:even number for 1 to 20.
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
    
#task3:print odd number from 1 to 15.
for i in range(1, 16):
    if i % 2 != 0:
        print(i)
        
#task4:print each character of a string using for loop.
text="python"
for char in text:
    print(char)
    
#task5: print all item in the list using for loop.

fruits=["apple","banana","mango"]
for items in fruits:
    print(items)
    
#task6: find the sum of number from 1 to 10 using a for loop.

total =0
for i in range(1,11):
    total += i
    print(total)
    
#task7: print a multiplication table of 5 using a for loop.
for i in range(1,11):
    print(f"5 x {i} = {5*i}")
    
#task8: count how many vowels are in string using for loop.
text = "helloo"
vowels="aeiou"
count=0
for char in text:
    if char in vowels:
        count += 1
        print(count)
        
#task9: print numbers in reverse  order from 10 to 1 using for loop.

for i in range(10, 0, -1):
    print(i)
    
#task10: print square of numbers from 1 to 5.
for i in range(1,6):
    print(i*i) 
    

