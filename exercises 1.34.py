def drawSpiral(myTurtle, maxSide):
     for sideLength in range(1,maxSide+1,5):
          myTurtle.forward(sideLength)
          myTurtle.right(75)
