def getReverseGCD(g, n):
	output_array = [str(g*2)]*n
	output_array[n-1] = str(g * 3)
	return ' '.join(output_array)

T = int(raw_input())

for x in range(T):
	TT = raw_input().split()
	g, n = int(TT[0]), int(TT[1])
	
	print getReverseGCD(g, n)