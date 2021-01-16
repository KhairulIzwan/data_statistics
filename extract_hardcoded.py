#!/usr/bin/env bash

# -------------------------------------------------

# Usage: Read text files (.txt) and extracting important data's
# Author: Khairul Izwan Bin Kamsani (wansnap@gmail.com)

# References: 
# https://www.pythontutorial.net/python-basics/python-read-text-file/
# https://www.geeksforgeeks.org/count-number-of-lines-in-a-text-file-in-python/

# -------------------------------------------------

#with open('int8_batch1.txt') as f:
#	for line in f:
#		print(line.strip())

# Opening a file 
file = open("GPU-int8_resnet-50.txt","r") 
Counter = 0

# Reading from file 
Content = file.read() 
CoList = Content.split("\n")

print(Content)

for i in CoList: 
	if i: 
		Counter += 1

print("This is the number of lines in the file") 
print(Counter)

#=== Model Options ===
#Format:
print(CoList[2])

#=== Model Options ===
#Prototxt:
print(CoList[4])

#=== Build Options ===
#Precision:
print(CoList[11])

#=== Inference Options ===
#Batch:
print(CoList[27])

#=== Reporting Options ===
#throughput:
print(CoList[80])

#=== Inference Options ===
#Batch:
print(CoList[121])

#=== Reporting Options ===
#throughput:
print(CoList[161])

#=== Inference Options ===
#Batch:
print(CoList[202])

#=== Reporting Options ===
#throughput:
print(CoList[240])

#=== Inference Options ===
#Batch:
print(CoList[281])

#=== Reporting Options ===
#throughput:
print(CoList[318])

#=== Inference Options ===
#Batch:
print(CoList[359])

#=== Reporting Options ===
#throughput:
print(CoList[395])

#=== Inference Options ===
#Batch:
print(CoList[436])

#=== Reporting Options ===
#throughput:
print(CoList[472])

#=== Inference Options ===
#Batch:
print(CoList[513])

#=== Reporting Options ===
#throughput:
print(CoList[549])
