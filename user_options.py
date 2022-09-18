#User_Options (If,else statements)
#Program to output certain decisions depending on what sorting method user wants to compare
#November 30, 2021
#Kevin Patel

#Import Function(s) and Module(s)
import createlists
import bubblesort
import heapsort
import quicksort
import radixsort
import clearconsole
import validint
import time

#Function to output what the user wants from the 1-5 choices
def user_options(user_input,list_1,list_2,list_3):
	
	#If user input is equal to 1
	if(user_input == 1):
		clearconsole.clearconsole()
		print("Please Wait One Moment!")
		time.sleep(2)
		clearconsole.clearconsole()

		#Send all three lists to the bubblesort file
		bubble_sorted_list = bubblesort.bubble_sort(list_1, list_2, list_3)

		bubble_time_difference_1 = bubble_sorted_list[0]
		bubble_time_difference_2 = bubble_sorted_list[1]
		bubble_time_difference_3 = bubble_sorted_list[2]
		bubble_comparisons_1 = bubble_sorted_list[3]
		bubble_comparisons_2 = bubble_sorted_list[4]
		bubble_comparisons_3 = bubble_sorted_list[5]
		bubble_switches_1 = bubble_sorted_list[6]
		bubble_switches_2 = bubble_sorted_list[7]
		bubble_switches_3 = bubble_sorted_list[8]

		#Print Bubble Sort Statements
		print("BUBBLE SORT:\n-----------------")
		print("Time Difference(s):\nList 1:", bubble_time_difference_1, "\nList 2:", bubble_time_difference_2, "\nList 3:", bubble_time_difference_3, "\n")
		print("Comparisons(#):\nList 1:", bubble_comparisons_1, "\nList 2:", bubble_comparisons_2, "\nList 3:", bubble_comparisons_3, "\n")
		print("Switches(#):\nList 1:", bubble_switches_1, "\nList 2:", bubble_switches_2, "\nList 3:", bubble_switches_3)


	#If user input is equal to 2
	elif(user_input == 2):
		clearconsole.clearconsole()
		print("Please Wait One Moment!")
		time.sleep(2)
		clearconsole.clearconsole()

		#Declare Variables
		time_1_initial = 0
		time_2_initial = 0
		time_3_initial = 0
		time_1_final = 0
		time_2_final = 0
		time_3_final = 0
		heap_time_difference_1 = 0
		heap_time_difference_2 = 0
		heap_time_difference_3 = 0

		#Call heap sort function and send list 1, time the initial and final time it takes to complete the sort. Then find the time difference
		time_1_initial = time.time()
		heap_sorted_list_1 = heapsort.heap_sort_1(list_1)
		time_1_final = time.time()
		heap_time_difference_1 = time_1_final - time_1_initial

		#Call heap sort function and send list 2, time the initial and final time it takes to complete the sort. Then find the time difference
		time_2_initial = time.time()
		heap_sorted_list_2 = heapsort.heap_sort_2(list_2)
		time_2_final = time.time()
		heap_time_difference_2 = time_2_final - time_2_initial
		
		#Call heap sort function and send list 3, time the initial and final time it takes to complete the sort. Then find the time difference
		time_3_initial = time.time()
		heap_sorted_list_3 = heapsort.heap_sort_3(list_3)
		time_3_final = time.time()
		heap_time_difference_3 = time_3_final - time_3_initial
		
		#Round All Three Time Values
		heap_time_difference_1 = round(heap_time_difference_1, 3)
		heap_time_difference_2 = round(heap_time_difference_2, 3)
		heap_time_difference_3 = round(heap_time_difference_3, 3)

		#Print Heap Sort Statements
		print("HEAP SORT:\n-----------------")
		print("Time Difference(s):\nList 1:", heap_time_difference_1, "\nList 2:", heap_time_difference_2, "\nList 3:", heap_time_difference_3, "\n")
		print("Comparisons(#):\nList 1:", heapsort.heap_comparisons_1, "\nList 2:", heapsort.heap_comparisons_2, "\nList 3:",heapsort.heap_comparisons_3, "\n")
		print("Switches(#):\nList 1:", heapsort.heap_switches_1, "\nList 2:", heapsort.heap_switches_2, "\nList 3:", heapsort.heap_switches_3)


	#If user input is equal to 3
	elif(user_input ==3):
		clearconsole.clearconsole()
		print("Please Wait One Moment!")
		time.sleep(2)
		clearconsole.clearconsole()

		#Declare Variables
		time_1_initial = 0
		time_2_initial = 0
		time_3_initial = 0
		time_1_final = 0
		time_2_final = 0
		time_3_final = 0
		quick_time_difference_1 = 0
		quick_time_difference_2 = 0
		quick_time_difference_3 = 0

		#Call quick sort function and send list 1, time the initial and final time it takes to complete the sort. Then find the time difference
		time_1_initial = time.time()
		quick_sorted_list_1 = quicksort.quick_sort_1(list_1)
		time_1_final = time.time()
		quick_time_difference_1 = time_1_final - time_1_initial

		#Call quick sort function and send list 2, time the initial and final time it takes to complete the sort. Then find the time difference
		time_2_initial = time.time()
		quick_sorted_list_2 = quicksort.quick_sort_2(list_2)
		time_2_final = time.time()
		quick_time_difference_2 = time_2_final - time_2_initial

		#Call quick sort function and send list 3, time the initial and final time it takes to complete the sort. Then find the time difference
		time_3_initial = time.time()
		quick_sorted_list_3 = quicksort.quick_sort_3(list_3)
		time_3_final = time.time()
		quick_time_difference_3 = time_3_final - time_3_initial
		
		#Round All Three Time Values
		quick_time_difference_1 = round(quick_time_difference_1, 3)
		quick_time_difference_2 = round(quick_time_difference_2, 3)
		quick_time_difference_3 = round(quick_time_difference_3, 3)

		#Print Quick Sort Statements
		print("QUICK SORT:\n-----------------")
		print("Time Difference(s):\nList 1:", quick_time_difference_1, "\nList 2:", quick_time_difference_2, "\nList 3:", quick_time_difference_3, "\n")
		print("Comparisons(#):\nList 1:", quicksort.quick_comparisons_1, "\nList 2:", quicksort.quick_comparisons_2, "\nList 3:",quicksort.quick_comparisons_3, "\n")
		print("Switches(#):\nList 1:", quicksort.quick_switches_1, "\nList 2:", quicksort.quick_switches_2, "\nList 3:", quicksort.quick_switches_3)


	#If user input is equal to 4
	elif(user_input == 4):
		clearconsole.clearconsole()
		print("Please Wait One Moment!")
		time.sleep(2)
		clearconsole.clearconsole()

		#Declare Variables
		time_1_initial = 0
		time_2_initial = 0
		time_3_initial = 0
		time_1_final = 0
		time_2_final = 0
		time_3_final = 0
		radix_time_difference_1 = 0
		radix_time_difference_2 = 0
		radix_time_difference_3 = 0

		#Call radix sort function and send list 1, time the initial and final time it takes to complete the sort. Then find the time difference
		time_1_initial = time.time()
		radix_sorted_list_1 = radixsort.radix_sort_1(list_1)
		time_1_final = time.time()
		radix_time_difference_1 = time_1_final - time_1_initial

		#Call radix sort function and send list 2, time the initial and final time it takes to complete the sort. Then find the time difference
		time_2_initial = time.time()
		radix_sorted_list_2 = radixsort.radix_sort_2(list_2)
		time_2_final = time.time()
		radix_time_difference_2 = time_2_final - time_2_initial

		#Call radix sort function and send list 3, time the initial and final time it takes to complete the sort. Then find the time difference
		time_3_initial = time.time()
		radix_sorted_list_3 = radixsort.radix_sort_3(list_3)
		time_3_final = time.time()
		radix_time_difference_3 = time_3_final - time_3_initial
		
		#Round All Three Time Values
		radix_time_difference_1 = round(radix_time_difference_1, 3)
		radix_time_difference_2 = round(radix_time_difference_2, 3)
		radix_time_difference_3 = round(radix_time_difference_3, 3)

		#Print Radix Sort Statements
		print("RADIX SORT:\n-----------------")
		print("Time Difference(s):\nList 1:", radix_time_difference_1, "\nList 2:", radix_time_difference_2, "\nList 3:", radix_time_difference_3, "\n")
		print("Comparisons(#):\nList 1:", radixsort.radix_comparisons_1, "\nList 2:", radixsort.radix_comparisons_2, "\nList 3:",radixsort.radix_comparisons_3, "\n")
		print("Switches(#):\nList 1:", radixsort.radix_switches_1, "\nList 2:", radixsort.radix_switches_2, "\nList 3:", radixsort.radix_switches_3)