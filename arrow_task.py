
x = int(input("n = "))

for n in range(0,x,1):
  for j in range(0,n+1) :
    print('* ', end="")
  print()

for n in range(x,1,-1):
  for j in range(1,n) :
    print('* ', end="")
  print()

import time
import os



size =    int(input("Enter the size of star: "))
loading = int(input("Enter no. of loading: "))

k = 0


while loading:
  os.system("cls")
  loading -= 1

  for i in range(0, size+1):
    for j in range(i):
      print("* ", end = "")
    print("")
  time.sleep(1)

  for i in range(0, size):
    for j in range(i,size-1):
      print("* ", end = "")
    print("")
  time.sleep(1)

  for i in range(0, size+1):
    for j in range(0,(size-i)+1):
      print(end = "  ")
    for l in range(i-1):
      print("* ",end = "")

    print("\r")
  time.sleep(1)


  for i in range(size+1,0,-1 ):
    for j in range(0,(size-i)+1):
      print(end = "  ")
    for l in range(i-1):
      print("* ",end = "")

    print("\r")
  time.sleep(1)


  for i in range(size , 0, -1):
    for j in range(1,(size - i)+1):
      print(end = "  ")

    while k != (2*i-1):
      print("* ", end = "")
      k += 1
    k = 0
    print("\r")
  time.sleep(1)


  for i in range(1, size + 1):
    for j in range(1,(size - i)+1):
      print(end = "  ")

    while k != (2*i-1):
      print("* ", end = "")
      k += 1

    k = 0
    print("\r")
  time.sleep(1)
	

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	