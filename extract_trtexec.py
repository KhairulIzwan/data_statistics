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
# https://realpython.com/python-csv/#writing-csv-files-with-csv
# https://www.geeksforgeeks.org/python-exit-commands-quit-exit-sys-exit-and-os-_exit/
# https://pynative.com/print-pattern-python-examples/
# https://www.geeksforgeeks.org/python-iterate-multiple-lists-simultaneously/
# https://www.w3resource.com/python-exercises/python-basic-exercise-99.php

# -------------------------------------------------
# import the necessary packages
import argparse
from itertools import groupby
import sys
import csv
import os
from datetime import datetime

os.system('clear')
os.system('tree')

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", required=True,
	help="path to input data")
args = vars(ap.parse_args())

#class Extract(self):
#	def __init__(self):
#		pass
		
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
	"""Search for the given string in file and return lines number"""
	line_number = 0
	list_of_results = []
	# Open the file in read only mode
	with open(file_name, 'r') as read_obj:
		# Read all lines in the file one by one
		for line in read_obj:
			# For each line, check if line contains the string
			line_number += 1
			if string_to_search in line:
				# If yes, then add the line number
				list_of_results.append(line_number)
	# Return list of tuples line numbers
	return list_of_results

def search_multiple_strings_in_file(file_name, list_of_strings):
	"""Get line from the file along with line numbers, which contains any
	 string from the list"""
	line_number = 0
	list_of_results = []
	# Open the file in read only mode
	with open(file_name, 'r') as read_obj:
		# Read all lines in the file one by one
		for line in read_obj:
			line_number += 1
			# For each line, check if line contains any string from 
			# the list of strings
			for string_to_search in list_of_strings:
				if string_to_search in line:
					# If any string is found in line, then 
					# append that line along with line 
					# number in list
					list_of_results.append(line_number)
	# Return list of tuples line numbers
	return list_of_results

def matched_lines(file_name, list_of_strings):
	"""Checks required "Header" Dimensions"""
	matched = search_multiple_strings_in_file(file_name, list_of_strings)
	
	# The dimension equal?
	if len(matched) % len(list_of_strings) == 0:
		return True
	else:
		return False
		
def find_line_of_interest(file_name, string_to_search):
	""" """
	line_of_interest = []
	line_of_data = []
	interested = search_string_in_file(file_name, string_to_search)
	for i in interested:
		line_of_interest.append(i)
		
	return line_of_interest
	
def list_of_interest(listing, N):
	""" """
	list_of_interest = []
	for i in listing:
		list_of_interest.append(CoList[i-1][N::])
	
	return list_of_interest
	
def clean_data(listing):
	""" """
	condition = all_equal(listing)
	if all_equal(listing):
		return listing[0]
	else:
		# exits the program 
		print("[ERROR] Required headers are missing or in-balance...")
		print("[ERROR] Please check the file!")
		sys.exit("[ERROR] Files may be corrupted...")

#print(args["file"][6:-4])

# Opening a file 
file = open(args["file"],"r")

# Reading from file 
Content = file.read() 
CoList = Content.split("\n")

# Checks required "Header" Dimensions
# In our case, we required "=== Model Options ===", "=== Build Options ===", 
# "=== Inference Options ===", "=== Reporting Options ===" which is where our
# interested data "Format", "Prototxt", "Precision", "Iterations", "Batch" and
# "throughput" were placed
listHeader = 	[
		"=== Model Options ===", 
		"=== Build Options ===", 
		"=== Inference Options ===", 
		"=== Reporting Options ==="
		]
boolHeader = matched_lines(args["file"], listHeader)
if boolHeader:
	pass
else:
	# exits the program 
	print("[ERROR] Required headers are missing or in-balance...")
	sys.exit("[ERROR] Files may be corrupted...")

line_of_format = find_line_of_interest(args["file"], 'Format:')
line_of_prototxt = find_line_of_interest(args["file"], 'Prototxt:')
line_of_precision = find_line_of_interest(args["file"], 'Precision:')
line_of_iteration = find_line_of_interest(args["file"], 'Iterations:')
line_of_batch = find_line_of_interest(args["file"], 'Batch:')
line_of_throughput = find_line_of_interest(args["file"], 'throughput:')

list_of_format = list_of_interest(line_of_format, 34)
list_of_prototxt = list_of_interest(line_of_prototxt, 36)
list_of_precision = list_of_interest(line_of_precision, 37)
list_of_iteration = list_of_interest(line_of_iteration, 38)
list_of_batch = list_of_interest(line_of_batch, 26)
list_of_throughput = list_of_interest(line_of_throughput, 38)

# Checking for purist data
# Ensure same "Format", "Prototxt", "Precision", "Iterations" were used
usedFormat = clean_data(list_of_format)
usedPrototxt = clean_data(list_of_prototxt)
usedPrecision = clean_data(list_of_precision)
usedIteration = clean_data(list_of_iteration)

# Summary
print("*" * 15 + " SUMMARY " + "*" * 15)
print("Format: %s" % usedFormat)
print("Prototxt: %s" % usedPrototxt)
print("Precision: %s" % usedPrecision)
print("Iteration: %s" % usedIteration)
print("Throughput:")

for (i, j) in zip(list_of_batch, list_of_throughput):
	print("%s: %s" % (i, j))

print("*" * 40)

# Save a copy
# datetime object containing current date and time
now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%B %d, %Y %H:%M:%S")
#newFilename = args["file"][:-4] + '.xls'
newFilename = args["file"][:-4] + "-" + dt_string +'.csv'
 
with open(newFilename, mode='w') as extract_file:
	extract_writer = csv.writer(
					extract_file, 
					delimiter=',', 
					quotechar='"', 
					quoting=csv.QUOTE_MINIMAL
					)

	extract_writer.writerow(["Format", usedFormat])
	extract_writer.writerow(["Prototxt", usedPrototxt])
	extract_writer.writerow(["Precision", usedPrecision])
	extract_writer.writerow(["Iteration", usedIteration])
	extract_writer.writerow(["Throughput"])
	
	for (i, j) in zip(list_of_batch, list_of_throughput):
		extract_writer.writerow([i, j])
		
print("[INFO] Extracted files were save in: %s" % newFilename)
os.system('tree')
