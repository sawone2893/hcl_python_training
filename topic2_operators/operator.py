#Arithmetic Operators
num1 = 10
num2 = 5
addition = num1 + num2 # output: 15
subtraction = num1 - num2 # output: 5
multiplication = num1 * num2 # output: 50
division = num1 / num2  # output: 2.0
#Modulus Operator
modulus = num1 % num2   # output: 0
#Floor Division Operator
floor_div = 15 // 4 # output: 3
#Exponentiation Operator
exponentiation = 2 ** 3 # output: 8
  
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)    
print("Division:", division)
print("Modulus:", modulus)
print("Floor Division of 15 // 4:", floor_div)
print("2 raised to the power 3:", exponentiation)

#Comparison Operators
a = 15
b = 20
print("Equal:", a == b) # output: False
print("Not Equal:", a != b) # output: True
print("Greater Than:", a > b)   # output: False
print("Less Than:", a < b)  # output: True
print("Greater Than or Equal To:", a >= b)  # output: False
print("Less Than or Equal To:", a <= b) # output: True
#Logical Operators
x = True
y = False
print("Logical AND:", x and y) # output: False
print("Logical OR:", x or y)   # output: True
print("Logical NOT:", not x)    # output: False
#Assignment Operators
value = 10
value += 5 # output: 15
print("After += :", value)
value -= 3  # output: 12
print("After -= :", value)
value *= 2 # output: 24
print("After *= :", value)
value /= 4 # output: 6.0
print("After /= :", value)
value %= 3 # output: 0.0
print("After %= :", value)
#Bitwise Operators
p = 6  # Binary: 110
q = 3  # Binary: 011
print("Bitwise AND:", p & q)  # Binary: 010
print("Bitwise OR:", p | q)   # Binary: 111
print("Bitwise XOR:", p ^ q)  # Binary: 101
print("Bitwise NOT:", ~p)      # Binary: ...11111001
print("Left Shift:", p << 1)   # Binary: 1100
print("Right Shift:", p >> 1)  # Binary: 011
#Membership Operators
my_list = [1, 2, 3, 4, 5]
print("Is 3 in list?:", 3 in my_list) # output: True
print("Is 6 not in list?:", 6 not in my_list) # output: True
#Identity Operators
str1 = "hello"
str2 = "hello"
str3 = str1
print("str1 is str2?:", str1 is str2) # output: True
print("str1 is str3?:", str1 is str3) # output: True
print("str1 is not str2?:", str1 is not str2) # output: False
print("str1 is not str3?:", str1 is not str3) # output: False
print("str1 id:", id(str1)) # output: memory address
print("str2 id:", id(str2)) # output: memory address
print("str3 id:", id(str3)) # output: memory address
#Ternary Operator
age = 18
status = "Adult" if age >= 18 else "Minor"
print("Status:", status) # output: Adult
#Unary Operators
num = 10
print("Unary Plus:", +num) # output: 10
print("Unary Minus:", -num) # output: -10
print("Increment:", num + 1) # output: 11
print("Decrement:", num - 1) # output: 9
#Augmented Assignment Operators
count = 5
count += 2
print("After += 2:", count) # output: 7
count *= 3
print("After *= 3:", count) # output: 21
count -= 4
print("After -= 4:", count) # output: 17
count /= 2
print("After /= 2:", count) # output: 8.5
count %= 3
print("After %= 3:", count) # output: 2.5
#Operator Precedence
result = 10 + 5 * 2 - (8 / 4) ** 2
print("Result of operator precedence:", result) # output: 17.0
#Shift Operators
num = 8  # Binary: 1000
print("Left Shift by 2:", num << 2)  # Binary: 100000
print("Right Shift by 2:", num >> 2) # Binary: 0010 
#Chained Comparison Operators
x = 10
is_between = 5 < x < 15
print("Is x between 5 and 15?:", is_between) # output: True
#Complex Number Operators
complex1 = 2 + 3j
complex2 = 1 + 4j
complex_add = complex1 + complex2
complex_sub = complex1 - complex2
print("Complex Addition:", complex_add) # output: (3+7j)
print("Complex Subtraction:", complex_sub) # output: (1-1j)
#String Operators
str_a = "Hello"
str_b = "World"
str_concat = str_a + " " + str_b
str_repeated = str_a * 3
print("String Concatenation:", str_concat) # output: Hello World
print("String Repetition:", str_repeated) # output: HelloHelloHello
#List Operators
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list_concat = list1 + list2
list_repeated = list1 * 2
print("List Concatenation:", list_concat) # output: [1, 2, 3, 4, 5, 6]
print("List Repetition:", list_repeated) # output: [1, 2, 3, 1, 2, 3]
#Dictionary Operators
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict1.update(dict2)
print("Updated Dictionary:", dict1) # output: {'a': 1, 'b': 3, 'c': 4}
#Set Operators
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set_union = set1 | set2
set_intersection = set1 & set2
print("Set Union:", set_union) # output: {1, 2, 3, 4, 5}
print("Set Intersection:", set_intersection) # output: {3}
#Lambda Operator
square = lambda x: x ** 2
print("Square of 5 using lambda:", square(5)) # output: 25
#Walrus Operator
if (n := 10) > 5:
    print("Walrus Operator assigned n =", n) # output: Walrus Operator assigned n = 10
#Type Conversion Operators
num_str = "100"
num_int = int(num_str) # output: 100
num_float = float(num_str) # output: 100.0
print("String to Integer:", num_int)
print("String to Float:", num_float)
#Identity vs Equality
list_a = [1, 2, 3]
list_b = [1, 2, 3]
print("list_a == list_b?:", list_a == list_b)
print("list_a is list_b?:", list_a is list_b)
print("list_a id:", id(list_a))
print("list_b id:", id(list_b))
#Conditional Expressions
value = 42
result = "Even" if value % 2 == 0 else "Odd"
print("The value is:", result)
#Numeric Operators
import math
num = 16
sqrt_num = math.sqrt(num)
log_num = math.log(num)
print("Square Root of", num, "is:", sqrt_num)
print("Natural Logarithm of", num, "is:", log_num)
