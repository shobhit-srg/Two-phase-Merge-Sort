import csv
import sys
import os
import math
from collections import OrderedDict
from itertools import islice
import heapq


class tuple1:
 #    entry = []
	# def print():
	# 	print(entry)
    
    def __lt__(self,other):
        global as_ds
        global cols
		# cols1=[]
		# tchunks1=0
		# as_ds1=0
		# heap1=[]
        if as_ds == 1:
            for i in cols:
                if self.entry[i] < other.entry[i]:
                    return True
                if self.entry[i] > other.entry[i]:
                    return False
            return False
        else:
   #      	cols11=[]
			# tchunks11=0
			# as_ds11=0
			# heap11=[]
            for i in cols:
                if self.entry[i] > other.entry[i]:
                    return True
                if self.entry[i] < other.entry[i]:
                    return False
            return False

    def __init__(self,row):
        self.entry = row




def main():
	
	f=open('./metadata.txt','r') 
	f1=f.readlines()
	col_siz=0
	for x in f1:
		y=(x.split(",")[1])
		y=y.split("\n")[0]
		col_siz+=int(y)
	# print(col_siz)
	f.close()
	# print("Name of Input File ")
	# in_file=input()
	# print("Name of output File ")
	# out_file=input()
	print("1 for asc/2 for desc")
	as_ds=int(input())

	print("Ram size")
	ram_siz=int(input())

	factors=ram_siz//col_siz  #kitne columns ek baar me

	print("On columns")
	col=input().split()
	cols=col
	cols = [int(i) for i in cols]
	# print(col)
	# print(cols)
	# print(col[1])

	f=open('./input.txt','r')
	f1=f.readlines()
	total_elements=0
	for x in f1:
		total_elements+=1
	f.close()
	# print(total_elements)

	chunks=math.ceil((float)(total_elements/factors))
	# print(chunks)
	listOfLines = list()        
	with open ("input1.txt", "r") as myfile:
	    for line in myfile:
	        listOfLines.append(line.strip())

	# print(listOfLines)
	datavec=[]
	j=0
	fd=[]
	for i in range(0,chunks):
		tchunks=chunks
		tempc=factors
		while(tempc):
			if(j>=len(listOfLines)):
				break
			# print(j)
			x=listOfLines[j].split("  ")
			# print(x)
			# print(tempc)
			datavec.append(x)
			j+=1
			tempc-=1

		if(as_ds==1):
			datavec.sort(key=lambda x: (x[cols[0]] , x[cols[1]] , x[cols[2]]))
		else:
			datavec.sort(key=lambda x: (x[cols[0]] , x[cols[1]] , x[cols[2]]),reverse=True)
		# print(datavec)

		file_="file_"+str(i)
		fd.append(file_)
		# print(file_)

		with open(file_, 'w') as f:
			for item in datavec:
				# f.write("%s\n" % item)
				rowt = ""
				for k in item:
					rowt = rowt + str(k ) + "  "
				rowt = rowt.strip("  ")
				f.write(rowt+"\n")
			f.close()
		datavec.clear()


	mergerheap = []
	files=[]
	for i in range(chunks):
		filename = "file_"+str(i)
		temp = open(filename,"r+")
		files.append(temp)
	# print(files)
	opfile = open("opfilename.txt","w+")
	for i in range(chunks):
		temp1 = files[i].readline()
		temp = temp1.strip("\n")
		temp = temp.split("  ")
		# print(temp)
		heapq.heappush(mergerheap,(tuple1(temp),i))
	loop = 0
	while len(mergerheap) > 0:
		loop = loop + 1
		min = heapq.heappop(mergerheap)
		index = min[1]
		temp = files[index].readline()
		if temp != '':
			temp = temp.strip("\n")
			temp = temp.split("  ")
			heapq.heappush(mergerheap,(tuple1(temp),index))
		# print("writing ",min[0].entry)
		for i in min[0].entry:
			opfile.write(str(i) + ",")
		opfile.write("\n")
	opfile.close()
	# print("Loop ",loop)
	datavec1=[]
	f=open('./input.txt','r')
	f1=f.readlines()
	for x in f1:
		x=x.strip("\n")
		x=x.split("  ")
		datavec1.append(x)
	print(datavec1)
	if(as_ds==1):
		datavec1.sort(key=lambda x: (x[cols[0]] , x[cols[1]] , x[cols[2]]))
	else:
		datavec1.sort(key=lambda x: (x[cols[0]] , x[cols[1]] , x[cols[2]]),reverse=True)

	opfile1=open("opfilename.txt","w+")
	for x in datavec1:
		# print(x)
		# x=x.split(",")
		# print(x)
		opfile1.write(str(x))
		opfile1.write("\n")
	opfile1.close()

if __name__ == '__main__':
	cols=[]
	tchunks=0
	as_ds=0
	heap=[]
	main()