# NineByNine.py
for i in range(1,10):
	for j in range(1,i+1):
		print("{}*{}={}".format(j,i,i*j),end='   ')
	print(' ')

# 阶乘和1！+2！+3！+++
sum = 0
temp = 1
for i in range(1,11):
	temp *= i
	sum += temp
print("运算结果：{}".format(sum))