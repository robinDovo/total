total = 0
for i in range(2,20,2):
	if i == 10:
		continue;
	else:
		total += i
		print('計數器：',i,'總和：',total);