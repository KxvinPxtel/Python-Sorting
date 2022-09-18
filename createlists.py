#Create Lists File
#Function to create three lists to use for sorting
#Kevin Patel
#November 24, 2021

#Import Function(s) and Module(s)
import random

#Main Program
#Function to create the three lists

#Function to create list 1
def list1():

	#Declare Variables
	counter_1 = 0
	counter_2 = 0
	list_number_1 = []

	#Open a file to write
	number_file = open("list1.txt", "w")

	for x in range(500):
		list_number_1.append(counter_1)
		counter_1 += 1
	
	random.shuffle(list_number_1)

	for j in range (500):
		number = list_number_1[counter_2]
		number_file.write("%d\n"%(number))
		counter_2 += 1

	number_file.close() 

	return(list_number_1)

#Function to create list 2
def list2():

	#Declare Variables
	counter_1 = 0
	counter_2 = 0
	list_number_2 = []

	#Open a file to write
	number_file = open("list2.txt", "w")

	for x in range(5000):
		list_number_2.append(counter_1)
		counter_1 += 1
	
	random.shuffle(list_number_2)

	for j in range (5000):
		number = list_number_2[counter_2]
		number_file.write("%d\n"%(number))
		counter_2 += 1

	number_file.close() 

	return(list_number_2)

#Function to create list 3
def list3():

	#Declare Variables
	counter_1 = 0
	counter_2 = 0
	list_number_3 = []

	#Open a file to write
	number_file = open("list3.txt", "w")

	for x in range(10000):
		list_number_3.append(counter_1)
		counter_1 += 1
	
	random.shuffle(list_number_3)

	for j in range (10000):
		number = list_number_3[counter_2]
		number_file.write("%d\n"%(number))
		counter_2 += 1

	number_file.close() 

	return(list_number_3)