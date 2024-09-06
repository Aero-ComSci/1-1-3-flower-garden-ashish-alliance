# draw flower
painter.color("darkorchid")
painter.goto(20,190)

for petal in range(18):
  painter.right(20)
  painter.forward(30)
  painter.stamp()

# ring 2 of flower
painter.goto(20,160)
painter.color("blue")

for petal in range(12):
  painter.right(30)
  painter.forward(30)
  painter.stamp()
  
wn = trtl.Screen()
wn.mainloop()
