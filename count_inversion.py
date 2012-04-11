#count no of inversions in an list. 
#using the merge sort adaptation

from sys import argv



def merge (arraylist1, arraylist2) : 
	l1 = len(arraylist1)
	l2 = len(arraylist2)
	
	if l1 == 0 :
		return arraylist2, 0
	if l2 == 0 :
		return arraylist1, 0
		
	count = 0
	arraylist3 = []
	
	i = 0
	j = 0
	
	while i < l1 and j < l2 :
		if arraylist1[i] <= arraylist2[j] :
			arraylist3.append(arraylist1[i])
			i += 1
		else :
			arraylist3.append(arraylist2[j])
			j += 1	
			#imp  as elements on right side alawys be smaller than all elements coming after the first larger element 
			count += (l1 - i)			
	
	if i < l1 :
		arraylist3 += arraylist1[i:]
	if j < l2 :
		arraylist3 += arraylist2[j:]	
	
#	print arraylist3
	return 	arraylist3, count
	
def sort_and_count(arr) :
	l = len(arr) 
	joint = []
	if l > 1 :
		left, x = sort_and_count(arr[:l/2])
		right, y  = sort_and_count(arr[l/2:])
		joint, z  = merge(left, right)
		#print joint
		return joint, (x + y + z)
	else :	
		return 	arr, 0
	

script, filename = argv
inputstr = [ ]
for line in open(filename,'r').readlines():	
	inputstr.append(int(line))
	
print sort_and_count(inputstr) 