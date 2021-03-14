s = "Ahmed Mosuatafa Mourad"

words = s.split()
stack = []
for i in words:
	stack.append(i[::-1])

out = ''
for i in range(len(stack)):
	out += stack.pop(0)
	out += " "

print(out)	

