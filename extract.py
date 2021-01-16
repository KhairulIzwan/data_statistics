#!/usr/bin/env bash

# -------------------------------------------------

# Usage: Read text files (.txt) and extracting important data's
# Author: Khairul Izwan Bin Kamsani (wansnap@gmail.com)

# References: 
# https://www.pythontutorial.net/python-basics/python-read-text-file/
# https://www.geeksforgeeks.org/count-number-of-lines-in-a-text-file-in-python/
# https://thispointer.com/python-search-strings-in-a-file-and-get-line-numbers-of-lines-containing-the-string/
# https://stackoverflow.com/questions/3844801/check-if-all-elements-in-a-list-are-identical
# https://stackoverflow.com/questions/23655005/printing-boolean-values-true-false-with-the-format-method-in-python

# -------------------------------------------------
from itertools import groupby

def all_equal(iterable):
	g = groupby(iterable)
	return next(g, True) and not next(g, False)

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
	# Open the file in read only mode
	with open(file_name, 'r') as read_obj:
		# Read all lines in the file one by one
		for line in read_obj:
			line_number += 1
			# For each line, check if line contains any string from the list of strings
			for string_to_search in list_of_strings:
				if string_to_search in line:
					# If any string is found in line, then append that line along with line number in list
					list_of_results.append((string_to_search, line_number, line.rstrip()))
	# Return list of tuples containing matched string, line numbers and lines where string is found
	return list_of_results

# Opening a file 
file = open("GPU-int8_resnet-50.txt","r") 
Counter = 0

# Reading from file 
Content = file.read() 
CoList = Content.split("\n")

# Find "Format"
matched_format = search_string_in_file('GPU-int8_resnet-50.txt', 'Format:')
# Find "Prototxt"
matched_prototxt = search_string_in_file('GPU-int8_resnet-50.txt', 'Prototxt')
# Find "Precision"
matched_precision = search_string_in_file('GPU-int8_resnet-50.txt', 'Precision')
# Find "Iterations"
matched_iterations = search_string_in_file('GPU-int8_resnet-50.txt', 'Iterations')
# Find "Batch"
matched_batch = search_string_in_file('GPU-int8_resnet-50.txt', 'Batch')
# Find "throughput"
matched_throughput = search_string_in_file('GPU-int8_resnet-50.txt', 'throughput')

line_of_format = []
line_of_prototxt = []
line_of_precision = []
line_of_iteration = []
line_of_batch = []
line_of_throughput = []

for elem in matched_format:
	line_of_format.append(elem[0])
	
for elem in matched_prototxt:
	line_of_prototxt.append(elem[0])
	
for elem in matched_precision:
	line_of_precision.append(elem[0])
	
for elem in matched_iterations:
	line_of_iteration.append(elem[0])
	
for elem in matched_batch:
	line_of_batch.append(elem[0])
	
for elem in matched_throughput:
	line_of_throughput.append(elem[0])

list_of_format = []
list_of_prototxt = []
list_of_precision = []
list_of_iteration = []
list_of_batch=[]
list_of_throughput=[]

# "Format" is equal?
#print("[INFO] Checking the 'Format' used...")
for i in line_of_format:
	list_of_format.append(CoList[i-1][34::])

condition = all_equal(list_of_format)
if all_equal(list_of_format):
	print("[INFO] Format: %s" % list_of_format[0])
else:
	print("[ERROR] Please check the file!")
	print("List of 'Format' used were mixed!")

# "Prototxt" is equal?
#print("[INFO] Checking the 'Prototxt' used...")
for i in line_of_prototxt:
	list_of_prototxt.append(CoList[i-1][36::])

condition = all_equal(list_of_prototxt)
if all_equal(list_of_prototxt):
	print("[INFO] Prototxt: %s" % list_of_prototxt[0])
else:
	print("[ERROR] Please check the file!")
	print("List of 'Prototxt' used were mixed!")

# "Precisions" is equal?
#print("[INFO] Checking the 'Precisions' used...")
for i in line_of_precision:
	list_of_precision.append(CoList[i-1][37::])

condition = all_equal(list_of_precision)
if all_equal(list_of_precision):
	print("[INFO] Precisions: %s" % list_of_precision[0])
else:
	print("[ERROR] Please check the file!")
	print("List of 'Precisions' used were mixed!")
	
# "Iterations" is equal?
#print("[INFO] Checking the 'Iterations' used...")
for i in line_of_iteration:
	list_of_iteration.append(CoList[i-1][38::])

condition = all_equal(list_of_iteration)
if all_equal(list_of_precision):
	print("[INFO] Iterations: %s" % list_of_iteration[0])
else:
	print("[ERROR] Please check the file!")
	print("List of 'Iterations' used were mixed!")
	
# "Batch" is equal?
#print("[INFO] Checking the 'Iterations' used...")
for i in line_of_batch:
	list_of_batch.append(CoList[i-1][26::])
	
print(list_of_batch)

# "throughput" is equal?
#print("[INFO] Checking the 'Iterations' used...")
for i in line_of_throughput:
	list_of_throughput.append(CoList[i-1][38::])
	
print(list_of_throughput)
