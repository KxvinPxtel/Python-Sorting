#Heap Sort File
#To sort numbers in a heap sort format 
#November 24, 2021
#Kevin Patel

#List 1 = time 1 = 500 numbers 
#List 2 = time 2 = 5000 numbers
#List 3 = time 3 = 10,000 numbers

#Declare Variables
heap_switches_1 = 0
heap_switches_2 = 0
heap_switches_3 = 0
heap_comparisons_1 = 0
heap_comparisons_2 = 0
heap_comparisons_3 = 0


#Main Program

#Function to Heap sort list 1
def heap_sort_1(list1):
	n = len(list1)
	for i in range(n // 2 - 1, -1, -1):
		heapify_1(list1, n, i)
	for i in range(n-1, 0, -1):
		list1[i], list1[0] = list1[0], list1[i] 
		heapify_1(list1, i, 0)

def heapify_1(list1, n, i):
	global heap_switches_1 
	global heap_comparisons_1 

	largest = i 
	l = 2 * i + 1 
	r = 2 * i + 2 

	heap_comparisons_1+=1
	if l < n and list1[i] < list1[l]:
		largest = l

	heap_comparisons_1+=1
	if r < n and list1[largest] < list1[r]:
		largest = r

	if largest != i:
		list1[i],list1[largest] = list1[largest],list1[i] 
		heap_switches_1 += 1
		heapify_1(list1, n, largest)
	
	return(heap_comparisons_1, heap_switches_1, list1)


#Function to Heap sort list 2
def heap_sort_2(list2):
	n = len(list2)
	for i in range(n // 2 - 1, -1, -1):
		heapify_2(list2, n, i)
	for i in range(n-1, 0, -1):
		list2[i], list2[0] = list2[0], list2[i] 
		heapify_2(list2, i, 0)
	
def heapify_2(list2, n, i):
	global heap_switches_2 
	global heap_comparisons_2 

	largest = i 
	l = 2 * i + 1 
	r = 2 * i + 2 

	heap_comparisons_2+=1
	if l < n and list2[i] < list2[l]:
		largest = l
			
	heap_comparisons_2+=1
	if r < n and list2[largest] < list2[r]:
		largest = r

	if largest != i:
		list2[i], list2[largest] = list2[largest],list2[i] 
		heap_switches_2 += 1
		heapify_2(list2, n, largest)
	
	return(heap_comparisons_2, heap_switches_2, list2)


#Function to Heap sort list 3
def heap_sort_3(list3):
	n = len(list3)
	for i in range(n // 2 - 1, -1, -1):
		heapify_3(list3, n, i)
	for i in range(n-1, 0, -1):
		list3[i], list3[0] = list3[0], list3[i] 
		heapify_3(list3, i, 0)

def heapify_3(list3, n, i):
	global heap_switches_3 
	global heap_comparisons_3 

	largest = i 
	l = 2 * i + 1 
	r = 2 * i + 2 

	heap_comparisons_3+=1
	if l < n and list3[i] < list3[l]:
		largest = l
			
	heap_comparisons_3+=1
	if r < n and list3[largest] < list3[r]:
		largest = r

	if largest != i:
		list3[i],list3[largest] = list3[largest],list3[i] 
		heap_switches_3 += 1
		heapify_3(list3, n, largest)
	
	return(heap_comparisons_3, heap_switches_3, list3)