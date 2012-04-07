def quicksort(A,begin,end) :
	if begin < end :
		split = partition(A,begin,end)
		quicksort(A,begin,split-1)				
		quicksort(A,split+1,end)
	

def partition(A,begin,end) :
	pivot = A[end]
	i = begin - 1

	for j in range(begin,end) :
		if A[j] <= pivot :
			i = i + 1					
			A[i], A[j] = A[j], A[i]			
			
	A[i+1], A[end] = A[end], A[i+1]
	return i+1
	
#use any array like below to sort
A = [3,8,2,5,1,4,7,6] 

quicksort(A,0,len(A)-1)
print A