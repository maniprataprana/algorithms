def insertion_sort(A):
	for i in range(len(A)):
		temp = A[i]
		j = i
		while temp < A[j-1] and j > 0:
			A[j] = A[j-1]
			j -= 1
		A[j] = temp
	return A

print insertion_sort([22,1,5,9,22,7,10,44,1])
