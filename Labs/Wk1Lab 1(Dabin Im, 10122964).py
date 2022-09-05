#region LAB 1

###########################################################################################################################
################################################                           ################################################  
################################################        PseudoCodes        ################################################
################################################                           ################################################
###########################################################################################################################


	#region	1. Write Pseudocodes for the following problems


	#		a. Calculate the area of a triangle from its base and height.
	#		1)	Write "Enter the Base"											
	#		2)	Read The Base.													
	#		3)	Write "Enter the Height"										
	#		4)	Read The Height.													
	#		5)	Area =  B * H * 1/2 			
	#		6)	Write "The area of this triangle is "
	#		7)	Write Area						
																				
																					
	#		b. Calculate the area of a rectangle, ask user for necessary inputs
	#		1)	Write "Enter the Base"	
	#		2)	Read The Base.
	#		3)	Write "Enter the Height"										
	#		4)	Read The Height.	
	#		5)	Area =  Base * Height
	#		6)	Write "The area of this rectangle is "
	#		7)	Write Area	


	#		c. Ask the user to input an integer and decide if its odd or even.
	#		1)	Write "Enter the number"
	#		2)	Read number
	#		3)	remainder = Remainder from number / 2
	#		4)	If remainder is equal to 0 then do step 5
	#		5)		Write "This number is Even."
	#		6)	Else do step 7
	#		7)		Write "This number is Odd."


	#		d. Compare two peoples age and decide who is older and who is younger or are they of the same age.
	#		1)	Write "Enter the age of person A"
	#		2)	Read the age of person A.
	#		3)	Write "Enter the age of person B"
	#		2)	Read the age of person B.
	#		4)	If the value user have inputted is Integer, determines which The value is bigger 
	#			between two values by using conditional statement and inequality sign.


	#		e. Ask user to Read the time of the day (just the hour as an integer between 0 and 23) and decide 
	#		   whether its morning (between 0 and 12), afternoon (between 12 and 17), evening 
	#		   (between 17 and 19), or night (between 20 and 23).

	#		1)	Ask user to Read the time of the day between 0 and 23 by using The "print()" function.
	#		2)	Read a integer.
	#		3)	The software have to check the input whether The Integer is or not 
	#			by using the ".isdigit()" Function
	#		4)	If the value user have inputted is Integer, the software have to distinguish the time of the day. 
	#			So, software is able to distinguish the time by using if-else statement.


	#		f. Display the text “I love programming!” N times on the screen where N is decided by the user.
	#		1)	Ask user to input a integer how many texts display on the screen by using The "print()" function.
	#		2)	Read the integer.
	#		3)	The software have to check the input whether The Integer is or not 
	#			by using the ".isdigit()" Function
	#		4)	If the value user have inputted is Integer, Invoke the print function within the statement 
	#			which is repeating statements such as "for" or "while" statement.


	#		g. Calculate the factorial of N where N is input by the user.
	#		1)	Ask user to input a integer by using The "print()" function.
	#		2)	Read the Integer.
	#		3)	The software have to check the input whether The Integer is or not 
	#			by Using The ".isdigit()" Function
	#		4)	If the value user have inputted is Integer, multiply values and store the result within the statement 
	#			which is repeating statements such as "for" or "while" statement.


	#endregion


	#region	2.	Write Pseudocodes for the following problems
	
	
	#		a.	Calculate the area and perimeter of a circle whose radius is N.
	#		1)	Write “Enter Radius”
	#		2)	Read radius.
	#		3)	area = radius * radius * 3.14 or π
	#		4)	Write “the area of this triangle is ”
	#		5)  Write area
	
	
	
	#		b.	Calculate the area and perimeter of a hexagon whose side length is N.
	#		1)	Write “Enter length”
	#		2)	Read length.
	#		3)	area =  (3 * √3 * length^2) / 2.
	#		4)	Write “the area of this hexagon is ”
	#		5)  Write area
	#		
	
	
	#		c.	Calculate the sum, difference, absolute difference, product, quotient, and remainder of two input integers.
	#		1)	Write “Enter an Integer”
	#		2)	Read an Integer a
	#		3)	Write “Enter an Integer”
	#		4)	Read an Integer b
	#		5)	sum = a + b
	#		6)	_isBiggerThanB = a > b
	#		7)	_isBiggerThanB_ABS = a > b
	#		8)	product = a * b
	#		9)	quotient = a / b
	#		10)	remainder = a % b
	#		11)	Write “the sum, difference, absolute difference, product, quotient, and remainder of two input integers is ”
	#		12) Write sum, difference, absolute difference, product, quotient, and remainder
	
	
	
	#		d.	Calculate the distance between two points x1,y1 and x2,y2 where x1,y1,x2,y2 is given as input.
	#		1)	Write “Enter the point a”
	#		2)	Read the point a.
	#		3)	Write “Enter the point b”
	#		4)	Read the point b.
	#		5)  distance = (x2 - x1)^2  + (y2 - y1)^2
	#		6)  Write “the distance between two points x1,y1 and x2,y2 where x1,y1,x2,y2 is ” 
	#		7)	Write distance
	
	
	
	#		e.	Ask a user to enter an integer. If the number is between 0 and 9 inclusive output the word “blue”. 
	#			If the number is between 10 and 19 inclusive output the word “red”. If the number is between 20 and 29 inclusive, 
	#			output the word “green”. Otherwise output “invalid color code”.
	#		
	#		1)	Write “Enter an Integer Color”
	#		2)	Read the Integer iColor
	#		3)	validColor		= iColor / 10
	#		4)	if				validColor == 0		then		Write “blue”
	#		5)	Otherwise if	validColor == 1		then		Write “red”
	#		6)	Otherwise if	validColor == 2		then		Write “green”
	#		7)	Otherwise							then		Write “invalid color code”
	
	
	
	#		f.	Read two integers a and b and output “Makes 10” if either a or b is 10 or (a+b) is 10, otherwise output “Does not make 10”.
	#		1)	Write “Enter an Integer a”
	#		2)	Read the Integer a
	#		3)	Write “Enter an Integer b”
	#		4)	Read the Integer b
	#		5)	sum		= a + b
	#		6)	if		sum == 10		then		Write “Makes 10”
	#		7)	Otherwise				then		Write “Does not make 10”
	
	
	
	#		g.	Read in three integers and write them all in sorted order (smallest to largest).
	#		1)	Write “Enter an Integer a”
	#		2)	Read the Integer a
	#		3)	Write “Enter an Integer b”
	#		4)	Read the Integer b
	#		5)	Write “Enter an Integer c”
	#		6)	Read the Integer c
	#		7)	Declare a repeating statement for the three numbers.
	#		8)	Compare the values sequentially.
	#		9)	Swap the value if it is the minimum value.
	
	
	
	#		h.	When squirrels get together for a party, they like to have cigars. 
	#			A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. 
	#			Unless it is the weekend, in which case there is no upper bound on the number of cigars. 
	#			Read in the number of cigars and the day of the week as an integer 
	#			(1 = Monday, 2 = Tuesday, … 6 and 7 are Saturday and Sunday respectively and are also weekend days). 
	#			Output either “Successful Party” or “Unsuccessful Party” based on number of cigars and day of the week.
	
	#		1)	Write “Enter an Integer Cigars”
	#		2)	Read the Integer Cigars.
	#		3)	Write “Enter an Integer Day”
	#		4)	Read the Integer Day.
	#		5)	if				Day >= 1 and Day < 6		then		Write “Successful Party”
	#		6)	Otherwise									then		
	#		7)												if			Cigars >= 40 and Cigars <= 60		then		Write “Successful Party”
	#		8)												Otherwise										then		Write “Unsuccessful Party”


	
	#		i.	Calculate the sum of all odd integers from 1 to N where N is an integer input by the user.
	#		1)	Write “Enter an Integer N”
	#		2)	Read the Integer N.
	#		4)	Declare integer sum
	#		5)	for	x in range(N):	
	#		6)	if		x % 2 > 0		then		sum += x
	#		7)	Otherwise				then		continue												
	#		8)	Write “the sum of all odd integers from 1 to N is ”
	#		9)	Write sum
	
	
	
	#		j.	Calculate then sum of all integers input by the user until a negative number is entered 
	#			at which point display the sum and average of all numbers entered. 
	#			The negative number should not be counted towards the sum (or the average).

	#		1)	Declare While statement.	
	#		2)	Write “Enter an Integer N”
	#		3)	Read the Integer N.
	#		4)	Declare integer sum, count = 0
	#		5)	if		N < 0			then		break
	#		6)	Otherwise				then		sum += x, count++
	#		7)	When a negative number comes, calculate the sum and average of all numbers entered 											
	#		8)	Write “the sum and average of all numbers entered are ”
	#		9)	Write sum, average of all numbers entered
	
	
	
	#		k.	Determine if an input integer N is prime or not.
	#		1)	Write “Enter an Integer N”
	#		2)	Read the Integer N.
	#		3)	for i in reversed(range(N-1), 2):
	#		4)	if		N % i == 0		then		Write “integer N is prime”	break
	#		5)	Otherwise				then		continue

	
	
	
	#		l.	Display all prime numbers below N.
	#		1)	Write “Enter an Integer N”
	#		2)	Read the Integer N.
	#		3)	for i in range(2, range(N-1)):
	#		4)		for x in range(2, i):
	#		5)			if		i % x == 0			then		
	#												if		i == x		then	Write “integer N is prime”	break
	#												Otherwise			then									break	
	#		6)			Otherwise					continue
	
	
	
	#		m.	Display product, sum and average of all prime numbers below N.
	#		1)	Write “Enter an Integer N”
	#		2)	Read the Integer N.
	#		3)  product = 1
	#		4)	sum = 0
	#		4)	for i in range(2, range(N-1)):
	#		5)		for x in range(2, i):
	#		6)			if		i % x == 0			then		
	#												if		i == x		then	product *= x, sum += x			break
	#												Otherwise			then									break	
	#		7)			Otherwise					continue
	#		8)	When repeating statement has finished, Write " product, sum and average of all prime numbers below N is "
	#		9)	Write product, sum and average of all prime numbers below N



	#		n.	Read an integer N and output how many digits there are in N.
	#		1)	Write “Enter an Number”
	#		2)	Read the Number.
	#		3)  digits = 1 
	#		4)	count = 1
	#		5)	Repetition forever in steps 6 to 11
	#		6)		quotient = N / digits
	#		7)		if	quotient > 1					then	do steps 8 to 9
	#		8)			digits = digits * 10					(multifly 10 with digits and store the result in digits)
	#		9)			count = count + 1						(increase count by 1)
	#		10)		Otherwise							then	do step 11
	#		11)			stop repetition on line 5
	#		12)	Write " how many digits there are in N is "
	#		13)	Write count
	


	
	#		o.	Read an integer N and output the sum and average of all the digits in N.
	#		1)	Write “Enter an Number”
	#		2)	Read the Number.
	#		3)  digits = 1 
	#		4)	sum = 0
	#		5)	count = 1
	#		6)	Repetition forever in steps 7 to 13
	#		7)		quotient = N / digits
	#		8)		if	quotient > 1						then	do steps 9 to 11
	#		9)			digits = digits * 10						(multifly 10 with digits and replace old digits)
	#		10)			sum = sum + integer part of quotient		(add sum with integer part of quotient and store the result in sum)
	#		11)			count = count + 1							(increase count by 1)
	#		12)		Otherwise								then	do step 13	
	#		13)			stop repetition on line 6
	#		14)	Write "the sum is "
	#		15)	Write sum 
	#		16)	average = sum / count 
	#		17) Write "the average is "
	#		18) Write average 



	#endregion
	

###########################################################################################################################


#endregion
