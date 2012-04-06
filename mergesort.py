a = [9, 2, 4, 2, 5, 3, 1, 8, 7, 6]

#merge module
def merge (b, c) :
	bl = len(b)
	cl = len(c)
	if bl == 0 :
		return c
	if cl == 0 :
		return b
	d = [] 
	i = 0
	j = 0
	k = 0
#elements copied to new list	
	while j < bl and k < cl :
		if b[j] < c[k] :
			d.append(b[j])
			j = j + 1
		else :
			d.append(c[k])
			k = k + 1
#check for remaining elements in lists
	if j < bl :
			d += b[j:]
		
	if k < cl :
			d += c[k:]
		 		
	return d		

#merge sort	
def merge_sort (arr) :
	l  = len(arr)
	d = []
	if l > 1 :
		arr1 = arr[:l/2]
		arr2 = arr[l/2 : ]
		b =  merge_sort (arr1) 
		c =  merge_sort (arr2) 
		d =  merge (b, c) 
		return d
	else :	
		return arr
	
print merge_sort (a)
print a