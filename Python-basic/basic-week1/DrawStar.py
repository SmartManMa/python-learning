# DrawStar.py
from turtle import *
color('red','yellow')
# fillcolor("red")
# setx(-100)
# sety(100)
begin_fill()
while True:
	forward(200)
	left(160)
	if abs(pos())<1:
		break
end_fill()
done()

