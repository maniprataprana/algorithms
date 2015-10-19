T = int(raw_input())

for x in range(T):
	S = raw_input()
	tokens = list(S)
	elements = []
	j = 0
	for i in range(len(tokens)):
		if not elements:
			j = i
			j+=1
			elements.append(tokens[i])
		else:
			if elements[j-1] != tokens[i] :
				elements.append(tokens[i])
				j+=1

	S = ''.join(str(alphabet) for alphabet in elements)
	print S