#Valid Int File 
#To validate input from user and making sure the input is a valid choice
#Kevin Patel
#November 24, 2021

#Import Function and Module
import time #To delay outputting certain lines of code
import clearconsole #To clear the console

#A function to try to get valid choice integer values from user
def valid_int():
	#Variable
	x = 0 

	#Main Program
	while (x==0):
		try:
			#Getting input from user
			user_input = int(input("PLEASE CHOOSE ONE OF THE OPTIONS BELOW:\n(1) Bubble Sort\n(2) Heap Sort\n(3) Quick Sort\n(4) Radix Sort\n(5) Exit\n\n"))
			clearconsole.clearconsole()
			
			#If user input is between 1-4 then continue the program, if it is 5 then stop the program or if it is not any of them then make user enter a valid number
			if (user_input >= 1 and user_input <=4):
				x = 2
				return (user_input) #return the valid integer to the main program
			elif (user_input == 5):
				break
			else:
				x = 0
				clearconsole.clearconsole()
				print("Please input valid number values...") 
				time.sleep(0.8)
				clearconsole.clearconsole()
				
		#If string is entered tell user to input valid values 
		except ValueError:
			clearconsole.clearconsole()
			print("Please input valid number values...") 
			time.sleep(0.8)
			clearconsole.clearconsole()