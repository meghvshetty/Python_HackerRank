n=input()
a=int(n)%2
b=int(a)
if b!=0:
	print('Weird')
elif 2<=int(n)<=5:
	print('Not Weird')
elif 6<=int(n)<=20:
	print('Weird')
else:
	print('Not Weird')