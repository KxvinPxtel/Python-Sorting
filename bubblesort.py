#Bubble Sort File
#To sort numbers in a bubble sort format and find the time it takes to do so
#November 24, 2021
#Kevin Patel

#List 1 = time 1 = 500 numbers 
#List 2 = time 2 = 5000 numbers
#List 3 = time 3 = 10,000 numbers

#Import Function(s) and Module(s)
import time

#Main Program

#Function to Bubble Sort the Three Lists
def bubble_sort(list1,list2,list3):

	#Declare Variables
	time_1_initial = 0
	time_2_initial = 0
	time_3_initial = 0
	time_1_final = 0
	time_2_final = 0
	time_3_final = 0
	bubble_time_difference_1 = 0
	bubble_time_difference_2 = 0
	bubble_time_difference_3 = 0
	bubble_switches_1 = 0
	bubble_switches_2 = 0
	bubble_switches_3 = 0
	bubble_comparisons_1 = 0
	bubble_comparisons_2 = 0
	bubble_comparisons_3 = 0

	#Find inital and final time for the code to run list 1
	time_1_initial = time.time()
	
	for i in range (0, len(list1) - 1):
		for j in range (0, len(list1) - 1 - i):
			bubble_comparisons_1 += 1
			if list1[j] > list1[j + 1]:
				bubble_switches_1 += 1
				list1[j], list1[j+1] = list1[j+1], list1[j]
	
	time_1_final = time.time()

	#find time difference for list 1
	bubble_time_difference_1 = time_1_final - time_1_initial


	#Find initial and final time for the code to run list 2
	time_2_initial = time.time()

	for i in range (0, len(list2) - 1):
		for j in range (0, len(list2) - 1 - i):
			bubble_comparisons_2 += 1
			if list2[j] > list2[j + 1]:
				bubble_switches_2 += 1
				list2[j], list2[j+1] = list2[j+1], list2[j]

	time_2_final = time.time()

	#find time difference for list 2
	bubble_time_difference_2 = time_2_final - time_2_initial

	
	#Find initial and final time for the code to run list 2
	time_3_initial = time.time()

	for i in range (0, len(list3) - 1):
		for j in range (0, len(list3) - 1 - i):
			bubble_comparisons_3 += 1
			if list3[j] > list3[j + 1]:
				bubble_switches_3 += 1
				list3[j], list3[j+1] = list3[j+1], list3[j]

	time_3_final = time.time()
	
	#find time difference for list 2
	bubble_time_difference_3 = time_3_final - time_3_initial

	#Round All Three Time Difference Values
	bubble_time_difference_1 = round(bubble_time_difference_1, 3)
	bubble_time_difference_2 = round(bubble_time_difference_2, 3)	
	bubble_time_difference_3 = round(bubble_time_difference_3, 3)

	#Return Time Values to Main Program
	return(bubble_time_difference_1, bubble_time_difference_2, bubble_time_difference_3, bubble_comparisons_1, bubble_comparisons_2,  bubble_comparisons_3, bubble_switches_1, bubble_switches_2, bubble_switches_3)