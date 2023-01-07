

Goods_amounts = {
    "apple"  :  "50",
    "banana" :  "70",  
    "orange" :  "60",
}
Goods_price = {
    "apple"  :  "20",
    "banana" :  "10",  
    "orange" :  "5",
}

print("\n'''''''''welcome To Grocery_shop'''''''''''\n\n")
print("for grocery mode      press1")
print("for customer mode     press2")
print("for exit mode         press0")

while 1:

	n = int(input("\nenter your mode:"))
	if n == 1:
		print("\n\n'''''''welcome to owner page ''''''''\n\n")
		print("show type of furits       press1")
		print("change price              press2")
		print("for exit mode             press0")
		while 1:
		
			y = int(input("\nenter your choice:"))
			if   y == 1:
				print("PRICES :")
				for items,values in Goods_price.items():
						print(items,"=",values)
				print("AMOUNTS:")
				for items,values in Goods_amounts.items():
						print(items,"=",values)
				
			elif y == 2:
				
				print("\n To edite price   press1")
				print(" To edite amount    press2")
				
				while 1:
					print("\n\n'''''''welcome to mode 2'''''''\n\n")
					k = int(input("edite ="))
					if k == 1:
						print("edite price:")
						product = input("product:")
						if  product == "apple":
							new_price =int(input("enter new price:"))
							Goods_price["apple"]= new_price
							print()
						elif product == "banana":
							new_price =int(input("enter new price:"))
							Goods_price["banana"]= new_price
							print()
						elif product == "orange":
							new_price =int(input("enter new price:"))
							Goods_price["orange"]= new_price
							print()
						else:
							print("wrong type")
							break
					elif k == 2:
						print("edite amount:")
						product = input("product:")
						if  product == "apple":
							new_amount =int(input("enter new amount:"))
							Goods_amounts["apple"]=new_amount
							print()
						elif product == "banana":
							new_amount =int(input("enter new amount:"))
							Goods_amounts["banana"]=new_amount
							print()
						elif product == "orange":
							new_amount =int(input("enter new amount:"))
							Goods_amounts["orange"]=new_amount
							print()
							break
						else:
							print("wrong type")
							break
			elif  y == 0:
				print("exit from owner page")
				break
			else:
				print("wrong enter")
	elif n==2:	
		print("\n\n'''''''''''''' welcome to customer mode''''''''''''''\n\n")
		print("To show menu       press1")
		print("To buy             press2")
		print("To exit            press0")
		while 1:
			m = int(input("\nenter your option:"))
			if m == 1:
				print("amounts :")
				for items ,values in Goods_amounts.items():
					print(items ,"=", values)
			
				print("prices :")
				for items,values in Goods_price.items():
					print(items ,"=", values)
			
				print()
			
			elif m==2:
				print("enter product and amount :")
				while 1:
					product = input("product or cost:")
					if product == "apple":
						amount = int(input("enter amount :"))
						if(amount > Goods_amounts["apple"]):
							print("we dont have this quantaty")
						else :
							cost = cost + (Goods_amounts["apple"]* amount)
							Goods_amounts["apple"] = Goods_amounts["apple"] - amount
							print()
			
					elif product == "banana":
						amount = int(input("enter amount :"))
						if(amount>Goods_amounts["banana"]):
							print("we dont have this quantaty")
						else :
							cost = cost + (Goods_amounts["banana"]* amount)
							Goods_amounts["banana"] = Goods_amounts["banana"] - amount
							print()
			
					elif product == "orange":
						amount = int(input("enter amount :"))
						if(amount>Goods_amounts["orange"]):
							print("we dont have this quantaty")
						else :
							cost = cost + (Goods_amounts["orange"]* amount)
							Goods_amounts["orange"] = Goods_amounts["orange"] - amount
							print()
					elif product == "cost":
						print("total cost = " ,cost)
			
			
			
					else :
						print("This product dont exist")
			elif m==0:
				print("exit from customer mode")
				break
			else:
				print("wrong choice")
	elif n==0:
		print("exit from program")
		break
	else:
		print("wrong choice")
		break








	
			
			