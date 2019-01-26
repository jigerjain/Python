def generator(n):
	for i in range(n):
		yield i+10

a = list(generator(10))
print(a)

print(generator(10))

for i in generator(10):
	print(i)
