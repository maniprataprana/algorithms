#implementataion of linear random selection algorithm
# returns the i'th smallest element inn O(n) time ie Linear time
#pivot selection : first element of list
def radnom_selection(A, start, end, order_i_statistic):
	n = len(A)
	if n == 1 or start == end:
		return A[start]
	split = partition(A, start, end)
	p_split = split - start + 1
	if p_split == order_i_statistic  :
		return A[split]
	elif p_split > order_i_statistic :	
		return radnom_selection(A, start, split - 1, order_i_statistic)
	else :	
		return radnom_selection(A, split + 1 , end, order_i_statistic - p_split)

# partition function to get pivot element	
def partition(A,start,end):
	pivot = A[start]
	i = start + 1
	
	for j in range(start+1,end) :
		if A[j] < pivot :
			A[j], A[i] = A[i], A[j]
			i = i + 1
					 
	A[start], A[i-1]=A[i-1], A[start]
	return i - 1

A = [2, 4, 1, 6, 7, 3, 8, 5, 9]

#sample test  run
print radnom_selection(A, 0, 9, 3)