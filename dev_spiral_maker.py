import turtle
#colors = [ "pink","yellow","blue","green","white","red"]
sketch = turtle.Pen()
turtle.bgcolor("black")
turtle.speed(1000)
sketch.pencolor("white")
for i in range(200):
   #sketch.pencolor(colors[i % 6])
   sketch.width(i/100 + 1)
   sketch.forward(i)
   sketch.left(59)
turtle.mainloop()