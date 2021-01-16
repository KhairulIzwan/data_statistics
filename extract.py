#!/usr/bin/env bash

# -------------------------------------------------

# Usage: Read text files (.txt) and extracting important data's
# Author: Khairul Izwan Bin Kamsani (wansnap@gmail.com)

# References: 
# https://www.pythontutorial.net/python-basics/python-read-text-file/
# https://www.geeksforgeeks.org/count-number-of-lines-in-a-text-file-in-python/

# -------------------------------------------------

def check_if_string_in_file(file_name, string_to_search):
	""" Check if any line in the file contains given string """
	# Open the file in read only mode
	with open(file_name, 'r') as read_obj:
		# Read all lines in the file one by one
		for line in read_obj:
			# For each line, check if line contains the string
			if string_to_search in line:
				return True
	return False
	
def search_string_in_file(file_name, string_to_search):
	"""Search for the given string in file and return lines containing that string,
	along with line numbers"""
	line_number = 0
	list_of_results = []
	# Open the file in read only mode
	with open(file_name, 'r') as read_obj:
		# Read all lines in the file one by one
		for line in read_obj:
			# For each line, check if line contains the string
			line_number += 1
			if string_to_search in line:
				# If yes, then add the line number & line as a tuple in the list
				list_of_results.append((line_number, line.rstrip()))
	# Return list of tuples containing line numbers and lines where string is found
	return list_of_results
	
def search_multiple_strings_in_file(file_name, list_of_strings):
	"""Get line from the file along with line numbers, which contains any string from the list"""
	line_number = 0
	list_of_results = []
	list_of_results1 = []
	# Open the file in read only mode
	with open(file_name, 'r') as read_obj:
		# Read all lines in the file one by one
		for line in read_obj:
			line_number += 1
			# For each line, check if line contains any string from the list of strings
			for string_to_search in list_of_strings:
				if string_to_search in line and string_to_search == "=== Model Options ===":
					# If any string is found in line, then append that line along with line number in list
					list_of_results.append((string_to_search, line_number, line.rstrip()))
					list_of_results1.append((string_to_search, line_number+1, line.rstrip()))
	# Return list of tuples containing matched string, line numbers and lines where string is found
	return list_of_results, list_of_results1
	
def main():
#	print('*** Check if a string exists in a file *** ')
#	
#	# Check if string 'is' is found in file 'sample.txt'
#	if check_if_string_in_file('GPU-int8_resnet-50.txt', '=== Model Options ==='):
#		print('Yes, string found in file')
#	else:
#		print('String not found in file')
#		
#	print('*** Search for a string in file & get all lines containing the string along with line numbers ****')
#	
#	matched_lines = search_string_in_file('GPU-int8_resnet-50.txt', '=== Model Options ===')
#	print('Total Matched lines : ', len(matched_lines))
#	for elem in matched_lines:
#		print('Line Number = ', elem[0], ' :: Line = ', elem[1])
	
	print('*** Search for multiple strings in a file and get lines containing string along with line numbers ***')
	
	# search for given strings in the file 'sample.txt'
	matched_lines, matched_lines1 = search_multiple_strings_in_file('GPU-int8_resnet-50.txt', ['=== Model Options ===', '=== Build Options ===', '=== Inference Options ===', '=== Reporting Options ==='])
	print('Total Matched lines : ', len(matched_lines))
	for elem in matched_lines:
#		print('Word = ', elem[0], ' :: Line Number = ', elem[1], ' :: Line = ', elem[2])
#		print(elem[1], ' :: ', elem[2][25::])
		print(elem[2][25::])
	for elem in matched_lines1:
#		print('Word = ', elem[0], ' :: Line Number = ', elem[1], ' :: Line = ', elem[2])
#		print(elem[1], ' :: ', elem[2][25::])
		print(elem[1])

if __name__ == '__main__':
	main()

#matched_lines = search_string_in_file('GPU-int8_resnet-50.txt', '=== Model Options ===')
#matched_lines = search_string_in_file('int8_batch1.txt', '=== Model Options ===')

#print('Total Matched lines : ', len(matched_lines))
#for elem in matched_lines:
##	print('Line Number = ', elem[0], ' :: Line = ', elem[1])
#	print(elem[1].split("\n"))

## Opening a file 
#file = open("GPU-int8_resnet-50.txt","r") 
#Counter = 0

## Reading from file 
#Content = file.read() 
#CoList = Content.split("\n")

#print(Content)

#for i in CoList: 
#	if i: 
#		Counter += 1

#print("This is the number of lines in the file") 
#print(Counter)

##Format:
#print(CoList[2])

##Prototxt:
#print(CoList[4])

##Precision:
#print(CoList[11])

##Batch:
#print(CoList[27])

##throughput:
#print(CoList[80])

##Batch:
#print(CoList[121])

##throughput:
#print(CoList[161])

##Batch:
#print(CoList[202])

##throughput:
#print(CoList[240])

##Batch:
#print(CoList[281])

##throughput:
#print(CoList[318])

##Batch:
#print(CoList[359])

##throughput:
#print(CoList[395])

##Batch:
#print(CoList[436])

##throughput:
#print(CoList[472])

##Batch:
#print(CoList[513])

##throughput:
#print(CoList[549])
