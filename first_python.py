g = (x * x for x in range(10))
for n in g:
	print(n)

def fib(max):
	n,a,b = 0,0,1
	while n < max:
		yield b
		a,b = b,a+b
		n = n + 1
	return 'done'
f = fib(6)
print(f)

for n in fib(6):
	print(n)

g = fib(6)
while True:
	try:
		x = next(g)
		print('g:',x)
	except StopIteration as e:
		print('Generator return value:',e.value)
		break

#git test
#git is a dirstributed version control system.
#git is free software distributed under the GPL
#git has a mutable index called stage
#git tracks changes of files.
#my stupid boss still prefers SVN

#Git is very good version control system

