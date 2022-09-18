#Radix Sort File
#To sort numbers in a radix sort format
#December 11, 2021
#Kevin Patel

#List 1 = time 1 = 500 numbers
#List 2 = time 2 = 5000 numbers
#List 3 = time 3 = 10,000 numbers


#Declare Variables
radix_switches_1 = 0
radix_switches_2 = 0
radix_switches_3 = 0
radix_comparisons_1 = 0
radix_comparisons_2 = 0
radix_comparisons_3 = 0


#Main Program

#Function to Radix sort list 1
def radix_sort_1(list1):
	global radix_switches_1
	global radix_comparisons_1
	# Get maximum element
	max_element = max(list1)

	# Apply counting sort to sort elements based on place value.
	place = 1
	while max_element // place > 0:
		countingSort_1(list1, place)
		place *= 10

	return list1

# Using counting sort to sort the elements in the basis of significant places
def countingSort_1(list1, place):
	global radix_switches_1
	global radix_comparisons_1
	size = len(list1)
	output = [0] * size
	count = [0] * 10

	# Calculate count of elements
	for i in range(0, size):
		index = list1[i] // place
		count[index % 10] += 1

	# Calculate cumulative count
	for i in range(1, 10):
		count[i] += count[i - 1]
		

	# Place the elements in sorted order
	i = size - 1
	while i >= 0:
		index = list1[i] // place
		output[count[index % 10] - 1] = list1[i]
		count[index % 10] -= 1
		i -= 1


	for i in range(0, size):
		list1[i] = output[i]
		radix_switches_1 = radix_switches_1 + 1


#Function to Radix sort list 2
# Using counting sort to sort the elements in the basis of significant places
def countingSort_2(list2, place):
	global radix_switches_2
	global radix_comparisons_2
	size = len(list2)
	output = [0] * size
	count = [0] * 10

	# Calculate count of elements
	for i in range(0, size):
		index = list2[i] // place
		count[index % 10] += 1

	# Calculate cumulative count
	for i in range(1, 10):
		count[i] += count[i - 1]

	# Place the elements in sorted order
	i = size - 1
	while i >= 0:
		index = list2[i] // place
		output[count[index % 10] - 1] = list2[i]
		count[index % 10] -= 1
		i -= 1

	for i in range(0, size):
		list2[i] = output[i]
		radix_switches_2 = radix_switches_2 + 1


# Main function to implement radix sort
def radix_sort_2(list2):
	global radix_switches_2
	global radix_comparisons_2
	# Get maximum element
	max_element = max(list2)

	# Apply counting sort to sort elements based on place value.
	place = 1
	while max_element // place > 0:
		countingSort_2(list2, place)
		place *= 10

	return list2

#Function to Radix sort list 3
# Using counting sort to sort the elements in the basis of significant places
def countingSort_3(list3, place):
	global radix_switches_3
	global radix_comparisons_3
	size = len(list3)
	output = [0] * size
	count = [0] * 10

	# Calculate count of elements
	for i in range(0, size):
		index = list3[i] // place
		count[index % 10] += 1

	# Calculate cumulative count
	for i in range(1, 10):
		count[i] += count[i - 1]

	# Place the elements in sorted order
	i = size - 1
	while i >= 0:
		index = list3[i] // place
		output[count[index % 10] - 1] = list3[i]
		count[index % 10] -= 1
		i -= 1

	for i in range(0, size):
		list3[i] = output[i]
		radix_switches_3 = radix_switches_3 + 1



# Main function to implement radix sort
def radix_sort_3(list3):
	global radix_switches_3
	global radix_comparisons_3
	# Get maximum element
	max_element = max(list3)

	# Apply counting sort to sort elements based on place value.
	place = 1
	while max_element // place > 0:
		countingSort_3(list3, place)
		place *= 10

	return list3