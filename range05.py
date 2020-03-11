for i in range(2,10):
	for x in range(1,i):
		print(x,end='')
	print();

data = [10,'Jhon', 3.14, True]
data2 = [10,20,30,40]

print(data[1])
print(data2[0])

print('-'*30)

for i in range(len(data)):
	print(data[i])

print('-'*30)

for i in range(4):
	print(data[i])

print('-'*30)

print(data[-1])
print('-'*30)
print(data[-2])
print('-'*30)

data2[1] = 100
print(data2[1])
for x in data:
	print(x)

