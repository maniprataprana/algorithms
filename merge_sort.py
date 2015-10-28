A = [22,27,1,8 ,9, 10, 20, 88, 77, 101, 66 , 44,77]

def merge(left, right):
	n1 = len(left)
	n2 = len(right)

	if n1 == 0:
		return right
	if n2 == 0:
		return left

	lr = []

	i = 0
	j = 0


	while i < n1 and j < n2:
		if left[i] >= right[j]:
			lr.append(left[i])
			i += 1
		else:
			lr.append(right[j])
			j += 1

	if (i < n1) :
		for j in range(i,n1):
			lr.append(left[j])

	elif (j < n2) :
		for j in range(j,n2):
			lr.append(right[j])

	return lr

def merge_sort(A):
	l = len(A)
	if l > 1:
		mid = int(l/2)
		left = merge_sort(A[:mid])
		right = merge_sort(A[mid:])
		newA = merge(left, right)
		return newA
	else :
		return A

T = int(raw_input())
for t in range(T):
	N = int(raw_input())
	A = raw_input().split(' ')
	A = map(int, A)
	A = merge_sort(A)
	print ' '.join(map(str, A))
