#Quick Sort File
#To sort numbers in a quick sort format
#December 2, 2021
#Kevin Patel

#List 1 = time 1 = 500 numbers
#List 2 = time 2 = 5000 numbers
#List 3 = time 3 = 10,000 numbers

#Declare Variables
quick_switches_1 = 0
quick_switches_2 = 0
quick_switches_3 = 0
quick_comparisons_1 = 0
quick_comparisons_2 = 0
quick_comparisons_3 = 0

#Main Program

#Function to Quick sort list 1
def quick_sort_1(list1):
	global quick_switches_1
	global quick_comparisons_1

	elements = len(list1)
  
	#Base case
	if elements < 2:
		quick_comparisons_1 = quick_comparisons_1 + 1
		return list1
  
	current_position = 0 #Position of the partitioning element
 
	for i in range(1, elements): #Partitioning loop
		if list1[i] <= list1[0]:
			current_position += 1
			temp = list1[i]
			list1[i] = list1[current_position]
			list1[current_position] = temp
			quick_switches_1 = quick_switches_1 + 1

	temp = list1[0]
	list1[0] = list1[current_position]
	list1[current_position] = temp #Brings pivot to it's appropriate position
	
	left = quick_sort_1(list1[0:current_position]) #Sorts the elements to the left of pivot
	right = quick_sort_1(list1[current_position+1:elements]) #sorts the elements to the right of pivot
 
	list1 = left + [list1[current_position]] + right #Merging everything together
	return list1


#Function to Quick sort list 2
def quick_sort_2(list2):
	global quick_switches_2
	global quick_comparisons_2

	elements = len(list2)
  
   #Base case
	if elements < 2:
		quick_comparisons_2 = quick_comparisons_2 + 1
		return list2
  
	current_position = 0 #Position of the partitioning element
 
	for i in range(1, elements): #Partitioning loop
		if list2[i] <= list2[0]:
			current_position += 1
			temp = list2[i]
			list2[i] = list2[current_position]
			list2[current_position] = temp
			quick_switches_2 = quick_switches_2 + 1
 
	temp = list2[0]
	list2[0] = list2[current_position]
	list2[current_position] = temp #Brings pivot to it's appropriate position
  
	left = quick_sort_2(list2[0:current_position]) #Sorts the elements to the left of pivot
	right = quick_sort_2(list2[current_position+1:elements]) #sorts the elements to the right of pivot
 
	list2 = left + [list2[current_position]] + right #Merging everything together
	return list2


#Function to Quick sort list 3
def quick_sort_3(list3):
	global quick_switches_3
	global quick_comparisons_3

	elements = len(list3)
  
	#Base case
	if elements < 2:
		quick_comparisons_3 = quick_comparisons_3 + 1
		return list3
  
	current_position = 0 #Position of the partitioning element
 
	for i in range(1, elements): #Partitioning loop
		if list3[i] <= list3[0]:
			current_position += 1
			temp = list3[i]
			list3[i] = list3[current_position]
			list3[current_position] = temp
			quick_switches_3 = quick_switches_3 + 1
 
	temp = list3[0]
	list3[0] = list3[current_position]
	list3[current_position] = temp #Brings pivot to it's appropriate position
  
	left = quick_sort_3(list3[0:current_position]) #Sorts the elements to the left of pivot
	right = quick_sort_3(list3[current_position+1:elements]) #sorts the elements to the right of pivot
 
	list3 = left + [list3[current_position]] + right #Merging everything together
	return list3