#Python Sorting Assignment #1
#Program to compare sorting methods, to see which sorting methods are faster or slower than the other
#November 23, 2021
#Kevin Patel

#Import functions from designated files
import createlists
import bubblesort
import heapsort
import clearconsole
import validint
import user_options

#Main Program

#Call validint file to figure out if user input is valid 
user_input = validint.valid_int()

#Create Three Lists
list_1 = createlists.list1()
list_2 = createlists.list2()
list_3 = createlists.list3()

#Call user options and send the valid user input and the lists to user option file
user_options.user_options(user_input,list_1,list_2,list_3)