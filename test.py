from graphics import *
win= GraphWin()
origin= Point(100,100)

## Head
circle=Circle(origin,50)
circle.draw(win)
eyeLeft=Point(80,80)
eyeRight=Point(120,80)
eyeLeft.draw(win)
eyeRight.draw(win)

## Draws a mouth
topLip=Line(Point(70,120),Point(140,120))
bottomLip=Line(Point(80,135),Point(130,135))
connectJawRight=Line(Point(70,120),Point(80,135))
connectJawLeft=Line(Point(140,120),Point(130,135))
bottomLip.draw(win)
topLip.draw(win)
connectJawRight.draw(win)
connectJawLeft.draw(win)

## Hat Drawing(part 1)
rectangle= Rectangle(Point(50,40),Point(150,60))
rectangle.setFill("red")
rectangle.draw(win)

## Hat Drawing(part 2)
rectangle2= Rectangle(Point(85,10),Point(115,40))
rectangle2.draw(win)
rectangle2.setFill("black")

##Body
oval= Oval(Point(80,150),Point(120,201))
oval.draw(win)

##Arms
armRight= Line(Point(120,170),Point(150,170))
armRight.draw(win)
armLeft= armRight.clone()
armLeft.move(-70,0)
armLeft.draw(win)


##Draws Teeth
for i in range(6):
    Rectangle(Point(85+(i*4),120),Point(100+(i*4),125)).clone().draw(win)
for i in range(6):
    Rectangle(Point(85+(i*4),130),Point(100+(i*4),135)).clone().draw(win)
