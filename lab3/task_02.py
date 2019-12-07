from graph import *

# windowSize(500, 600)
# print(windowSize())

# # Рисую траву
penColor("#32CD32")
brushColor("#32CD32")
rectangle(0, 400, 500, 600)

# Рисую небо
penColor("#1E90FF")
brushColor("#1E90FF")
rectangle(0, 0, 500, 100)

# Рисую забор
penColor("#DAA520")
brushColor("#DAA520")
rectangle(0, 100, 500, 400)
penColor("#000000")
line(0, 400, 500, 400)

n = 500 / 15
for i in range(15):
    line(n, 400, n, 100)
    n += 500 / 15

# Рисую Будку 
penColor("#000000")
brushColor("#DAA520")
polygon( [(340, 410), (440, 430), (440, 550),
          (340, 530), (340, 410)] )

polygon( [(440, 430), (440, 550), (470, 530),
          (470, 410), (440, 430)] )

brushColor("#B8860B")
polygon( [(340, 410), (440, 430), (400, 350), (340, 410)] )
polygon( [(400, 350), (425, 325), (470, 410),
          (440, 430), (400, 350)] )

brushColor("#000000")
circle(390, 470, 30)


run()