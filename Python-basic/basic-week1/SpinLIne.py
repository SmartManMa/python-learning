#SpinLIne.py
import turtle as tt
import time
tt.pensize(2)
tt.bgcolor("black")
colors = ['red','yellow','purple','blue']
tt.tracer(False)
for x in range(400):
	tt.forward(10*x)
	tt.color(colors[x%4])
	tt.left(95)
tt.tracer(True)
time.sleep(10)