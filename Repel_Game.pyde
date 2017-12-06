#PVectors
ballSize = 50
speed = PVector(3, 6) 
posNon = PVector(50, 50) #position for non player ellipse 
score = 0

def setup():
    size(600, 600)
    frameRate(60)
    
def draw():
  background(255)
  
  #player ellipse
  global ballSize
  posPlayer = PVector(mouseX, mouseY)
  
  #Detection of Non Player Sprite
  radius = ballSize/2 
  
  noFill()
  stroke(0)
  strokeWeight(3)
  ellipse(posPlayer.x, posPlayer.y, ballSize, ballSize)
  
  #non player ellipse
  global posNon
  
  noStroke()
  fill(0)
  ellipse(posNon.x, posNon.y, ballSize, ballSize)
  
  posNon.add(speed)
  
  if posNon.x > width:
    posNon.x = width
    speed.x = -speed.x
  elif posNon.x < 0:
    posNon.x = 0
    speed.x = -speed.x
    
  if posNon.y > height:
    posNon.y = height
    speed.y = -speed.y
  elif posNon.y < 0:
    posNon.y = 0
    speed.y = -speed.y
 
 #score
  textSize(30)
  text("score:", 20, 40)
  text(score, 115, 40)
  fill(0)






  
  
  

  
  
  
  
  
  
  
  
  
  
  
