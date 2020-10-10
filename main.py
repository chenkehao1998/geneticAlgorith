from route import *
from graphics import *

cityList = []
# 随机创建25个城市
for i in range(0,25):
    cityList.append(City(x=int(random.random() * 200), y=int(random.random() * 200)))

win = GraphWin("city-map", 800, 800)
win.setCoords(0, 0, 200, 200)
for city in cityList:
    circle=Circle(Point(city.x,city.y),1)
    circle.setFill("red")
    circle.draw(win)

# 每代100个个体，保留20个精英个体，给定基因的变异率为1%，运行500代
route,plt=geneticAlgorithmPlot(population=cityList, popSize=100, eliteSize=20, mutationRate=0.01, generations=500)
for i in range(len(route)):
    start = Point(route[i].x, route[i].y)
    if i <len(route)-1:
        end=Point(route[i+1].x,route[i+1].y)
    else:
        end =Point(route[0].x,route[0].y)
    line = Line(start,end)
    line.setArrow("last")
    line.draw(win)

plt.show()
win.close()
