T = int(raw_input())
TT = raw_input().split()
N, X = int(TT[0]), int(TT[1])

for x in range(T):
	friends_cost = []
	current_sum = 0
	start = 0
	found = False
	for i in range(N):
		friends_cost.append(int(raw_input()))

	for i in range(N):

		current_sum += friends_cost[i]

		while current_sum > X:
			current_sum -= friends_cost[start]
			start += 1

		if current_sum == X:
			print "YES"
			found = True
			break
	if not found:
		print "NO"
	