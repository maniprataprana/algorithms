#The file contains all of the integers between 1 and 10,000 (inclusive) 
#in unsorted order (with no integer repeated). 
#The integer in the ith row of the file gives you the ith entry of an input array.
#Your task is to compute the total number of comparisons used to sort the given input file by QuickSort. 
#As you know, the number of comparisons depends on which elements are chosen as pivots, 
#so we'll ask you to explore three different pivoting rules.
#You should not count comparisons one-by-one.
#Compute the number of comparisons (as in Problem 1),
# always using the final element of the given array as the pivot element.


from sys import argv

def quicksort(A,begin,end) :
	count = 0
	if end - begin <= 1:
		return 0
	else :
		#swap done here
		A[begin], A[end-1] = A[end-1] , A[begin]
		split = partition(A,begin,end)
		count = end - begin - 1
		lc = quicksort(A,begin,split)				
		rc = quicksort(A,split+1,end)
		return count + lc + rc
	

def partition(A,begin,end) :
	pivot = A[begin]
	i = begin + 1

	for j in range(begin+1,end) :
		if A[j] < pivot :					
			A[i], A[j] = A[j], A[i]
			i = i + 1			
			
	A[i-1], A[begin] = A[begin], A[i-1]
	return i-1
	
#use any array like below to sort
script, filename = argv
A = [ ]
for line in open(filename,'r').readlines():	
	A.append(int(line))

print len(A)
print quicksort(A,0,len(A))
