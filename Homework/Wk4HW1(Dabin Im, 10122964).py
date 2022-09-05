##	Pseudocode 
#	1)	Write "Enter weight "                 (Ask the user for weight in kilograms)
#	2)	Read the weight in kilograms.
#	3)  Write "Enter height "                 (Ask the user for height in centimeters)
#	4)	Read the height in centimeters.
#	5)	height = height * 0.01                  (Change the unit from centimeters to meters [1m = 100cm]) 
#	6)	bmi = weight / height / height          (By using formula for Body Mass Index, calculate the bmi.  ※ Body Mass Index = weight * (1/height)^2) 
#   7)  Write "Your BMI is "
#   8)  Write bmi 
#	9)	If	    bmi < 18.5					    do step 10
#	10)	        Write "You are Underweight !     	
#	11)	Else if	bmi >= 18.5 and bmi <= 24.9     do step 12
#	12)			Write "You are Normal !"
#	13)	Else if	bmi >= 25.0 and bmi <= 29.9     do step 14
#	14)			Write "You are Overweight !"    
#	15)	Else    							    do step 16	
#	16)			Write "You are Obese!"


##	Python Code
weight = eval(input("Enter weight[kg]: "))      ## Ask the user for weight in kilograms
height = eval(input("Enter height[cm]: "))      ## Ask the user for height in centimeters
height = height * 0.01                          ## Change the unit from centimeters to meters [1m = 100cm]
bmi = weight / height / height					## By using formula for Body Mass Index, calculate the bmi.  ※ Body Mass Index = weight * (1/height)^2
print("Your BMI is", round(bmi, 2))
if		bmi < 18.5:
		print("You are Underweight !")  
elif	bmi >= 18.5 and bmi <= 24.9:
		print("You are Normal !")
elif	bmi >= 25.0 and bmi <= 29.9:
		print("You are Overweight !")   
else:
		print("You are Obese!")
