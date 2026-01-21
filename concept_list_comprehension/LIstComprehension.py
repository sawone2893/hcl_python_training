nums=[12,54,87,98,78,65,56,78,1549,956,17,19]
#Even Number
result=[n for n in nums if n%2==0]
#Odd Number
result=[n for n in nums if n%2!=0]
#Prime Numbers
result=[n for n in nums if all(n%k!=0 for k in range(2,n))]
#Double Even Number
result=[n*2 for n in nums if n%2==0]
print(result)