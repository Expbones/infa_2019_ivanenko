from graph import *

# Рисуем основной круг
penColor("black")
penSize(3)
brushColor("yellow")
circle(250, 300, 200)

# Рисуем глаза
brushColor("red")
circle(150, 250, 40)
brushColor("black")
circle(150, 250, 15)

brushColor("red")
circle(350, 250, 30)
brushColor("black")
circle(350, 250, 15)

# Рисуем рот
rectangle(150, 400, 350, 440)

# Рисуем брови
penSize(20)
line(50, 140, 210, 230)
penSize(25)
line(300, 230, 460, 130)

# polygon([(60, 90), (200, 225),
#          (200, 225), (100, 100)])
# Рисуем треугольник
# brushColor("yellow")
# polygon([(100, 100), (200, 50),
#          (300, 100), (100, 100)])
# Рисуем круг
# penColor("white")
# brushColor("green")
# circle(200, 150, 50)

run()