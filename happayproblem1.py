
T = int(raw_input())

for t in range(T):
	XY = raw_input().split(' ')
	N, M = int(XY[0]), int(XY[1])
	K = int(raw_input())
	step_count = 0
	x = 1
	y = 1
	for k in range(K):
		AB = raw_input().split(' ')
		X, Y = int(AB[0]), int(AB[1])

		mark  = False
		

		while not mark :
			if x+X in range(1, N+1) and y+Y in range(1, M+1):
				x = x+X
				y =  y+Y
				step_count += 1
			else :
				mark = True
			
	print step_count


