# starting = [0, 1]
#
#
# def fibonacci(num):
# 	while len(starting) <= num:
# 		starting.append((starting[len(starting) - 1] + starting[len(starting) - 2]))
# 	print(starting)
#
#
# fibonacci(20000)

def fib(number):
	a = 0
	b = 1
	for i in range(number + 1):
		yield a
		c = a
		a = b
		b = c + b


for num in fib(20):
	print(num)