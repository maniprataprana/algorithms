T = int(raw_input())

for x in range(T):
	TT = raw_input().split()
	N, K, M = int(TT[0]), int(TT[1]), int(TT[2])
	
	str_array = []
	for y in range(N):
		z = raw_input()
		str_array.append(z)

	str_array = sorted(str_array, key=lambda x:x[:M])
	print str_array[K-1]