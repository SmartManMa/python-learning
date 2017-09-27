# TempConvert.py
val = input("输入温度：")
if val[-1] in ['C','c']:
	f = 1.8 * float(val[0:-1]) + 32
	print("华氏温度为%0.2fF" %f)
elif val[-1] in ['F','f']:
	c = (float(val[0:-1]) - 32) / 1.8
	print("摄氏温度为%0.2fC" %c)
else:
	print("温度格式错误")
	