a = int(raw_input("inter number a"))
b = int(raw_input("inter number b"))
operator = raw_input('enter arithmatic operator')
if operator == '+':
	c = a+b
	print 'addition of two no is:',c
elif operator == '-':
	c = a-b
	print 'substraction of two no is:',c

elif operator == '*':
	c = a*b
	print 'multiplication of two no is:',c

elif operator == '%':
	c = a%b
	print 'modulo of two no is:',c


elif operator == '/':
	c = a/b
	print 'division of two no is:',c

else:
	print "wrong input"

print "end"
