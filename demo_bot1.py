from sys import argv

script = argv
prompt = '> '
print "Hi, I am a %s script . You can chat with me" %script
print "I'd like to ask you a few questions."

print "What's your name ?"
name = raw_input(prompt).strip("\n")

print "Nice meeting you", name,"."
print "Talk to me", name,"."

ques = []
phrase = "What makes you say "
while True :
	inp = raw_input(prompt).strip("\n")
	if inp == 'bye' :
		break
	ques = inp.split()
	
	ans = phrase
	for e in ques :
		if e == 'you' :
			ans = ans + ' I '
		elif e == 'are' :
			ans = ans + ' am '
		else :	
			ans = ans + " " + e
	print ans," ?"	
print "Bye ",name,"!!"		