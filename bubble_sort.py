def bubble_sort(A):
	for i in range(len(A)):
		for j in range(len(A)-i-1):
			if A[j] > A[j+1]:
				A[j+1],A[j] = A[j],A[j+1]
	return A

print bubble_sort([22,1,5,9,22,7,10,44,1])