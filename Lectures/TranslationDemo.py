''' Problem C)

c) Ask the user to input an integer and decide if its odd or even.
	1.	Write "Enter the number"
	2.	Read number
	3.	remainder = Remainder from number / 2
	4.	If remainder is equal to 0 then do step 5
	5.		Write "This number is Even."
	6.	Else do step 7
	7.		Write "This number is Odd."

##1.  Read number
number = input("Enter an integer :")
number = int(number)

##2.  remainder = Remainder from number
remainder = number % 2

##3.  If remainder is equal to 0 then do step 4
if remainder == 0:
	##4.  Write "This number is Even."
	print(str(number) + "is even.")
##5.  Else do step 6
else:
	##6.  Write "This number is Odd."
	print(str(number) + " is odd.")
'''

''' Problem G)

g.	Calculate the factorial of N where N is input by the user.

	1.	Write “Enter N:”
	2.	Read N
	3.	factorial = 1
	4.	k = 1
	5.	repeat steps until k is equal to N
	6.	    factorial = factorial * k
	7.	    k = k + 1
	8.	Write “N! is ”
	9.	Write factorial

##1.  Read number
number = input("Enter N :")
number = int(number)

##2.  Set factorial = 1
factorial = 1

##3.  Set k = 1 (k means the count)
k = 1

while k <= number:
	factorial = factorial * k
	k = k+1

print("N! is " + str(factorial))
'''

''' Question 1)

k = 1
total = 0

while k < 10:
	k = k *2
	total = total + k

print(total)

'''

''' Question 2)

m = 0
n = 5
t = 100

while m<n:
	if m < 2:
		t = t + 100
	else:
		t = t // 7
	m = m+1
print(t)

''' 



