EE = True
while EE:
	print("\n\n'''''''''''Welcome To Calculater Modes'''''''''''''\n")
	print("For standerd mode     press 1")
	print("For programmer mode   press 2")
	print("For exit mode         press 0")



	number1 = int(input("\nEnter number1:"))
	number2 = int(input("Enter number2:"))

	x = int(input("\nEnter your mode:"))

	if x == 1:
		print("\n'''''''''''''welcome to standared mode''''''''''''''\n\n")
		print("add operation          press1")
		print("sub operation          press2")
		print("multi operation        press3")
		print("division operation     press4")
		print("Exit mode              press5")
		
		y = int(input("Enter your operation:"))
		
		if y == 1:
			print("add ="   ,  (number1+number2))
		elif y == 2:	
			print("sub ="   ,  (number1-number2))
		elif y == 3:
			print("multi =" ,  (number1*number2))
		elif y == 4:
			print("division =",(number1/number2))
		elif y == 5:
			print("you exit the standared mode")
		else:
			print("false")
	elif x == 2:
		print("\n'''''''''''''welcome to programmer mode''''''''''''''\n\n")
		print("AND operation=          press1")
		print("OR  operation=          press2")
		print("XOR operation=          press3")
		print("NOT operation=          press4")
		print("convert from decimal to binary   press5 ")
		print("Exit mode               press0")
		
		z = int(input("Enter your operation:"))
		
		if z == 1:
			print("AND ="   ,  (number1 & number2))
		elif z == 2: 	
			print("OR  ="   ,  (number1 | number2))
		elif z == 3:
			print("XOR ="   , (number1 ^ number2))
		elif z == 4:
			print(" To inverse number1    press 1 " )
			print(" To inverse number2    press 2 " )
			n = int(input("Enter n to make NOT op:"))
			if n == 1:
				print("NOT of number1 =",(~number1))
			elif n == 2:
				print("NOT of number2 =" ,(~number2))
		elif z == 5:
			print("if you want to convert num1 to decimal      press 1")		
			print("if you want to convert num2 to decimal      press 2")	
			f = int(input("enter your choice:"))
			if f == 1:
				print("Binary of number1 =" , bin(number1))
			elif f == 2 :
				print("Binary of number2 =" , bin(number2))
					
				
		elif z == 0:
			print("you exit the programmer mode")
		else:
			print("false")
			
	elif x == 0:
		print("EXIT CAL")
		break

else:
	EE = False