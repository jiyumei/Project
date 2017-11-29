#draw an ellipse in random location  
#store location in a variable (PVector is optional)
#using the mousePressed() function (outside of draw() function), when user clicks
#assign new location for ball
#in that same function, add one to a score variable 
#display score using text() function

ballX = 30
ballY = 30
score = 0

def setup():
    size(400, 400)
    
def draw():
    #background
    background(255)
    beginning = color(5, 5, 99)
    ending = color(5, 201, 187)
    
    for i in range(401):
        stroke(lerpColor(beginning, ending, i/500.0))
        line(0, i, width, i)
    
    #Ball
    global ballX 
    global ballY
    
    fill(0)
    stroke(255)
    ellipse(ballX, ballY, 30, 30)
    
    #Score
    global score
    
    textSize(20)
    fill(201, 248, 247)
    text("score:", 10, 25)
    text(score, 72, 25)
    
def mousePressed():
#Now, when the user clicks, use the mouseX and mouseY variables, within the
   #mousePressed() function, compare those values to the location of the ellipse. 
   #If the mouse location is within a certain range, then you add to the 
   #score and change the ellipse location.
#add a second ball, with its own position variable, and its own score, and
   #its own click detection in the mousePressed() function.
#if a player reaches a score of 10, they win. Code this

    global ballX
    global ballY
    
    ballX = random(30, 390)
    ballY = random(30, 390)
    
    if mouseX == ballX:
        score += 1
        
    

    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        