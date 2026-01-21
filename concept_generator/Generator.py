#1. Check if a string is palindrom using generator function
#Solution:
def is_Palindrome(strValue):
	yield strValue==strValue[::-1]
word="madam";
print(next(is_Palindrome(word)))
#---------------------------------------------------------------
#2. Print only even numbers from a list use generator
#Solution: 
def evens(nums):
    for num in nums:
        if num % 2 == 0:
                yield num

nums=[1,2,3,4,5,788,798,7,77]
for n in evens(nums):
    print(n)
#--------------------------------------------------------------------------
#3. Print only prime numbers using generator
#Solution:
def primeNumber(count):
	for n in range(count):
		if all(n%k!=0 for k in range(2, n)):
			yield n

for n in primeNumber(50):
    print(n)
 
#4. Write your own iterator and generator and iterate through a list.
#Iterator
nums=[12,54,87,9,2,8,7,96,8]
my_iter=iter(nums)
for n in my_iter:
	print(n)

#Generator
def listGenerator(numList):
  for n in numList:
    yield n

for n in listGenerator(nums):
  print(n)