T = int(raw_input())

for x in range(T):
	S = raw_input()
	tokens = list(S)
	tokens = tokens[::-1]
	S = ''.join(str(alphabet) for alphabet in tokens)
	print S