
def bubbleSort(x):  
	length = len(x)-1
	count = 0
	for i in range(length):
		for j in range(length-i):
			if x[j] > x[j+1]:
				x[j], x[j+1] = x[j+1], x[j]
				count += 1
	print "Count : " + str(count)
	return x


import random
print "Enter the Number"
j = int(raw_input())
while(j!=0):
        j+=1
        list = [1]*j
        for i in range(j):
              list = random.sample(range(1,j),j-1)

        print "Not Sort"
        print list

        bubbleSort(list)
        print "Sort"
        print list
        
        print "Enter the Number"
        j = int(raw_input())

print "Exit"
